from django.views.generic import View

class ServiceDetailView(View):

    def get(self, request, service_id, *args, **kwargs):
        """ 这个是获取单个数据 """
        pass


    def put(self, request, service_id, *args, **kwargs):
        """ 这个是全量修改数据 """
        pass

    def patch(self, request, service_id, *args, **kwargs):
        """ 这个是部分修改数据 """
        pass

    def delete(self, request, service_id, *args, **kwargs):
        """ 这个是删除数据 """
        pass