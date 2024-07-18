from django.shortcuts import redirect, render
from .short_logic import url
# Create your views here.
def index(request) :
    message = request.session.pop('message', '')
    if message == '':
        return render(request,'index.html')
    elif message == 'valid':
        context = {
            'message': 'valid' , 
            'normal' : request.session['normal'] ,
            'shorten' : request.session['shorten']
        }
    else : 
        context = {
        'message': 'not valid'
        }
    return render(request,'index.html',context)
def Convert_url(request):
    user_url = request.POST.get("url", "")
    ur = url(user_url)
    if ur.validation() :
        ur.generate_shorten_url()
        ur.save()
        urls = ur.get_info()
        request.session['message'] = 'valid'
        request.session['normal'] = urls[0]
        request.session['shorten'] = urls[1]
    else : 
        request.session['message'] = 'not valid'
    return redirect("http://127.0.0.1:8000/url_shortener/")
def redirecting(request,url_code):
    user_url = url("")
    search_result = user_url.url_from_shorten_url("http://127.0.0.1:8000/url_shortener/task1/"+url_code)
    if search_result is None :
        context = {
            'message': 'entry not valid' ,
        }
        return render(request,'index.html',context)
    else :
        return redirect(user_url.url)
    
        
