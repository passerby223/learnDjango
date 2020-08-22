# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/9/23 20:55 
  @Auth : 可优
  @File : urls.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from django.urls import path, include
from rest_framework import routers

from projects import views

# 1. 创建SimpleRouter路由对象
# router = routers.SimpleRouter()
router = routers.DefaultRouter()
# 2. 注册路由
# 第一个参数prefix为路由前缀, 一般添加为应用名即可
# 第二个参数viewset为视图集, 不要加as_view()
router.register(r'projects', views.ProjectsViewSet)

urlpatterns = [
    # path('', index),
    # path('index/', index),
    # 如果为类视图, path第二个参数为类视图名.as_view()
    # path('', views.IndexView.as_view()),
    # path('<int:pk>/', views.IndexView.as_view())
    # int为路径参数类型转化器
    # :左边为转换器, 右边为参数别名
    # path('projects/', views.ProjectsList.as_view()),
    # path('projects/<int:pk>/', views.ProjectsDetail.as_view()),
    # path('projects/', views.ProjectsViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create',
    # }), name='proejcts-list'),
    # path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    #
    # path('projects/names/', views.ProjectsViewSet.as_view({
    #     'get': 'names',
    # }), name='proejcts-names'),
    #
    # path('projects/<int:pk>/interfaces/', views.ProjectsViewSet.as_view({
    #     'get': 'interfaces',
    # })),
    # 3. 将自动生成的路由, 添加到urlpatterns中
    # path('', include(router.urls)),
]

urlpatterns += router.urls
