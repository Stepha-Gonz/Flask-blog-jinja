from flask import Flask, render_template
import requests
from post import Post
blog_url="https://api.npoint.io/673ccc80824705651391"
blog_response=requests.get(blog_url)
blog_data=blog_response.json()
blog_info=[]
for blog_post in blog_data:
    blog_obj=Post(blog_post["id"],blog_post["title"],blog_post["subtitle"],blog_post["body"])
    blog_info.append(blog_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts=blog_info)

@app.route("/post/<int:id>")
def post(id):
    requested_post= None
    for blog_post in blog_info:
        if blog_post.id==id:
            requested_post=blog_post
    return render_template("post.html",post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
