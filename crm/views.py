from django.shortcuts import render
from django.views.generic import View
from crm.models import Employee
from django.http import JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeCreateView(View):

    def get(self,request):

        qs = Employee.objects.all().values()

        Employee_list = list(qs)

        return JsonResponse(Employee_list,safe=False)

    def post(self,request):

        json_data = loads(request.body)

        qs = Employee.objects.create(
            name = json_data.get("name"),
            department = json_data.get("department"),
            salary = json_data.get("salary"),
            location = json_data.get("location"),
            email = json_data.get("email")
            )

        response_data = {"message":"creation completed"}

        return JsonResponse(response_data)


class EmployeeRetrieveUpdateDeleteView(View):

    def get(self,request,pk=None):

        qs = Employee.objects.filter(id=pk).values()

        Employee_details = list(qs)

        return JsonResponse(Employee_details,safe=False)
