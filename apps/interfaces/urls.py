# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/11/8 20:38 
  @Auth : 可优
  @File : urls.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework import routers

from .views import InterfacesViewSet

router = routers.DefaultRouter()
router.register(r'interfaces', InterfacesViewSet)

urlpatterns = [

]
urlpatterns += router.urls
