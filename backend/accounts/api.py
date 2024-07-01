from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import serializers  # type: ignore
from y_backend import settings
from .utils import send_verification_email
from .models import EmailVerification, User
from rest_framework.response import Response  # type: ignore
from .serializers import SignupSerializer, UserInfoSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes  # type: ignore
from rest_framework import status  # type: ignore
from rest_framework.permissions import AllowAny  # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from django.contrib.auth import login


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):

    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        response_data = serializer.data

        send_verification_email(user, request)

        return Response(response_data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def check_email_exists(request):
    email = request.data.get("email")
    email_exists = User.objects.filter(email=email).exists()

    return JsonResponse({"exists": email_exists})


@api_view(["GET"])
@permission_classes([AllowAny])
def verify_email(request, token):
    try:
        verification = EmailVerification.objects.get(token=token)
    except EmailVerification.DoesNotExist:
        return Response({"error": "Invalid link"}, status=status.HTTP_400_BAD_REQUEST)

    if verification.is_token_expired():
        return Response(
            {"error": "Verification link has expired"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Mark the user as verified and activate the account
    user = verification.user
    user.is_active = True
    user.save()

    # Delete the verification entry
    verification.delete()

    
    # Redirect to a new URL with JWT token as a query parameter
    redirect_url = settings.FRONTEND_URL + "VerificationSuccessful" 

    return redirect(redirect_url)


@api_view(["POST"])
@permission_classes([])
def check_username_exists(request):
    username = request.data.get("username")
    email_exists = User.objects.filter(username=username).exists()

    return JsonResponse({"exists": email_exists})


@api_view(['GET'])
def get_user_info(request):
    # Retrieve authenticated user instance
        user = request.user

        # Update user fields directly from database instance
        user_data = {
            'username': user.username,
            'full_name': user.full_name,
            'email': user.email,
            'date_of_birth': user.date_of_birth,
        }

        # Serialize and validate the updated data
        serializer = UserInfoSerializer(instance=user, data=user_data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        