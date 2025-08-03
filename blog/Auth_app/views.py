from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import user
from .serializer import UserSerializer
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def signup(request):
    return render(request, 'Auth_app/index.html')

@csrf_exempt
def data_view(request):
    if request.method=="GET":
        user_data=user.objects.all() #queryset -> [object]
        print(user_data)
        sd=UserSerializer(user_data,many=True) #JSON
        return JsonResponse(sd.data, safe=False) #list serialized data
    
    if request.method=="POST":
        input_data=json.loads(request.body) #json data 
        sd=UserSerializer(data=input_data) 

        if sd.is_valid(): #validating the data
            sd.save() #saving the data

            res={
            'succes':True,
            'message':"Data Saved Successfully"  
            }

            return JsonResponse(res,status=201)
        

@csrf_exempt
def sud_view(request,pk):
    if request.method=='GET':
        try: 
            single_user=user.objects.get(pk=pk) #object
            sd=UserSerializer(single_user)

            res={
            'success':True,
            'data':sd.data  
            }
            return JsonResponse(res,status=200)
        
        except Exception as e:
            res={
            'success':False,
            'error':str(e), 
            }

            return JsonResponse(res,status=404)
        
    if request.method=="PATCH": # partial updating the data

        single_user=user.objects.get(pk=pk) #finding user
        input_data=json.loads(request.body) #getting data from the client side

        sd=UserSerializer(single_user,data=input_data,partial=True)

        if sd.is_valid():
            sd.save()
            res={
            'success':True,
            "message":"partial data updated successfully" 
            }
            return JsonResponse(res,status=200)
        
    if request.method=="DELETE":
        single_user=user.objects.get(pk=pk)
        single_user.delete()
        res={
            'success':True,
            "message":"data deleted successfully" 
            }
        return JsonResponse(res,status=200)
    

    
        #Put