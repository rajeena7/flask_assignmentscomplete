#. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask , render_template


app=Flask(__name__)

@app.route('/')
def index():
    return "Welcome to flask url parameter"



@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s ' %username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id



if __name__=='__main__':
    app.run(host="0.0.0.0" , port=5001)    