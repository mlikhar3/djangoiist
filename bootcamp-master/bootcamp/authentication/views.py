from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from bootcamp.authentication.forms import SignUpForm
from bootcamp.feeds.models import Feed

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from .tokens import account_activation_token
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import smtplib


def send_email(fromr, tor, sub, message):
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.starttls()
    conn.login("rasiist2018@gmail.com", "zeecinema1")
    msg = 'Subject: {}\n\n{}'.format(sub, message)
    conn.sendmail(fromr, tor, msg)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'authentication/signup.html',
                          {'form': form})

        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            welcome_post = '{0} has joined the network.'.format(user.username)
            subject="Thankyou for signup"
            message='welcome to Indore institute of Science and Technology'
            from_email=settings.EMAIL_HOST_USER
            to_email=email#,settings.EMAIL_HOST_USER
            print("logging")                                                                                                                                                                                                                                                                                                                                                
            send_email(from_email, to_email, subject, message)

            # def send_email(request):
            #     msg = EmailMessage('Request Callback',
            #            'Here is the message.', to=['charl@byteorbit.com'])
            #     msg.send()
            #     return HttpResponseRedirect('/')
            # feed = Feed(user=user, post=welcome_post)
            # feed.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':account_activation_token.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #             mail_subject, message, to=[to_email]
            # )
            # email.send()
            # return HttpResponse()

            return redirect('/student')


    else:
        return render(request, 'authentication/signup.html',
                      {'form': SignUpForm()})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')