from flask import Flask, render_template, request

app = Flask(__name__)

APP_NAME = 'GameShop'
HEADER_MSG = 'Buy Games At Best Deals'
HEADER_SUB = 'Discover Top Titles at Unbeatable Prices - Limited-Time Offers!'

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


@app.route('/register', endpoint='register')
def register():
    data = {
        'app_name': APP_NAME,
        'header_msg': HEADER_MSG,
        'header_sub': HEADER_SUB,
        'route_name': request.endpoint.capitalize()
    }
    return render_template('register.html', data=data)

@app.route('/login', endpoint='login')
def login():
    data = {
        'app_name': APP_NAME,
        'header_msg': HEADER_MSG,
        'header_sub': HEADER_SUB,
        'route_name': request.endpoint.capitalize()
    }
    return render_template('login.html', data=data)



if __name__ == '__main__':
    app.run(
        debug=True,
    )