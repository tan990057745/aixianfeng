import hashlib
import os
import uuid

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

from myapp.models import Wheel, Nav, Mustbuy, Shop, MainShow, Goods, Foodtypes, User


def index(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()

    #商品展示部分
    shopList = Shop.objects.all()
    shophead = shopList[0]
    shoptab = shopList[1:3]
    shopclass = shopList[3:7]
    shopcommend = shopList[7:11]

    mainshows = MainShow.objects.all()

    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,

        'shophead': shophead,
        'shoptab': shoptab,
        'shopclass': shopclass,
        'shopcommend': shopcommend,
        'mainshows': mainshows
    }
    return render(request,'index/index.html',context=data)


def market(request,categoryid, childid, sortid):
    foodtypes = Foodtypes.objects.all()

    # 分类 点击 下标  >>>>  分类ID
    typeIndex = int(request.COOKIES.get('typeIndex', 0))

    # 根据分类下标 获取 对应 分类ID
    categoryid = foodtypes[typeIndex].typeid

    # 子类信息
    childtypenames = foodtypes.get(typeid=categoryid).childtypenames
    # 将每个子类拆分出来

    childTypleList = []
    for item in childtypenames.split('#'):
        arr = item.split(':')
        dir = {
            'childname': arr[0],  # 子类名称
            'childid': arr[1]  # 子类ID
        }
        childTypleList.append(dir)

    print(childTypleList)
    #
    # # 商品信息 - 根据分类id获取对应数据
    # goodsList = Goods.objects.all()[0:5]
    if childid == '0':  # 全部分类
        goodsList = Goods.objects.filter(categoryid=categoryid)
    else:  # 下拉子类
        goodsList = Goods.objects.filter(categoryid=categoryid, childcid=childid)

    # 排序
    if sortid == '1':  # 销量排序
        goodsList = goodsList.order_by('-productnum')
    elif sortid == '2':  # 价格最低
        goodsList = goodsList.order_by('price')
    elif sortid == '3':  # 价格最高
        goodsList = goodsList.order_by(('-price'))

    data = {
        'foodtypes': foodtypes,  # 分类信息
        'goodsList': goodsList,  # 商品信息
        'childTypleList': childTypleList,  # 子类信息
        'categoryid': categoryid,  # 分类ID
        'childid': childid,  # 子类ID
    }

    return render(request,'market/market.html',context=data)


def cart(request):
    return render(request,'cart/cart.html')

###我的页面
def mine(request):
    # 获取用户信息
    token = request.session.get('token')

    responseData = {}

    if token:  # 登录
        user = User.objects.get(token=token)
        responseData['name'] = user.name
        responseData['rank'] = user.rank
        responseData['img'] = '/static/uploads/' + user.img
        responseData['isLogin'] = 1
    else:  # 未登录
        responseData['name'] = '未登录'
        responseData['img'] = '/static/uploads/axf.png'

    return render(request, 'mine/mine.html', context=responseData)
    


####登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')

        try:
            user = User.objects.get(account=account)
            if user.password == genarate_password(password):  # 登录成功

                # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('myapp:mine')
            else:  # 登录失败
                return render(request, 'login/login.html', context={'passwdErr': '密码错误!'})
        except:
            return render(request, 'login/login.html', context={'acountErr': '账号不存在!'})



###密码加密
def genarate_password(param):
    sha = hashlib.sha256()
    sha.update(param.encode('utf-8'))
    return sha.hexdigest()

####注册
def registe(request):
    if request.method == 'GET':
        return render(request,'registe/registe.html')
    elif request.method == 'POST':

        user = User()
        user.account = request.POST.get('account')
        user.password = genarate_password(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.phone = request.POST.get('phone')
        user.addr = request.POST.get('addr')

        # 头像
        imgName = user.account + '.png'
        imagePath = os.path.join(settings.MEDIA_ROOT, imgName)
        file = request.FILES.get('icon')
        with open(imagePath, 'wb') as fp:
            for data in file.chunks():
                fp.write(data)
        user.img = imgName

        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
        user.save()

        # 状态保持
        request.session['token'] = user.token

        # 重定向
        return redirect('myapp:mine')


##验证账户
def checkaccount(request):
    account = request.GET.get('account')

    responseData = {
        'msg': '账号可用',
        'status': 1 # 1标识可用，-1标识不可用
    }
    try:
        user = User.objects.get(account=account)
        responseData['msg'] = '账号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)

####登出
def logout(request):
    request.session.flush()
    return redirect('myapp:mine')