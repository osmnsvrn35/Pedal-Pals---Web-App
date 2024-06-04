import secrets
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from datetime import  date
from django.contrib.auth.models import User



def rental_view(request, bike_id):
    if not request.user.is_authenticated:
        return redirect('login')

    bike = Bike.objects.get(id=bike_id)

    if request.method == 'POST':
        start_time = date.fromisoformat(request.POST['start_time'])
        end_time = date.fromisoformat(request.POST['end_time'])
        total_cost = (end_time - start_time).days * bike.price_per_day
        customer = get_object_or_404(Customer, user_name=request.user.username)
        rental = Rental(user=customer, bike=bike, start_time=start_time, end_time=end_time, total_cost=total_cost)
        rental.save()
        bike.available = False
        bike.save()
        return redirect('main_page')

    return render(request, 'reservation.html', {'bike': bike})


def mountain_bikes(request):
    mountain_bike = Bike.objects.filter(bike_type=Bike.MOUNTAIN_BIKE)
    return render(request, 'mountain_bikes.html', {'mountain_bikes': mountain_bike})


def road_bikes(request):
    road_bike = Bike.objects.filter(bike_type=Bike.ROAD_BIKE)
    return render(request, 'road_bikes.html', {'road_bikes': road_bike})


def city_bikes(request):
    city_bike = Bike.objects.filter(bike_type=Bike.CITY_BIKE)
    return render(request, 'city_bikes.html', {'city_bikes': city_bike})


def e_bikes(request):
    e_bike = Bike.objects.filter(bike_type=Bike.E_BIKE)
    return render(request, 'e_bikes.html', {'e_bikes': e_bike})


def main_page(request):
    return render(request, 'main_page.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        password = secrets.token_hex(5)
        send_mail(
            'Password Reset',
            f'Your new password is: {password}',
            'from@example.com',
            [email],
            fail_silently=False,
        )

        return render(request, 'password_reset_done.html')
    return render(request, 'forgot_password.html')



def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            username = form.cleaned_data['username']
            hashed_password = make_password(password)
            try:

                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                customer = Customer(email=email, first_name=first_name,
                            last_name=last_name, password=hashed_password,
                            age=age, phone_number=phone_number, address=address,user_name=username)

                customer.save()
                return HttpResponseRedirect(f'/bicycle_rental/login')
            except IntegrityError:
                form.add_error('email', "This email is already used.")
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/bicycle_rental/')
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(f'/bicycle_rental/')


from django.shortcuts import render, redirect


def report_damage(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        bike = Bike.objects.get(id=request.POST['bike_id'])
        description = request.POST['description']
        report = DamageReport(user=request.user, bike=bike, description=description)
        report.save()
        return redirect('main_page')
    else:
        bikes = Bike.objects.all()
        return render(request, 'report_damage.html', {'bikes': bikes})


def bike_history(request):
    bikes = Bike.objects.all()
    
    customer = get_object_or_404(Customer, user=request.user)

   
    rental_history = Rental.objects.filter(user=customer)
    context = {
        'bikes': bikes,
        'rental_history' : rental_history,
        
    }
    return render(request, 'history.html', context)
    


