from django.urls import path

from . import views
import re
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>', views.detail, name='detail'),
    # path('<int:todo_id>/update', views.update, name='update'),
    # path('/create',views.create, name='create'),
    # path('/<int:todo_id>/delete', views.delete, name='delete'),
    url(r'^search/$', views.search, name = 'search'),
]