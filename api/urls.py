from django.urls import include, path
from . import views
# from rest_framework import routers
#
# router = routers.SimpleRouter()
# router.register('coord', views.CoordViewSet)
# urlpatterns = router.urls
urlpatterns = [
    path ('coord/', views.CoordListCreate.as_view()),
    path ('coord/<int:pk>', views.CoordRetrieveUpdateDestroy.as_view()),
]
