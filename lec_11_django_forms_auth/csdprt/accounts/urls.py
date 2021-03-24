from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import *
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('logout/', LogoutView.as_view(next_page='persons:index'), name='logout'),
    path('register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('password_change/',
         AccountsPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/',
         PasswordResetView.as_view(template_name='accounts/password_reset.html',
                                   subject_template_name='accounts/reset_subject.txt',
                                   email_template_name='accounts/reset_email.txt',
                                   success_url=reverse_lazy('accounts:password_reset_done')),
         name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='accounts/email_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/confirm_password.html',
         success_url=reverse_lazy('accounts:password_reset_camplete')),
         name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_confirmed.html'),
         name='password_reset_camplete'),
]