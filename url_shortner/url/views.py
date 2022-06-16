from django.http import HttpResponse
from django.shortcuts import redirect, render
import uuid
from . import models
# Create your views here.
def home(request):
    if request.method=='POST':
        long_url=request.POST['url']
        short_url=str(uuid.uuid4())[:5]
        url=models.link.objects.create(long_url=long_url,short_url=short_url)
        url.save()
        short_url="http://127.0.0.1:8000/"+short_url
        dict={'url':short_url}
        return render(request,'url/home.html',context=dict)
    return render(request,'url/home.html')
# def shorten(request):
#     obj=models.link.objects.get(id=10)
#     print(obj)
#     long_url=obj.long_url
#     short_url=obj.short_url
#     long_url="http://127.0.0.1:8000/"+short_url
#     dict={'url':long_url}
#     return render(request,'url/ans.html',context=dict)
def urlRedirect(request,short_url):
    obj=models.link.objects.get(short_url=short_url)
    print(short_url)
    long_url=obj.long_url
    # long_url="https://"+long_url
    return redirect(long_url)





