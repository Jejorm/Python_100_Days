from flask import Flask, render_template
from post import Post
import requests

POSTS_ENDPOINT = "https://api.npoint.io/ed99320662742443cc5b"

app = Flask(__name__)


def refresh_api():
    posts = requests.get(POSTS_ENDPOINT).json()
    post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in posts]

    return post_objects


@app.route("/")
def home():
    posts = refresh_api()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:blog_post_id>")
def post(blog_post_id):
    posts = refresh_api()
    requested_post = {}

    for post in posts:
        if post.post_id == blog_post_id:
            requested_post = post 

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
