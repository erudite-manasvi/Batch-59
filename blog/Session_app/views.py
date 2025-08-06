from django.shortcuts import render

from .models import User
from django.http import JsonResponse

# Create your views here.
def login(req):
    if req.session.get('username'):
        return JsonResponse({
            "message":"Already loggedIn",
            "user": req.session.get('username')
        })
    
    if req.method =='POST':
        username=req.POST['username']
        password=req.POST['password']

        try:
            user = User.objects.get(username=username)
            if user.password==password:
                req.session['username']=username
                req.session.set_expiry(15)
                return JsonResponse({
                    'success':True,
                    'message':'User loggedIn Successfully!!'
                })
            
        except Exception as e:
            return JsonResponse({
                    'success':False,
                    'message':str(e)
                })


    return render(req,'Session_app/login.html')