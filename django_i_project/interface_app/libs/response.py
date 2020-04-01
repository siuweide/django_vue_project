from django.http import JsonResponse

class ErrorCode:
    common = 10000
    auth = 10001

# 这是一个通用的
def common_response(success, data, error_code, error_message):
    response = {
        "data": data,
        "success": success,
        "error": {
            "code":error_code,
            "message": error_message
        }
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii':False}, safe=False)

# 这两个是快捷方式

def response_success(data={}):
    return common_response(True,data, "", "")

def response_failed(code=ErrorCode.common, message="参数错误", data={}):
    return common_response(False, data, code, message)