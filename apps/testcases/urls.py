# -*- coding: utf-8 -*-

from django.urls import path
from rest_framework import routers

# from .views import TestcasesViewSet, TestcasesRunView
from .views import TestcasesViewSet

router = routers.DefaultRouter()
router.register(r'testcases', TestcasesViewSet)

urlpatterns = [

]
urlpatterns += router.urls
