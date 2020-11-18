from django.urls import include, path
from . import views

urlpatterns = [
    path ('coord/', views.CoordListCreate.as_view()),
    path ('coord/<int:pk>', views.CoordRetrieveUpdateDestroy.as_view()),
]
