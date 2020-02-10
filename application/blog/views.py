from flask import render_template, redirect, url_for
from flask_login import login_required

from . import blog

@blog.route('/',methods=['GET','POST'])
def blog_page():
    return render_template('blog/blog_main_page.html')
