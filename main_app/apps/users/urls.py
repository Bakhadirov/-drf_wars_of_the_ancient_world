from django.urls import path
from rest_framework.authtoken import views
from main_app.apps.users.api.views.user import UserRegistrationView, UserProfileView

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('registration/', UserRegistrationView.as_view()),
    path('profile/', UserProfileView.as_view()),
]
