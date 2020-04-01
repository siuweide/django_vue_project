from django.views.generic import View

class ServiceListView(View):

    def get(self, request, *args, **kwargs):
        """ 这个是获取所有数据 """
        pass

    def post(self, request, *args, **kwargs):
        """ 这个是创建数据 """
        pass