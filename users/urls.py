from django.conf.urls import url
from . import views

#设置命名空间
app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
]