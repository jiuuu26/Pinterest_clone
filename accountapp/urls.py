import helloworld as helloworld
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"


urlpatterns = [
     #함수형 view
     path('hello_world/', hello_world, name='hello_world'),
     #class based view
     path('create/', AccountCreateView.as_view(), name='create')

]