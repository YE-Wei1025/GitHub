from django.db import models

# Create your models here.


class UserInfo(models.Model):

    name = models.CharField('用户名', max_length=50, null=False)
    password = models.CharField('密码', max_length=200, null=False)
    email = models.EmailField('邮箱', max_length=50, null=False)
    phone = models.CharField('手机号', max_length=20, null=True)
    time = models.DateTimeField('注册时间', auto_now=True)
    isban = models.BooleanField('禁用', default=False)
    isdelete = models.BooleanField('删除', default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'UserInfo'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(models.Model):
    name = models.CharField('用户', max_length=100, null=False)
    ads = models.CharField('地址', max_length=200, null=False)
    phone = models.CharField('手机号', max_length=20, null=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Address'
        verbose_name = '地址信息'
        verbose_name_plural = verbose_name
