from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from django.urls import reverse
from django.utils.six import BytesIO
from Book.models import BookInfo
import random
# Create your views here.


def post_test(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    print(name, pwd, gender, hobby)
    return render(request, 'post_test.html', context=locals())


# 输入验证码
def inputyzm(request):
    return render(request, 'inputyzm.html')


def recvyzm(request):
    # 接受客户端传递的验证码
    client_code = request.POST.get('yzm')
    # 服务器生成的验证码
    server_code = request.session['verifycode']
    # 对比
    if client_code == server_code:
      return HttpResponse('验证码OK！')
    else:
      return HttpResponse('验证码错误')


# 生成验证码
def verifyCode(request):
    # 引入随机函数模块
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
      20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
      xy = (random.randrange(0, width), random.randrange(0, height))
      fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
      draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
      rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def get(request):
    return render(request, 'get.html')


def get1(request):
    dict = request.GET
    a = dict.get('a')
    b = dict.get('b')
    c = dict.get('c')
    context = {'a': a, 'b': b, 'c': c}
    return render(request, 'get1.html', context)


def get2(request):
    dict = request.GET
    a = dict.getlist('a')
    b = dict.get('b')
    context = {'a': a, 'b': b}
    return render(request, 'get2.html', context)


def booklist(request):

    bookinfos = BookInfo.objects.all()
    context = {'booklist': bookinfos}

    return render(request, 'booklist.html', context)


def login(request):
    name = request.POST.get('name')
    print(name)
    response = redirect(reverse('Book:mine'))
    response.set_cookie('name', name)
    return response


def mine(request):
    name = request.COOKIES.get('name')
    return render(request, 'mine.html', context=locals())


def logout(request):
    response = redirect(reverse('Book:mine'))
    response.delete_cookie('name')
    return response


def index(request):

    return render(request, 'login.html')