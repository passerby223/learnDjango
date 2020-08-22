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
from rest_framework import routers

from .views import EnvsViewSet

router = routers.DefaultRouter()
router.register(r'envs', EnvsViewSet)

urlpatterns = [

]
urlpatterns += router.urls
