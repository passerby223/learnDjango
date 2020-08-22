# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/6/23 23:56 
  @Auth : 可优
  @File : urls.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
from rest_framework import routers

from .views import TestsuitsViewSet

router = routers.DefaultRouter()
router.register(r'testsuits', TestsuitsViewSet)

urlpatterns = [

]
urlpatterns += router.urls
