from datetime import datetime  # Add this line at the top of your views.py file

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import UserData
from travel.models import Regi, Destination
from django.contrib import messages
from project import settings
from django.core.mail import send_mail


# def home(request):
#     my_object = Destination.objects.all()
#     template = loader.get_template('home.html')
#
#     context = {
#         'my_object': my_object,
#     }
#     return HttpResponse(template.render(context, request))
def home(request):
    destinations = Destination.objects.all()
    context = {
        'destinations': destinations,
    }
    return render(request, 'home.html', context)


def index(request):
    template = loader.get_template('login_page.html')
    return HttpResponse(template.render({}, request))


def login(request):
    if request.method == "POST":
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        # print("TTTT###:-",Password, Username)
        try:
            mymembers = Regi.objects.all().values()
            # user = Regi.objects.get(username=Username, password=Password)
            for i in mymembers:
                # print("testing ",i)
                if Username == i['user'] and Password == i['password']:
                    # print("TEST222")
                    return render(request, 'distance.html')
            return render(request, 'login_page.html', {'error_message': 'Invalid username or password.'})
        except Regi.DoesNotExist:
            # print("YIIII##")
            import traceback
            traceback.print_exc()
            return render(request, 'login_page.html', {'error_message': 'Invalid username or password.'})
    else:
        # print("TEST#33")
        return render(request, 'login_page.html')


def map(request):
    template = loader.get_template('map.html')
    return HttpResponse(template.render({}, request))


def weather(request):
    template = loader.get_template('wether.html')
    return HttpResponse(template.render({}, request))


def registration(request):
    template = loader.get_template('registration_page.html')
    return HttpResponse(template.render({}, request))


def registration_data(request):
    if request.method == 'POST':
        # Use request.POST instead of request.post
        a = request.POST.get('fullname')
        b = request.POST.get('username')
        c = request.POST.get('email')
        d = request.POST.get('password')
        e = request.POST.get('contact')
        f = request.POST.get('city')
        g = request.POST.get('address')

        # Validate the data before creating the Registration instance and saving it
        if a and b and c and d and e and f and g:
            member = Regi(fullname=a, user=b, email=c, password=d, contact=e, city=f, address=g)
            member.save()
            return render(request, 'registration_success.html', {})
        else:
            # Handle the case where the form data is not complete
            return render(request, 'registration_error.html', {'error_message': 'Please fill in all the fields'})

    # Handle the case where the request method is not POST
    return render(request, 'registration_error.html', {'error_message': 'Invalid request method'})


def distance(request):
    template = loader.get_template('distance.html')
    return HttpResponse(template.render())


def wether(request):
    template = loader.get_template('wether.html')
    return HttpResponse(template.render({}, request))


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))


def contact_data(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    desc = request.POST.get('desc')
    date = datetime.today()
    userdata = UserData(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
    userdata.save()
    messages.success(request, 'Profiles Detailed Updated.')

    global mail
    if request.method == "POST":
        mail = request.POST.get('email')

    subject = "Greetings"
    msg = "Thanks for Contact us to jk Travel❤😊"

    to = mail
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if res == 1:
        return HttpResponseRedirect(reverse('distance'))
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)
