from ast import Not
from .models import Feature
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

from cmath import pi
from msilib.schema import ListView
from urllib import response
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer



# Create your views here.
def sidebar(request):
    features = Feature.objects.all()
    return render(request,'sidebar.html',{'features':features})

   
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        username = request.POST['username']
        email = request.POST['email']
        encryptedpassword = make_password(request.POST['password'])
        encryptedpassword = make_password(request.POST['password'])
        

        if encryptedpassword == encryptedpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
           
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists') 
                return redirect('register')
            elif User.objects.filter(last_name=last_name).exists():
                messages.info(request,'lastname already exists') 
                return redirect('register')
            elif User.objects.filter(first_name=first_name).exists():
                messages.info(request,'firstname already exists') 
                return redirect('register')        
            else:
                user = User.objects.create_user(username=username, email=email, password=encryptedpassword,last_name=last_name,first_name=first_name ) 
                user.save();
                return redirect('login')  
        else:
            messages.info(request,'passwords not the same') 
            return redirect('register') 
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        encryptedpassword = make_password(request.POST['password'])

        user = auth.authenticate(username=username, encryptedpassword=encryptedpassword)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')    

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')        
    

def counter(request):
    text = request.POST["text"]
    amount_of_words=len(text.split())
    return HttpResponse(request,'counter.html', { "amount":amount_of_words})

# Create your views here.
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/stamp.html'

def customer_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer,pk=pk)

    template_path = 'customers/pdf2.html'
    context={'customer':customer}

    #Create a django response object and specify content_type as pdf
    response = HttpResponse(content_type = 'application/pdf')
    # response['Content-Disposition'] = 'attachment; filename = "report.pdf"'
    
    #find the template and render it
    template = get_template(template_path)
    html = template.render(context)

    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest = response
    )

    #if error then show some funny view
    if pisa_status.err:
        return HttpResponse("we had some errors<pre>" + html + "<pre>")
    return response    






def render_pdf_view(request):
    template_path = 'customers/pdf1.html'
    context={'myvar':'this is my template path'}

    #Create a django response object and specify content_type as pdf
    response = HttpResponse(content_type = 'application/pdf')
    # response['Content-Disposition'] = 'attachment; filename = "report.pdf"'
    
    #find the template and render it
    template = get_template(template_path)
    html = template.render(context)

    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest = response
    )

    #if error then show some funny view
    if pisa_status.err:
        return HttpResponse("we had some errors<pre>" + html + "<pre>")
    return response    



