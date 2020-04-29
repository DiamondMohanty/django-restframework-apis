from django.urls import path
from .views import todo, todo_detail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('todo/', todo),
    path('todo/detail/<int:id>/', todo_detail),
]

urlpatterns= format_suffix_patterns(urlpatterns=urlpatterns)