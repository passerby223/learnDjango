from django.urls import path
from rest_framework import routers

from .views import ReportsViewSet

router = routers.DefaultRouter()
router.register(r'reports', ReportsViewSet)

urlpatterns = [

]
urlpatterns += router.urls
