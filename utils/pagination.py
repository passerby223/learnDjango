# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/10/21 21:38 
  @Auth : 可优
  @File : pagination.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from django.conf import settings
from rest_framework import pagination


class PageNumberPaginationManual(pagination.PageNumberPagination):
    max_page_size = 50
    page_size_query_param = 'size'
    page_query_description = '第几页'
    page_size_query_description = '每页几条'

    def get_paginated_response(self, data):
        response = super(PageNumberPaginationManual, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        response.data['current_page_num'] = self.page.number
        return response
