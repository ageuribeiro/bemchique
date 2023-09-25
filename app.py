from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = '611b32d89900b8a1c215b64cfa212fdb'

app.debug = True
posts = [
    {
        'author': 'Ageu Ribeiro',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },

    {
        'author': 'Ageu Ribeiro',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='Sobre')

@app.route('/vitrine')
def vitrine():
    return render_template('vitrine.html', title=' Vitrine')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts, title='Blog')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contatos')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('blog'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ageu87@gmail.com' and form.password.data == '123':
            flash('You have been logged in!','success')
            return redirect(url_for('blog'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
