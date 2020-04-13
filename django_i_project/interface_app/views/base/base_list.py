import json

from django.forms import model_to_dict

from django.views.generic import View

from interface_app.forms.service_form import ServiceForm
from interface_app.libs.response import response_success, response_failed, ErrorCode
from interface_app.models.service import Service

class BaseListView(View):

    model = Service
    form = ServiceForm
    code = ErrorCode.common

    def get(self, request, *args, **kwargs):
        """ 这个是获取所有数据 """
        service = self.model.objects.all()
        ret = []
        for s in service:
            t = model_to_dict(s)
            ret.append(t)
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """ 这个是创建数据 """
        body = request.body
        data = json.loads(body, encoding='utf-8')
        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        # name = form.cleaned_data['name']
        # description = form.cleaned_data['description']
        # service = self.module.objects.create(name=name, description=description)
        service = self.model.objects.create(**form.cleaned_data)
        if service:
            return response_success(model_to_dict(service))
        else:
            return response_failed(code=self.code, message='创建服务失败')
