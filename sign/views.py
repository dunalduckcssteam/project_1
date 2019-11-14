from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .forms import LoginForm
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from django.template import RequestContext

# from .models import Candidate  # models에 정의된 Candidate를 불러온다

def login(request):
    context = {}
    return render(request, 'sign/login.html', context)

@csrf_exempt
def test(id):
    print(id)
    # context = {}
    data = {
        'duplicate': True # 로그인 처리
    }
    return JsonResponse(data)

@csrf_exempt
def test2(request):
    print(request)
    # context = {}
    data = {
        'duplicate': True #중복된 아이디 처리
    }
    return JsonResponse(data)

