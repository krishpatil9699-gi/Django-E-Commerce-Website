# 🛒 Django E-Commerce Web Application

A full-stack e-commerce web application built using **Python, Django, MySQL, HTML, and CSS**. The project provides essential online shopping features such as user authentication, product browsing, search, category filtering, shopping cart management, checkout, stock management, and order tracking.

## 📌 Project Overview

This project was developed to understand and implement the complete workflow of an e-commerce website using Django.

Users can register and log in, browse available products, search for products, filter products by category, add products to their cart, update quantities, place orders, and view their previous orders.

The project also includes server-side validation, user authorization, CSRF protection, stock validation, and database transactions.

---

## 🚀 Features

### 👤 User Authentication

* User registration
* User login
* User logout
* Password authentication using Django's built-in authentication system
* Login-protected pages

### 🛍️ Product Management

* Product listing
* Product detail page
* Product availability
* Product categories
* Product search
* Category filtering
* Stock management

### 🛒 Shopping Cart

* Add products to cart
* Increase product quantity
* Decrease product quantity
* Remove products from cart
* Stock validation
* Automatic cart total calculation

### 📦 Checkout & Orders

* Checkout page
* Address and phone number validation
* Server-side total calculation
* Stock verification before placing an order
* Order creation
* Order item creation
* Automatic stock reduction
* Cart clearing after successful order

### 📋 Order Management

* View all personal orders
* View individual order details
* Order status
* Order date
* Delivery address
* Phone number
* Purchased product price
* Order total

### 🔐 Security & Validation

* Django authentication
* Login-required views
* User-based authorization
* CSRF protection
* Server-side validation
* `get_object_or_404()` for safe object retrieval
* Stock validation
* Database transactions using `transaction.atomic()`

---

## 🛠️ Technologies Used

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Backend programming    |
| Django     | Web framework          |
| MySQL      | Database               |
| HTML5      | Page structure         |
| CSS3       | Styling                |
| Django ORM | Database operations    |
| Git        | Version control        |
| GitHub     | Source code management |

---

## 🏗️ Project Structure

```text
django-ecommerce/
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── products/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── accounts/
│   ├── views.py
│   └── urls.py
│
├── orders/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── base.html
│   ├── products/
│   ├── accounts/
│   └── orders/
│
├── static/
│   └── css/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗄️ Database Models

The application uses relational database models for:

```text
User
  │
  ├── Cart
  │     └── CartItem
  │           └── Product
  │
  └── Order
        └── OrderItem
              └── Product
```

### Main Models

* `Product`
* `Category`
* `Cart`
* `CartItem`
* `Order`
* `OrderItem`
* Django's built-in `User`

---

## 🔄 Order Workflow

```text
User Registration
       ↓
     Login
       ↓
 Browse Products
       ↓
 Search / Category Filter
       ↓
   Product Details
       ↓
    Add to Cart
       ↓
  Manage Cart
       ↓
    Checkout
       ↓
 Validate Address & Phone
       ↓
 Check Product Stock
       ↓
 Calculate Total
       ↓
 Create Order
       ↓
 Create Order Items
       ↓
 Reduce Stock
       ↓
 Clear Cart
       ↓
   My Orders
```

---

## 🔐 Security Implementation

The project uses several Django security practices.

### Authentication

Protected views use Django's:

```python
@login_required
```

### Authorization

Users can only access their own orders and cart items.

Example:

```python
order = get_object_or_404(
    Order,
    id=order_id,
    user=request.user
)
```

### CSRF Protection

POST forms use:

```django
{% csrf_token %}
```

### Server-Side Validation

Important values such as:

* Product price
* Order total
* Quantity
* Stock
* Phone number
* Address

are validated on the server.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate into the project

```bash
cd django-ecommerce
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Create a MySQL database and configure the database settings in Django.

Example:

```sql
CREATE DATABASE djangoshop;
```

### 7. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create an admin account

```bash
python manage.py createsuperuser
```

### 9. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Testing

The application was tested for:

* User registration
* User login/logout
* Product browsing
* Product search
* Category filtering
* Cart operations
* Stock validation
* Checkout
* Order creation
* Order history
* Order ownership/security
* Invalid phone numbers
* Empty cart checkout
* CSRF protection

---

## 🔮 Future Improvements

Possible future enhancements include:

* Online payment gateway
* Product reviews and ratings
* Wishlist
* Coupon and discount system
* User profile management
* Product image upload
* Admin dashboard
* Order cancellation
* Email notifications
* Advanced product filtering
* REST API
* Deployment on a cloud platform

---

## 🎯 Learning Outcomes

Through this project, I practiced:

* Django project and app architecture
* Django Models and relationships
* Django ORM
* CRUD operations
* Authentication and authorization
* Templates and template inheritance
* Dynamic URLs
* GET and POST requests
* Django Forms and validation concepts
* Shopping cart implementation
* Order management
* Database transactions
* CSRF protection
* Server-side validation
* Git and GitHub

---

## 👨‍💻 Author

**Krishna Patil**

BSc Computer Science Graduate
Aspiring Python / Django Full-Stack Developer

---

## 📄 License

This project is created for **learning and educational purposes**.
