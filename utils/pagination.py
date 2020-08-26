# -*- coding: utf-8 -*-

from rest_framework import pagination


class PageNumberPaginationManual(pagination.PageNumberPagination):
    # 设置每页最大数据条目为50
    max_page_size = 50
    # 覆盖page_size字段为size
    page_size_query_param = 'size'
    # 配置page字段在接口文档中的描述信息
    page_query_description = '第几页'
    # 配置size字段在接口文档中的描述信息
    page_size_query_description = '每页几条'

    def get_paginated_response(self, data):
        '''
        重写父类的get_paginated_response()方法
        在分页后的数据构成的响应体中添加total_pages(总共分了多少页)和current_page_num(当前所在第几页)字段
        '''
        # 调用父类中的get_paginated_response()方法获得dict类型返回值，在进行定制
        response = super().get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        response.data['current_page_num'] = self.page.number
        return response
