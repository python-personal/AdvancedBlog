from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signup/', views.signupview, name='signup'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('login/',auth_view.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    # password reset
    path('reset/',auth_view.PasswordResetView.as_view(template_name='accounts/password_reset.html',email_template_name='accounts/password_reset_email.html',subject_template_name='accounts/password_reset_subjects.txt'),name='password_reset'),
    path('reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_compltete.html'),name='password_reset_complete'),
    # change password
    path('changepassword/',auth_view.PasswordChangeView.as_view(template_name='accounts/password_change.html'),name='password_change'),
    path('changepassword/done',auth_view.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),
    path('myaccount/',views.UserUpdateview.as_view(),name='my_account')

]
