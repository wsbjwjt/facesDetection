from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from .models import Employee
from .recognize_service import recognize_image, build_result_dict, decode_base64


@api_view(http_method_names=['GET', 'POST'])
def recognize_face(request: HttpRequest):
    #
    img_stream = request.POST.get("face_image")
    emp_id = recognize_image(decode_base64(img_stream))

    if emp_id is None:
        return Response({'result': 'failed'})
    else:
        employee = Employee.objects.get(employee_number=emp_id)
        return Response(build_result_dict(employee))
