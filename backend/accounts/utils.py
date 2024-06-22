from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from accounts.models import EmailVerification
from y_backend import settings


def send_verification_email(user, request):
    # Retrieve the current domain dynamically
    current_domain = request.scheme + '://' + request.get_host()
    
    # Retrieve the token from the EmailVerification object
    try:
        token = user.verification.token
    except EmailVerification.DoesNotExist:
        raise ValueError("Email verification token not found for the user")

    # Generate the verification link using reverse and appending the token
    verification_link = reverse('verify_email', kwargs={'token': str(token)})
    verification_url = current_domain + verification_link

    # Send verification email with link
    EmailMessage(
        'Verify your account',
        f'Click the following link to verify your account: {verification_url} ',
        settings.EMAIL_HOST_USER,
        [user.email],
    ).send(fail_silently=False)
    
    
