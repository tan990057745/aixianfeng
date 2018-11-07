from django.db import models

# Create your models here.

class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'

class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'

# 主页商品信息
class Shop(Base):
    class Meta:
        db_table='axf_shop'

# 主页商品主体内容
# (trackid,name,img,categoryid,brandname,
# img1,childcid1,productid1,longname1,price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3)
# values("21782","优选水果","http://img01.bqstatic.com//upload/activity/2017031018205492.jpg@90Q.jpg","103532","爱鲜蜂",

class MainShow(models.Model):
    trackid = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=8)
    brandname = models.CharField(max_length=50)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=8)
    productid1 = models.CharField(max_length=8)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=8)
    productid2 = models.CharField(max_length=8)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=8)
    productid3 = models.CharField(max_length=8)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'

class Goods(models.Model):
    productid = models.CharField(max_length=10)  # 商品ID
    productimg = models.CharField(max_length=100)  # 商品图片
    productname = models.CharField(max_length=100)  # 商品名称
    productlongname = models.CharField(max_length=100)  # 商品全称

    isxf = models.BooleanField(default=False)  # 精选
    pmdesc = models.BooleanField(default=False)  # 买一送一
    specifics = models.CharField(max_length=100)  # 规格
    price = models.DecimalField(max_digits=7, decimal_places=2)  # 价格

    marketprice = models.DecimalField(max_digits=7, decimal_places=2)  # 商场价格
    categoryid = models.IntegerField()  # 分类ID
    childcid = models.IntegerField()  # 子类ID
    childcidname = models.CharField(max_length=100)  # 分类名称

    dealerid = models.CharField(max_length=10)  # 详情ID
    storenums = models.IntegerField()  # 库存
    productnum = models.IntegerField()  # 销量

    class Meta:
        db_table = 'axf_goods'

#商品分类
class Foodtypes(models.Model):
    typeid = models.CharField(max_length=8) # 分类ID
    typename = models.CharField(max_length=100) # 分类名称
    childtypenames = models.CharField(max_length=256)   # 子类名称
    typesort = models.IntegerField()    # 显示先后顺序
    class Meta:
        db_table = 'axf_foodtypes'

#用户信息
class User(models.Model):
    # 账号
    account = models.CharField(max_length=80, unique=True)
    # 密码
    password = models.CharField(max_length=256)
    # 名字
    name = models.CharField(max_length=100)
    # 手机号
    phone = models.CharField(max_length=20, unique=True)
    # 地址
    addr = models.CharField(max_length=256)
    # 头像
    img = models.CharField(max_length=100)
    # 等级
    rank = models.IntegerField(default=1)
    # token
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'axf_user'


class Cart(models.Model):
    user = models.ForeignKey(User)
    # 商品
    goods = models.ForeignKey(Goods)
    # 商品数量(选择)
    number = models.IntegerField()
    # 是否选中
    isselect = models.BooleanField(default=True)
    class Meta:
        db_table = 'axf_cart'