from django.urls import path
from calculator import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('submitquery',views.submitquery,name='submitquery')
]