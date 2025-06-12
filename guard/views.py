from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Guard,Service,Booking,User,Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout as django_logout
# Create your views here.

def myProfile(request):
    return render(request,'myProfile.html')
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if full_name and email and message:
            Contact.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                message=message
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request,'Passwords do not match.')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists.')
            return redirect('signup')
        User.objects.create(
            username = email,
            email = email,
            first_name = name,
            phone = phone,
            password = make_password(password)
        )
        messages.success(request,'Account created successfully.Please login.')
        return redirect('login')
    return render(request,'signup.html')

def logout(request):
    django_logout(request)
    return redirect('login')

def guard_list(request):
    guards = Guard.objects.all()
    return render(request,'guards.html',{'guards':guards})

def services(request):
    services = Service.objects.all()
    return render(request,'services.html',{'services':services})

@login_required(login_url='login')
def book_service(request):
    services = Service.objects.all()
    guards = Guard.objects.filter(availability_status='Available')
    if request.method == 'POST':
        service_id = request.POST.get('service')
        guard_id = request.POST.get('guard')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        Booking.objects.create(
            user = request.user,
            guard = guard_id,
            service = service_id,
            booking_date = booking_date,
            booking_time = booking_time
        )
        return HttpResponse("Booking successfull")
    return render(request,'bookNow.html',{'services':services,'guards':guards})

def contact_view(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print("POST DATA:", full_name, email, phone, message)

        if full_name and email and message:
            contact = Contact.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                message=message
            )
            print("Saved:", contact.id)
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all required fields.")
            return redirect('contact')

    return render(request, "contact.html")

@login_required
def make_guard_profile(request):
    guard = getattr(request.user, 'guard', None)

    if request.method == 'POST':
        skills = request.POST.get('skills')
        experience = request.POST.get('experience')
        availability = request.POST.get('availability_status')
        image = request.FILES.get('guardImage')

        if guard:
            # Update existing profile
            guard.skills = skills
            guard.experience = experience
            guard.availability_status = availability
            if image:
                guard.guardImage = image
            guard.save()
            messages.success(request, 'Guard profile updated successfully.')
        else:
            # Create new profile
            guard = Guard.objects.create(
                user=request.user,
                skills=skills,
                experience=experience,
                availability_status=availability,
                guardImage=image
            )
            messages.success(request, 'Guard profile created successfully.')

        return redirect('myProfile')  # Replace with your actual profile view name

    return render(request, 'make_profile_guard.html', {'guard': guard})