from . import main
from .forms import *

from flask import render_template, redirect, url_for, request

@main.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/contact',methods=['GET','POST'])
def contact():
    form = Form_contact()
    if form.validate_on_submit():
        return redirect(url_for('main.redirect_contact'))
    return render_template('contact.html',form=form)

@main.route('/thank-you', methods=['GET','POST'])
def redirect_contact():
    noi_dung = 'Thank you for contacting me! I will reply as soon as possible.'
    return render_template('redirecting_page.html', noi_dung = noi_dung)
