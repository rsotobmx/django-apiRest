import json

from django.http.response import JsonResponse
from django.views import View
from .models import Company
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message': "Success", 'company': company}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos = {'message': "Success", 'companies': companies}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        print (jd)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass

