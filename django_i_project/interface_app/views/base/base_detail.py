import json

from django.forms import model_to_dict
from django.views.generic import View
from interface_app.forms.service_form import ServiceForm

from interface_app.libs.response import response_success, response_failed, ErrorCode
from interface_app.models.service import Service


class BaseDetailView(View):

    model = Service
    form = ServiceForm
    code = ErrorCode.common

    def get(self, request, base_id, *args, **kwargs):
        """ 这个是获取单个数据 """
        service = self.model.objects.filter(pk=base_id).first()
        if not service:
            return response_failed(code=self.code, message='数据不存在')
        return response_success(model_to_dict(service))

    def put(self, request, base_id, *args, **kwargs):
        """ 这个是全量修改数据 """
        body = request.body
        data = json.loads(body, encoding='utf-8')
        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        service = self.model.objects.filter(pk=base_id).first()
        if not service:
            return response_failed(code=self.code, message='数据不存在')

        self.model.objects.filter(pk=base_id).update(**form.cleaned_data)
        service = self.model.objects.filter(pk=base_id).first()
        if not service:
            return response_failed(code=self.code, message='修改数据失败')
        return response_success(model_to_dict(service))

    def patch(self, request, service_id, *args, **kwargs):
        """ 这个是部分修改数据 """
        return self.put(request, service_id, *args, **kwargs)

    def delete(self, request, base_id, *args, **kwargs):
        """ 这个是删除数据 """
        service = self.model.objects.filter(pk=base_id)
        if not service:
            return response_failed(code=self.code, message='数据不存在')
        service.delete()
        return response_success()
