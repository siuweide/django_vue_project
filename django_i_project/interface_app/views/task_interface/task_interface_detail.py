
from interface_app.forms.task_form import TaskInterfaceForm
from interface_app.models.task import TaskInterface

from interface_app.libs.response import ErrorCode
from interface_app.views.base.base_detail import BaseDetailView


class TaskInterfaceDetailView(BaseDetailView):

    model = TaskInterface
    form = TaskInterfaceForm
    code = ErrorCode.task_interface
