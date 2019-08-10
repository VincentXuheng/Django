# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Dept(models.Model):
##"""部门类"""
    no = models.IntegerField(primary_key=True, db_column='dno', verbose_name=u'部门编号')
    name = models.CharField(max_length=20, db_column='dname', verbose_name=u'部门名称')
    location = models.CharField(max_length=10, db_column='dloc', verbose_name=u'部门所在地')

    class Meta:
           db_table = 'tb_dept'

    def __str__(self):
        return self.name
   

class Emp(models.Model):
##"""员工类"""

    no = models.IntegerField(primary_key=True, db_column='eno', verbose_name=u'员工编号')
    name = models.CharField(max_length=20, db_column='ename', verbose_name=u'员工姓名')
    job = models.CharField(max_length=10, verbose_name=u'职位')
# 多对一外键关联(自参照)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'主管')
    sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=u'月薪')
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name=u'补贴')
# 多对一外键关联(参照部门模型)
    dept = models.ForeignKey(Dept, db_column='dno', on_delete=models.PROTECT, verbose_name=u'所在部门')
   
    class Meta:
           db_table = 'tb_emp'

    def __str__(self):
        return self.name
