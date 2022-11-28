from django.shortcuts import render, HttpResponse
from WebCytePages.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def TRIALindex(request): #Ofcourse, This Function works. :)
    content = {
        'value1' : 'Hello',
        'value2' : 'Bolo'
    }
    return render(request, 'TRIALindex.html', content)
    #return HttpResponse('<h1>This is Home page.</h1>')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('<h1>This is About page.</h1>')
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.now())

        contact.save()
        messages.success(request, "Your message has been sent!!")
    return render(request, 'contact.html')
    #return HttpResponse('<h1>This is Contact page.</h1>')

def featured(request):
    return render(request, 'featured.html')
    #return HttpResponse('<h1>This is featured page.</h1>')

#def search(request):
    #return HttpResponse('<h1>This is Search page.</h1>')