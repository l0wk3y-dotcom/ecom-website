from django.conf import settings
from django.core.mail import send_mail

def send_email_activation_mail(email,email_token):
    subject="Activation of mail"
    email_from=settings.EMAIL_HOST_USER
    body=f"Hello click on this link http://127.0.0.1:8000/accounts/activate/{email_token} to activate you email"
    print(subject,email_from,body,[email])