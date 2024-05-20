from django.urls import path, re_path
from .views import index

from . import views


app_name = "frontpage"
urlpatterns = [
    path("", views.index, name="frontpage"),
    re_path(r'^.*$', index, name='index'),

]
