from application import db

from flask import render_template, redirect, url_for
from flask_login import login_required

from datetime import datetime

from . import blog
from .forms import *
from ..models import *

@blog.route('/',methods=['GET','POST'])
def blog_page():
    post = Post.query.order_by(Post.id.desc()).first()
    image = 'images/' + post.feeling + '.png'
    return render_template('blog/blog_main_page.html', post = post, image = image)

@blog.route('/post',methods=['GET','POST'])
@login_required
def admin_post():
    form = Form_post()
    thong_bao = ''
    if form.validate_on_submit():
        post = Post()
        post.title = form.title.data
        post.feeling = form.feeling.data
        post.date = datetime.now()
        post.text = form.text.data
        
        db.session.add(post)
        db.session.commit()
        thong_bao = 'Thành công!'


    return render_template('blog/blog_posting_page.html', thong_bao = thong_bao, form=form)
