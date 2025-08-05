from django.shortcuts import render
from .forms import FileUploadForm
from .models import FormUpload

from django.http import JsonResponse

# Create your views here.
def file_upload_form(req):
    if req.method=='GET':
        form = FileUploadForm() # empty Form
        return render(req,'Form_app/upload.html',{'form':form})
    
    if req.method == 'POST':
        form = FileUploadForm(req.POST,req.FILES) #blob or bytes

        if form.is_valid():
            # file_upload = FormUpload(name=req.POST['name'],file=req.FILES['file']) # record
            # file_upload.save()

            form.save()

            return JsonResponse({'success':True})
        
        return JsonResponse({'error':form.errors})

