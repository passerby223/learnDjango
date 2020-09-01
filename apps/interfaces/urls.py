# -*- coding: utf-8 -*-

from rest_framework import routers

from .views import InterfacesViewSet

router = routers.DefaultRouter()
router.register(r'interfaces', InterfacesViewSet)

urlpatterns = [

]
urlpatterns += router.urls
