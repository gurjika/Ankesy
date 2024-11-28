from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def send_email_to_parent(data, email):

        # Send the email
        if data.get('opened'):
            data.pop('opened')
            html_content = render_to_string('email_template.html', {'data': data})
            email = EmailMultiAlternatives(
                subject="Revealed Information for Review",
                body="This is an important message regarding flagged information.",
                from_email="WARNING <info@ankesy.com>",
                to=[email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)
        else:
              
            email = EmailMultiAlternatives(
            subject="Information was not revealed",
            body="",
            from_email="<info@ankesy.com>",
            to=[email],
            )
            email.send(fail_silently=False)
              


# @shared_task
# def send_scam():
#     send_mail(
#         subject='You Won an Iphone',
#         message='You Won iphone 13 pro max. Claim it now <link>',
#         from_email='iPhone Giveaway <phhone@win.com>',
#         recipient_list=[email],
#         fail_silently=False ## TESTING
#     )
    # pass