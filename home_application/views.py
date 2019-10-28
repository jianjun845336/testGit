# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

import json
import requests
from requests import request
from common.mymako import render_mako_context
from common.mymako import render_mako_context, render_json
from home_application.models import *
from conf.default import *
from django.db import transaction
from mako.template import Template
from django.views.decorators.csrf import csrf_exempt


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def query(request):
    """
    联系我们
    """
    """
    """
    return render_mako_context(request, '/home_application/query.html')

def gethosts(request):
    """
    联系我们
    """
    print request.POST.dict()
    return render_mako_context(request, '/home_application/demo.html')

def search(request):
    """
    联系我们
    """
    print("request")
    req = request.POST.dict()
#    b = check(name='1212', age=32, address='cesi', teacher='zhangsan')
#    c = check.objects.create(name = '1212',age = '32',address='cesi',teacher='zhangsan')
    d = check.objects.get(id='1')
#    c.save()
#    print(d.name)
    d.age = 66
#    d.save()
    kwarks={
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": "admin"
    }
    pre = kwarks.get('bk_app_code')
    url1 = 'http://paas.bk.cloud.tencent.com/esb/api_docs/system/CC/search_host/'
    url = 'http://paas.bk.cloud.tencent.com/esb/api_docs/system/CC/search_business/'
    print(kwarks)
    res = requests.post(url,json=kwarks)
#    print(json.loads(res.content))
    mytemplate = Template("hello world!")
    print(mytemplate.render())
    print(res.content)
#    ids = [1, 2, 3]
#    ids = ",".join(ids)
    # 批量更新
#    with transaction.atomic():
     #   check.objects.extra(where=["id IN (" + ids + ")"]).update(is_active=True)

 #   d.objects.filter(id=1).update(name = '654321')
    return render_json({'result':'true','flag':'1'})

@csrf_exempt
def select_server(request):
    # client = get_client_by_request(request)
    # result = client.cc.search_host()
    user = "admin"
    client = get_client_by_user(user)
    data = request.GET
    param = {"bk_biz_id": data.get('bk_biz_id')}
    result = client.cc.search_host(param)
    info = result["data"].get("info")
    server_list = []
    for i in info:
        server_list.append(
            {
                "bk_host_innerip": i["host"].get("bk_host_innerip"),
                "bk_host_name": i["host"].get("bk_host_name"),
                "bk_os_name": i["host"].get("bk_os_name")}
        )
    # print server_list
    return render_json(server_list)

