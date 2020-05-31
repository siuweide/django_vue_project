import json

from django.forms import model_to_dict

from interface_app.forms.Interface_form import InterfaceForm

from interface_app.libs.response import ErrorCode, response_failed, response_success
from interface_app.models.interface import Interface
from interface_app.views.base.base_detail import BaseDetailView


class InterfaceDetailView(BaseDetailView):

    module = Interface
    form = InterfaceForm
    code = ErrorCode.common

    def get(self, request, base_id, *args, **kwargs):

        """ 这个是获取单个数据 """
        interface = self.module.objects.filter(pk=base_id).first()
        if not interface:
            return response_failed(code=self.code, message='数据不存在')
        ret = model_to_dict(interface)
        ret['context'] = json.loads(ret['context'], encoding='utf-8')
        return response_success(ret)

    def put(self, request, base_id, *args, **kwargs):
        """ 这个是全量修改数据 """
        body = request.body
        data = json.loads(body, encoding='utf-8')

        if 'context' not in data:
            return response_failed()
        data['context'] = json.dumps(data['context'])

        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        interface = self.module.objects.filter(id=base_id).first()
        if not interface:
            return response_failed(code=self.code, message='数据不存在')

        self.module.objects.filter(id=base_id).update(**form.cleaned_data)
        interface = self.module.objects.filter(id=base_id).first()

        ret = model_to_dict(interface)
        ret['context'] = json.loads(ret['context'], encoding='utf-8')
        return response_success(ret)


    def delete(self, request, base_id, *args, **kwargs):
        """ 这个是删除数据 """
        interface = self.module.objects.filter(id=base_id)
        if not interface:
            return response_failed(code=self.code, message='数据不存在')
        interface.delete()
        return response_success()