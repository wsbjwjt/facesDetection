from .models import Employee
import time
from PIL import Image
import io
import base64

def recognize_image(image):
    return '100002'


def build_result_dict(employee: Employee):
    return {'result': 'success',
            'employee_number': employee.employee_number,
            'employee_name': employee.employee_name,
            'department_name': employee.department.department_name,
            'record_time': time.strftime("%Y-%m-%d %H:%M", time.localtime())
            }


def decode_base64(img_base64):
    img_data = base64.b64decode(img_base64)
    image = io.BytesIO(img_data)
    img = Image.open(image)
    # img.show()
    return img