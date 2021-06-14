from ecommerce import app
from flask import render_template,session,request
# from ecommerce.controllers.customer_controller import CustomerController
from ecommerce.controllers.category_controller import CategoryController

@app.route('/')
def home():
    top_3_categories = CategoryController().top_3_categories()
    return render_template('customer/home.html', showCarousel=True, response={'top_3_categories': top_3_categories})


@app.route('/about-us')
def about():
    return render_template('customer/about.html', title='About Us')


@app.route('/contact-us')
def contact():
    return render_template('customer/contact.html', title='Contact Us')


@app.route('/login')
def login():
    return render_template('customer/auth/login.html', title='Login')


@app.route('/register')
def register():
    return render_template('customer/auth/registration.html', title='Registration')


@app.route('/categories/<category>')
def categories(category):
    return render_template('customer/categories.html', title=category, showPageBanner=True)


@app.route('/products/<product>')
def products(product):
    return render_template('customer/products.html', title=product)


@app.route('/cart')
def cart():
    return render_template('customer/cart.html', title='Cart')


@app.route('/checkout')
def checkout():
    return render_template('customer/checkout.html', title='Checkout')


@app.route('/search')
def search():
    return render_template('customer/search.html', title='Search')



# newly added
# to display product categories in header
# @app.route('/')
# def product_categories_to_menu():
#     product_category = CategoryController().product_category()
#     return render_template('/navbar.html',product_category="product_category")

def render_template_with_nav(html_page, **kwargs):
    categories = CategoryController().index()
    auth = session.get('auth')
    cart = []
    if auth:
        cart = CategoryController().get(auth[0]['customer_id'])

    return render_template(html_page, title=kwargs.get('title'), showCarousel=kwargs.get('showCarousel'),
                           categories=categories, auth=auth, cart=cart, response=kwargs.get('response'))
