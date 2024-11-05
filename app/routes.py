from .models import db, User, Restaurant, Order, MenuItem, OrderItem
from .forms import RegistrationForm, LoginForm, OrderForm

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('main', __name__)

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method = 'scrypt')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)

        db.session.add(user)
        db.session.commit()

        flash('Account Created Successfully!', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html', form = form)

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)

            return redirect(url_for('main.index'))
        
        flash('Invalid Login Credentials!', 'danger')
    
    return render_template('login.html', form = form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/restaurants')
def restaurants():
    res = Restaurant.query.all()

    return render_template('restaurants.html', restaurants = res)

@bp.route('/restaurant/<int:res_id>')
def restaurant_detail(res_id):
    restaurant = Restaurant.query.get_or_404(res_id)

    return render_template('restaurant_detail.html', restaurant = restaurant)

@bp.route('/order', methods = ['GET', 'POST'])
@login_required
def order():
    form = OrderForm()
    form.menu_item_id.choices = [(item.id, item.name) for item in MenuItem.query.all()]

    if form.validate_on_submit():
        order = Order(user_id = current_user.id, status = 'Pending')
        
        db.session.add(order)
        db.session.commit()

        order_item = OrderItem(order_id = order.id, menu_item_id = form.menu_item_id.data, quantity = form.quantity.data)

        db.session.add(order_item)
        db.session.commit()

        flash('Your Order has been placed successfully!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('order.html', form = form)