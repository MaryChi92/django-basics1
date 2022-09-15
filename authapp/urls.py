from django.urls import path, re_path

from authapp.views import login, logout, register, edit, verify

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    # path('verify/', verify, name='verify'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', verify, name='verify'),
]
