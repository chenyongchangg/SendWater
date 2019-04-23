# SendWater Version2.0
--------

> 路由表：		` path('admin', admin.site.urls),`

-------

> 创建用户   	 `path('creatuser', views.creatUser),`

```c
dto.name = request.GET['name']
dto.passwd = request.GET['passed']
```
------

 > 提交送水信息	 path('committable', views.commitTable),

```c
dto = models.CommitTable()
dto.address = request.GET['address']
dto.amount = request.GET['amount']
dto.time = request.GET['time']
dto.name = request.GET['name']
dto.kind = request.GET['kind']
dto.userPhone = request.GET['userphone']
dto.otherMsg = request.GET['othermsg']
```

---------

> 获得所有商铺 	 path('getallshop', views.getAllShop),

```c
 无参数
```
-----

 > 获得一个商铺  	 path('getoneshop', views.getOneShop),

```c
 dto = models.OfferMan.objects.filter(name=request.GET['name'])
```

 >  获得我的历史 	 path('gethistory', views.getMyHistory),

---------

 > 用户登录 	 	 path('login', views.login),


```c
dto = models.User.objects.filter(name=request.GET['name'])
passed = request.GET['passed']
```
------

 > 添加送水员 	 path('addofferman', views.addOfferMan),

```c
dto.kind = request.GET['kind']
dto.name = request.GET['name']
dto.count = request.GET['count']
dto.number = request.GET['number']
dto.othermsg = request.GET['othermsg']
```
-------

> 添加管理员      path('addadmin', views.addAdmin),//root权限 不在页面使用

```c
dto.passed = request.GET['passed']
dto.name = request.GET['name']
```
---------

> 管理员登录 	 path('adminlogin', views.adminLogin),//有一个默认 admin@passed

``` c
dto=models.admin.objects.filter(name=request.GET['name'])
passed = request.GET['passed']
```
