from django.db import models

from utils.base_models import BaseModel


class Projects(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('项目名称', max_length=200, unique=True, help_text='项目名称')
    leader = models.CharField('负责人', max_length=50, help_text='项目负责人')
    tester = models.CharField('测试人员', max_length=50, help_text='项目测试人员')
    programmer = models.CharField('开发人员', max_length=50, help_text='开发人员')
    publish_app = models.CharField('发布应用', max_length=100, help_text='发布应用')
    desc = models.CharField('简要描述', max_length=200, null=True, blank=True, default='', help_text='简要描述')

    class Meta:
        # 修改表名
        db_table = 'tb_projects'
        # 设置在admin站点中的显示表名，在英文表名下表现为单数形式
        verbose_name = '项目信息'
        # 在英文表名下表现为复数形式，会自动在英文表名后边加一个`s`
        verbose_name_plural = verbose_name
        # 添加view视图中进行查询操作时默认排序字段，如果不指定，在进行查询操作时会抛出warning
        ordering = ['id']

    def __str__(self):
        '''
        # 重写__str__()方法，使admin后台中展示model中定义的name
        '''
        return self.name
