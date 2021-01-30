from django.urls import include, path
from . import views

urlpatterns = [
    path ('coord/list/', views.CoordList.as_view()),
    path ('coord/', views.CoordCreate.as_view()),
]
