# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/6/30 9:20 
  @Auth : 可优
  @File : urls.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
from django.urls import path
from rest_framework import routers

# from .views import TestcasesViewSet, TestcasesRunView
from .views import TestcasesViewSet

router = routers.DefaultRouter()
router.register(r'testcases', TestcasesViewSet)

urlpatterns = [

]
urlpatterns += router.urls
