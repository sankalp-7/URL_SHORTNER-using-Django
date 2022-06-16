from django.urls import path
from . import views

app_name='url'
urlpatterns=[ 
    path('',views.home,name='home'),
    path("<str:short_url>", views.urlRedirect, name="redirect")
]