from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction   
from products.models import Product
from . models import Cart,CartItem,Order,OrderItem


@login_required(login_url='login')
def add_to_cart(request,product_id):
    product=get_object_or_404(Product,id=product_id,available=True)
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)

    if not created:
        cart_item.quantity+=1
        cart_item.save()

    messages.success(request,f"{product.name} added to cart.")

    return redirect('cart')

@login_required(login_url='login')
def cart_view(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_items=cart.items.select_related('product')

    total =sum(item.get_total_price() for item in cart_items)

    context = {
        'cart':cart,
        'cart_items':cart_items,
        'total':total,
    }

    return render(request,"orders/cart.html",context)

@login_required(login_url='login')
def update_cart(request,item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if request.method == 'POST':

        action=request.POST.get('action')

        if action == 'increase':
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity +=  1
                cart_item.save()

            else:
                messages.error(
                    request,'You cannot add more than available stock'
                )
        elif action=='decrease':

            if cart_item.quantity>1:
                cart_item.quantity-=1
                cart_item.save()

            else:
                cart_item.delete()

    return redirect('cart')

@login_required(login_url='login')
def remove_from_cart(request, item_id):

    cart_item = get_object_or_404(
        CartItem,id=item_id,cart__user=request.user
    )

    if request.method== 'POST':
        cart_item.delete()


        messages.success(request,"Product removed from cart.")

        return redirect("cart")

@login_required(login_url='login')
def checkout(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('product')

    if not cart_items.exists():
        messages.error(request,'Your cart is empty')
        return redirect('cart')


    if request.method=="POST":

        address=request.POST.get('address')
        phone=request.POST.get('phone')

        # basic validation

        if not address or not phone:
            messages.error(request,'Address and Phone number are required')

            return redirect('checkout')


        # check stock before creating order

        for item in cart_items:
            if item.quantity > item.product.stock:
                messages.error(request,f"Not enoguth stock for {item.product.name}")
                return redirect('cart')
        # Calculate total from database

        total = sum(
        item.get_total_price()
        for item in cart_items
        )

        with transaction.atomic():               

            #create order 

            order=Order.objects.create(
                user=request.user,
                total_amount=total,
                address=address,
                phone=phone
            )

            #Create Orderitems

            for item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price

                )
                #Reduce stock
                item.product.stock -= item.quantity
                item.product.save()

                #clear cart

                cart.items.all().delete()


            messages.success(request,f'order #{order.id} placed successfully!')

            return redirect('cart')
    total = sum(
        item.get_total_price()
        for item in cart_items
    )

    return render(
        request,'orders/checkout.html',{'cart_items':cart_items,'total':total,}
    )

@login_required(login_url='login')
def my_orders(request):

    orders=Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request,'orders/my_orders.html',{'orders':orders})

@login_required(login_url='login')
def order_detail(request,order_id):
    order=get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    order_items = order.items.select_related('product')

    return render(
        request,
        'orders/order_detail.html',
        {
            'order':order,
            'order_items':order_items
        }
    )