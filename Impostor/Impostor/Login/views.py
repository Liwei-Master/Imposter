from django.shortcuts import render
from django.shortcuts import HttpResponse
import json

# Create your views here.
# test command : python manage.py runserver 127.0.0.1:8000
# 根据API 返回 内容
username_list = ("Tony", "Wang")
keywords_list = ("123")
email_list = ("296390818@qq.com")
code_list = ("321")

def Login (request):

    return render(request, "Login.html", {'error_info': "是第一次的话，请申请账号"})

def submit (request):
    username = request.POST.get('email')
    keywords = request.POST.get('keywords')

    if request.method == 'POST' and username in username_list: # 接数据库

        print(username, keywords) # test

        if keywords in keywords_list: # 接数据库

            return render(request, "Login.html", {'error_info': "登陆成功"})
        else:
            return render(request, "Login.html", {'error_info': "该用户名或密码不正确，请重新输入"})

    else:
        return render(request, "Login.html", {'error_info': "是第一次的话，请申请账号"})

def sign_up(request):

    if request.method == 'POST':
        email = request.POST.get('set_email')
        keywords = request.POST.get('set_password')
        username = request.POST.get('set_name')
        print(email, keywords, username)
        return render(request, "Login.html", {'error_info': "听说你是第一次登录哦"})

def find_password(request):
    if request.method == "POST":
        email = str(request.POST.get('send_email'))
        if email.find("@", 2) < 0:
            return render(request, "Login.html", {'error_info': "邮箱输入错误"})

        print(email)
        return render(request, "Login.html",)



#def sign_up (request):
 #   json_data = request.POST.get('data')
  #  content = json.loads(json_data)

   # email = content[0].new_email
    #keyword = content[1].keywords
    #name = content[2].name

    #print(email, keyword, name)


    #return render(request, "Login.html", {'error_info': "听说你是第一次登录哦"})

