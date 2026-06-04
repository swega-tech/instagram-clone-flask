from flask import Flask, render_template, url_for, flash, redirect, request
from models import db, User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key-12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Automatically generate database tables upon launch
with app.app_context():
    db.create_all()

# --- Feed / Home Page (Read All) ---
@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)

# --- User Registration (Create User) ---
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        bio = request.form.get('bio')
        
        # 1. Validation: Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('That email address is already registered!', 'danger')
            return redirect(url_for('register'))
            
        # 2. Validation: Check password length requirement
        if not password or len(password) < 6:
            flash('Password must be at least 6 characters long!', 'danger')
            return redirect(url_for('register'))
            
        # Save to SQLite if valid
        user = User(username=username, email=email, password=password, bio=bio)
        db.session.add(user)
        db.session.commit()
        flash('User registered successfully!', 'success')
        return redirect(url_for('home'))
        
    return render_template('register.html')

# --- User Profile Page (Read User & User's Posts) ---
@app.route("/user/<int:user_id>")
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user=user)

# --- Create New Post (Create) ---
@app.route("/post/new", methods=['GET', 'POST'])
def create_post():
    user = User.query.first()
    if not user:
        flash('Please register at least one user before posting!', 'danger')
        return redirect(url_for('register'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        image_url = request.form.get('image_url') or "https://via.placeholder.com/500"
        
        post = Post(title=title, content=content, image_url=image_url, author=user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been published!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', legend='Create New Post')

# --- Individual Post Details (Read) ---
@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

# --- Update Existing Post (Update) ---
@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.image_url = request.form.get('image_url')
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post_detail', post_id=post.id))
    
    return render_template('create_post.html', title='Edit Post', legend='Edit Post', post=post)

# --- Delete Post (Delete) ---
@app.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)