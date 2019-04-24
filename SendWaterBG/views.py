from django.shortcuts import render,HttpResponse
from . import models
import json
from django.http import JsonResponse
from django.core import serializers
from twilio.rest import Client


def creatUser(request):
    try:
        dto = models.User()
        dto.name = request.GET['name']
        dto.passwd = request.GET['passed']

        if models.User.objects.filter(name=dto.name).exists():
            print(models.User.objects.filter(name=dto.name).exists())
            return JsonResponse({'msg': "failed"})

        else:
            print(models.User.objects.filter(name=dto.name).exists())
            dto.save()
            return JsonResponse({'msg': 'successed'})
    except IOError:
        return HttpResponse("操作失败")


def commitTable(request):
    try:
        print("1")
        dto = models.CommitTable()
        dto.address = request.GET['address']
        dto.amount = request.GET['amount']
        dto.time = request.GET['time']
        dto.name = request.GET['name']
        dto.kind = request.GET['kind']
        dto.userPhone = request.GET['userphone']
        dto.otherMsg = request.GET['othermsg']
        dto.save()

        shopnumber = "13287498539"

        content = dto.name+'在'+dto.time+'时候'+'需要'+dto.amount+'桶'+dto.kind+\
                  ' 备注：'+dto.otherMsg+'     '+'我的地址：  '+dto.address+\
                  '我的电话： '+dto.userPhone

        # Download the helper library from https://www.twilio.com/docs/python/install
    
    
        # Your Account Sid and Auth Token from twilio.com/console
        # DANGER! This is insecure. See http://twil.io/secure
        account_sid = 'AC8b0152de33aac3b4d735a0c864789cc4'
        auth_token = 'd8adba45f2bbaa94009a1418dc449c45'
        client = Client(account_sid, auth_token)
    
        message = client.messages \
            .create(
            body=content,
            from_='+12056602109',
            to='+86'+shopnumber,
        )
        message.sid
        dto.save()
        return HttpResponse('提交成功')
    except IOError:
        return HttpResponse("操作失败")


def getAllShop(request):
    try:
        data = {}
        book = models.OfferMan.objects.all()
        data['list'] = json.loads(serializers.serialize("json", book))
        return JsonResponse(data)
    except IOError:
        return HttpResponse("操作失败")


def getMyHistory(request):
    try:
        data = {}
        book = models.CommitTable.objects.filter(name=request.GET['name'])
        data['list'] = json.loads(serializers.serialize("json", book))
        return JsonResponse(data)
    except IOError:
        return HttpResponse("操作失败")


def login(request):
    try:
        dto = models.User.objects.filter(name=request.GET['name'])
        passed = request.GET['passed']
        print(passed)
        print(dto[0].passwd)
        if passed == dto[0].passwd:
            return JsonResponse({'isCommit': True})
        else:
            return JsonResponse({'isCommit': False})
    except IOError:
        return HttpResponse("操作失败")


def getOneShop(request):
    try:
        data={}
        dto = models.OfferMan.objects.filter(name=request.GET['name'])
        data['list'] = json.loads(serializers.serialize("json", dto))
        return JsonResponse(data)
    except IOError:
        return HttpResponse("操作失败")


def addOfferMan(request):
    try:
        if models.OfferMan.objects.filter(name=request.GET['name']).exists():

            dto = models.OfferMan.objects.get(name=request.GET['name'])
            dto.kind = request.GET['kind']
            dto.name = request.GET['name']
            dto.count = request.GET['count']
            dto.number = request.GET['number']
            dto.othermsg = request.GET['othermsg']
            dto.save()

            return HttpResponse("修改成功")
        else:
            dto = models.OfferMan()
            dto.name = request.GET['name']
            dto.number = request.GET['number']
            dto.otherMsg = request.GET['othermsg']
            dto.save()
            return HttpResponse('添加成功')
    except IOError:
        return HttpResponse("操作失败")


def addAdmin(request):
    try:
        dto = models.admin()
        dto.passed = request.GET['passed']
        dto.name = request.GET['name']
        dto.boss = request.GET['boss']
        return HttpResponse('添加成功')
    except IOError:
        return HttpResponse("操作失败")


def adminLogin(request):
    try:
        dto = models.admin.objects.filter(name=request.GET['name'])
        passed = request.GET['passed']
        if passed == dto[0].passwd:
            return JsonResponse({'isCommit': True})
        else:
            return JsonResponse({'isCommit': False})
    except IOError:
        return HttpResponse("操作失败")


def getMyCustomers(request):
    try:
        dto = models.CommitTable.objects.filter(name=request.GET['boss'])
        data = {}
        data['list'] = json.loads(serializers.serialize("json", dto))
        return JsonResponse(data)
    except IOError:
        return HttpResponse("操作失败")

