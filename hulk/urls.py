from hulk.views import *
from django.urls import path
app_name='something'
#urls
urlpatterns=[
    path('ntr/',ntr,name='ntr'),
]