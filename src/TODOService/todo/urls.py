from django.urls import path
from .views import TODOList, TODODetails
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('todo/', TODOList.as_view()),
    path('todo/detail/<int:id>/', TODODetails.as_view()),
]

urlpatterns= format_suffix_patterns(urlpatterns=urlpatterns)