from flask import (
    Flask, 
    render_template, 
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    UserMixin,
    current_user
)

from flask_wtf import CSRFProtect

from werkzeug.security import generate_password_hash, check_password_hash

# Import the db and User model
from models import db, User, init_db
from forms import RegistrationForm, LoginForm
from site_constant import (APP_NAME, HEADER_MSG, HEADER_SUB)

app = Flask(__name__)
app.secret_key = 'supersecretkey243#$@asFKR#+-9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gameshop.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
init_db(app)


# # Flask-Login setup
login_manager = LoginManager()
# login_manager.login_view = 'login'
login_manager.init_app(app)

csrf = CSRFProtect(app)

# for login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', endpoint='home')
def home():
    data = {
        'app_name': APP_NAME,
        'header_msg': HEADER_MSG,
        'header_sub': HEADER_SUB,
        'route_name': request.endpoint.capitalize()
    }
    return render_template('home.html', data=data)


@app.route('/shop', endpoint='shop')
def shop():
    data = {
        'app_name': APP_NAME,
        'header_msg': HEADER_MSG,
        'header_sub': HEADER_SUB,
        'route_name': request.endpoint.capitalize()
    }
    return render_template('shop.html', data=data)


@app.route('/contact', endpoint='contact')
def contact():
    data = {
        'app_name': APP_NAME,
        'header_msg': HEADER_MSG,
        'header_sub': HEADER_SUB,
        'route_name': request.endpoint.capitalize()
    }
    return render_template('contact.html', data=data)


@app.route('/about', endpoint='about')
def about():
    data = {
        'app_name': APP_NAME,
        'header_msg': HEADER_MSG,
        'header_sub': HEADER_SUB,
        'route_name': request.endpoint.capitalize()
    }
    return render_template('about.html', data=data)


@app.route('/register', endpoint='register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()

    # post request
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))

    data = {
        'app_name': APP_NAME,
        'header_msg': HEADER_MSG,
        'header_sub': HEADER_SUB,
        'route_name': request.endpoint.capitalize(),
    }
    return render_template('register.html', data=data, form=form)


# @app.route('/process-register', methods=['POST'], endpoint='process_register')
# def process_register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data
#         hashed_password = generate_password_hash(password)
        
#         new_user = User(email=email, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         flash('Account created successfully!', 'success')
#         return redirect(url_for('login'))
#     return redirect(url_for('register'))


@app.route('/login', endpoint='login', methods=["POST", "GET"])
def login():
    form = LoginForm()

    # post login
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        pass
        flash('invalid credintials', 'error')
        return redirect(url_for('login'))

    data = {
        'app_name': APP_NAME,
        'header_msg': HEADER_MSG,
        'header_sub': HEADER_SUB,
        'route_name': request.endpoint.capitalize()
    }
    return render_template('login.html', data=data, form=form)


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(
        debug=True,
    )