from flask import render_template, flash, url_for, Blueprint, redirect
from portfolio.aplikasi.form import ContactForm
from portfolio import mail
from flask_mail import Message

jarak = Blueprint('jarak', __name__)

@jarak.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        if form.send_copy.data:
            msg = Message("Message from " + name + " (Nabil Muqri Contact Form)", sender="pythonnabil@gmail.com", recipients=["nabilmuqri@protonmail.com"], cc=[email] )
        else:
            msg = Message("Message from " + name + " (Nabil Muqri Contact Form)", sender=email, recipients=["nabilmuqri@protonmail.com"])
        msg.body = f'''{message}'''
        mail.send(msg)
        flash('Successfully send message', 'success')
        return redirect(url_for('jarak.home'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    portfolio.run(host='127.0.0.1', port=8000, debug=True)