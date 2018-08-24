from django.db import models

# Create your models here.


class GoodsType(models.Model):
    title = models.CharField('分类名称', max_length=20, null=False)
    desc = models.CharField('描述', max_length=200, default='商品描述')
    flag = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='static/image/good_type', default='normal.png')
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'GoodsType'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    title = models.CharField('名称', max_length=50, null=False)
    price = models.DecimalField('商品价格', max_digits=8, decimal_places=2)
    desc = models.CharField('描述', max_length=1000)
    picture = models.ImageField('商品照片', upload_to='static/images/goods', default='normal.png')
    isDelete = models.BooleanField(default=False)
    type = models.ForeignKey(GoodsType)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/detail/?good={}/'.format(self.id)

    class Meta:
        db_table = 'Goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
