#from django.http import HttpResponse
from django.shortcuts import render ,redirect
from myapp.models import Contact
from django.contrib import messages

from myapp.models import Subscribers
from django.core.mail import send_mail







def home(request):
    if request.method == 'POST':
        Sub_email = request.POST.get('Sub_email')
        SUB = Subscribers(Sub_email = Sub_email)
        SUB.save()
        messages.add_message(request, messages.INFO,'your message is sent successfully!')
        return render(request,"webapp/home/Home.html")
    return render(request,"webapp/home/Home.html")





def services(request):
    if request.method == 'POST':
        Sub_email = request.POST.get('Sub_email')
        SUB = Subscribers(Sub_email = Sub_email)
        SUB.save()
        messages.add_message(request, messages.INFO,'your message is sent successfully!')
        return render(request, "webapp/home/services.html")
    return render(request, "webapp/home/services.html")


def about(request):
    if request.method == 'POST':
        Sub_email = request.POST.get('Sub_email')
        SUB = Subscribers(Sub_email = Sub_email)
        SUB.save()
        messages.add_message(request, messages.INFO,'your message is sent successfully!')
        return render(request, "webapp/home/abo.html")
    return render(request, "webapp/home/abo.html")



def contact(request):
    if request.method=='POST':
        if 'Con' in request.POST:
            username = request.POST.get('name', False) 
            email = request.POST.get('email', False)
            phone = request.POST.get('phone',False)
            subject = request.POST.get('subject', False)
            message = request.POST.get('message', False)
            DATA = {
                    'username': username,
                    'email': email,
                    'phone': phone,
                    'subject': subject,
                    'message': message 
            }
            message = '''
            New message: {}


            From: {}

            '''.format(DATA['message'], DATA['email'])
            send_mail(DATA['subject'], message, '', ['aorangzaib@numbersniff.com'])




            data = Contact(username=username,email=email,phone=phone,subject=subject,message=message)
            print(data.username)
            data.save()

            print('this record has been created')

            return render(request,"webapp/home/contacts.html")


        elif 'Subscribe' in request.POST:
               Sub_email = request.POST.get('Sub_email')
               SUB = Subscribers(Sub_email = Sub_email)
               SUB.save()
        else:
            return render(request, "webapp/home/contacts.html")
    return render(request, "webapp/home/contacts.html")





''' login page



def login(request):
    if request.method=='POST':
        if 'signup' in request.POST:
            username = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            print("THIS the value of new get",username,email,password)
            data = User(username=username,email=email,password=password)
            data.save()
            print('this record has been created')
            return render(request,"mysite/home/login.html")
        elif 'login' in request.POST:
            print('login is working')
            email = request.POST['email']
            password = request.POST['password']
            val = authenticate(email=email,password=password)
            if val is not None:
                print('this is authentioncate')
                login(request, val)
                return redirect('/')
        else:
            return render(request,"mysite/home/login.html")
    return render(request,"mysite/home/login.html")


    '''