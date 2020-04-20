import json

from django.forms import model_to_dict
from interface_app.forms.Interface_form import InterfaceForm
from interface_app.libs.response import ErrorCode, response_success, response_failed
from interface_app.models.interface import Interface
from interface_app.views.base.base_list import BaseListView


class InterfaceListView(BaseListView):

    module = Interface
    form = InterfaceForm
    code = ErrorCode.service

    def get(self, request, *args, **kwargs):

        """ 这个是获取某个服务下的所有接口 """
        service_id = request.GET.get('service_id', 0)
        interface = self.module.objects.filter(service_id=service_id)
        ret = []
        for s in interface:
            # t = dict()
            # t['id'] = s.id
            # t['name'] = s.name
            # t['description'] = s.description
            # t['service_id'] = s.service_id
            # t['context'] = json.loads(s.context, encoding='utf-8')  # 把字符串改为字段传到前端
            t = model_to_dict(s)
            t['context'] = json.loads(t['context'], encoding='utf-8')
            ret.append(t)
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """ 这个是创建数据 """
        body = request.body
        data = json.loads(body, encoding='utf-8')
        if 'context' not in data:
            return response_failed()

        data['context'] = json.dumps(data['context'], encoding='utf-8')
        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        interface = self.model.objects.create(**form.cleaned_data)
        if interface:
            ret = model_to_dict(interface)
            ret['context'] = json.loads(ret['context'], encoding='utf-8')
            return response_success(ret)
        else:
            return response_failed(code=self.code, message='创建服务失败')
