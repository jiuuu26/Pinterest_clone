import helloworld as helloworld
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = "accountapp"


urlpatterns = [
     #함수형 view
     path('hello_world/', hello_world, name='hello_world'),

     path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),

     #class based view
     path('create/', AccountCreateView.as_view(), name='create'),
     path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

]