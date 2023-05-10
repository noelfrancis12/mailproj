from .import views
from django.urls import path,include
urlpatterns = [
    path('',views.add,name='add'),
    path('sndmail',views.sndmail,name='sndmail'),
]