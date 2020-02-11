from application import db

from flask import render_template, redirect, url_for
from flask_login import login_required

from datetime import datetime

from . import blog
from .forms import *
from ..models import *

@blog.route('/<int:post_number>',methods=['GET','POST'])
def blog_page(post_number):
    try:
        list_post = Post.query.order_by(Post.id.desc()).all()
        post = list_post[post_number]
        image = 'images/' + post.feeling + '.png'
        return render_template('blog/blog_main_page.html', post_number = post_number, list_post = list_post, post = post, image = image)
    except IndexError:
        return redirect(url_for('blog.blog_page',post_number=0))


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
