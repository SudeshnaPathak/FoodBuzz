from .views import SignupPage, LoginPage, logoutPage, change_address, conclusion
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('signup/', SignupPage, name='signup'),
    path('login/', LoginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('address/', change_address, name='address'),
    path('conclude/', conclusion, name='conclude')


    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]

# urlpatterns = [
#    path('signup/', SignupPage, name='signup'),
#    path('login/', LoginPage, name='login')
# ]