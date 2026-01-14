from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    # return HttpResponse("Login Page")
    # return redirect("https://www.baidu.com")
    return render(request, 'login.html')

def user_list(request):
    # 1. 数据库读取数据
    data = ["tom", "sam", "alice"]

    # 2. 打开文件并读内容
    # 3. 模板的渲染 -> 文本替换
    return render(request, 'user_list.html',
                  {"users": data})

def phone_list(request):
    # 1. 获取数据
    querySet = [
        {"id": 1, "phone": "18888887777", "city": "上海"},
        {"id": 2, "phone": "18844447777", "city": "北京"},
        {"id": 3, "phone": "18855557777", "city": "南京"},
    ]
    # 2. 通过页面渲染返回用户 (表格)
    return render(request, 'phone_list.html',
                  {"data": querySet})