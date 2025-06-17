from django.shortcuts import render , redirect
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
import json
import random
import stripe
# from .models import register
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from . import models,emailAPI
import time
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from .models import Register  # or your course model if you have one

def home(request):
    courses = [
        {
            "image_url": "/static/img/course-1.jpg",
            "title": "Web Design & Development Course for Beginners",
            "price": 199.00,
            "stars": range(5),
            "reviews_count": 95673845,
            "instructor": "Naruto Uzumaki",
            "duration": "1.49 Hrs",
            "students_count": 95673849,
            "read_more_url": reverse('read_more'),
            "join_url": reverse('join'),
        },
        {
            "image_url": "/static/img/course-2.jpg",
            "title": "Advanced Graphic Design Course",
            "price": 299.00,
            "stars": range(4),
            "reviews_count": 951,
            "instructor": "Sung Jin-Woo",
            "duration": "2.5 Hrs",
            "students_count": 951,
            "read_more_url": reverse('read_more'),
            "join_url": reverse('join'),
        },
        {
            "image_url": "/static/img/course-3.jpg",
            "title": "Complete Video Editing Course",
            "price": 199.00,
            "stars": range(5),
            "reviews_count": 60,
            "instructor": "Ken Kaneki",
            "duration": "3 Hrs",
            "students_count": 60,
            "read_more_url": reverse('read_more'),
            "join_url": reverse('join'),
        },
    ]
    testimonials = [
        {
            "image_url": "/static/img/goku.jpeg",
            "name": "Goku",
            "profession": "Universe Saver",
            "feedback": "“Thanks to Chinu, I mastered Sung Jin-Woo’s skills with ease. The training was intense, focused, and powerful—just like me. Now, I’m stronger than ever!” 💪🔥",
        },
        {
            "image_url": "/static/img/onepunch.jpeg",
            "name": "Saitama",
            "profession": "Punch King",
            "feedback": "“Thanks to Chinu, I mastered Naruto’s Shadow Clone technique. Now, I can handle multiple challenges effortlessly. The training is simple yet incredibly effective—making me truly unstoppable!”",
        },
        {
            "image_url": "/static/img/gojo.jpg",
            "name": "Saturo Gojo",
            "profession": "3rd year student at jujutsu tech",
            "feedback": "“Training with expert instructors at Chinu was an incredible experience. The sessions were challenging yet fun, pushing my limits and helping me grow stronger every day. Highly recommended!”",
        },
        {
            "image_url": "/static/img/gpt.png",
            "name": "Chat gpt",
            "profession": "AI Chatbot",
            "feedback": "“Chinu offers top-notch courses with expert instructors and practical projects. The platform’s flexibility and rich resources make learning enjoyable and effective. A perfect place to upskill anytime, anywhere!”",
        },
    ]
    instructors = [
        {
            "image_url": "/static/img/instructor-1.jpg",
            "name": "Chinmay Joshi",
            "designation": "All Rounder (PRO) ",
            "facebook_url": "https://facebook.com/instructor1",
            "twitter_url": "https://twitter.com/instructor1",
            "instagram_url": "https://instagram.com/instructor1",
        },
        {
            "image_url": "/static/img/instructor-2.jpg",
            "name": "Nitin Sen",
            "designation": "Python Developer",
            "facebook_url": "https://facebook.com/instructor2",
            "twitter_url": "https://twitter.com/instructor2",
            "instagram_url": "https://instagram.com/instructor2",
        },
        {
            "image_url": "/static/img/instructor-3.jpg",
            "name": "Naruto Uzumaki",
            "designation": "Never Give Up",
            "facebook_url": "https://facebook.com/instructor3",
            "twitter_url": "https://twitter.com/instructor3",
            "instagram_url": "https://instagram.com/instructor3",
        },
        {
            "image_url": "/static/img/instructor-4.jpg",
            "name": "Ken Kaneki",
            "designation": "Never trust anyone",
            "facebook_url": "https://facebook.com/instructor4",
            "twitter_url": "https://twitter.com/instructor4",
            "instagram_url": "https://instagram.com/instructor4",
        },
    ]
    context = {
        "courses": courses,
        "testimonials": testimonials,
        "instructors": instructors,
    }
    return render(request, "home.html", context)

def courses(request):
    courses = [
        {
            "image_url": "/static/img/course-1.jpg",
            "title": "Web Design & Development Course for Beginners",
            "price": 149.00,
            "stars": range(5),  # Number of stars
            "reviews_count": 123,
            "instructor": "Naruto Uzumaki",
            "duration": "1.49 Hrs",
            "students_count": 30,
            "read_more_url": "#",
            "join_url": "#",
        },
        {
            "image_url": "/static/img/course-2.jpg",
            "title": "Advanced Graphic Design Course",
            "price": 199.00,
            "stars": range(4),
            "reviews_count": 98,
            "instructor": "Sung Jin-Woo",
            "duration": "2.5 Hrs",
            "students_count": 45,
            "read_more_url": "#",
            "join_url": "#",
        },
        {
            "image_url": "/static/img/course-3.jpg",
            "title": "Complete Video Editing Course",
            "price": 129.00,
            "stars": range(5),
            "reviews_count": 150,
            "instructor": "Ken Kaneki",
            "duration": "3 Hrs",
            "students_count": 60,
            "read_more_url": "#",
            "join_url": "#",
        },
    ]
    return render(request, "courses.html", {"courses": courses})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, "about.html")

def pages(request):
    return render(request, "pages.html")

def team(request):
    instructors = [
        {
            "image_url": "/static/img/instructor-1.jpg",
            "name": "Instructor Name 1",
            "designation": "Designation 1",
            "facebook_url": "#",
            "twitter_url": "#",
            "instagram_url": "#",
        },
        {
            "image_url": "/static/img/instructor-2.jpg",
            "name": "Instructor Name 2",
            "designation": "Designation 2",
            "facebook_url": "#",
            "twitter_url": "#",
            "instagram_url": "#",
        },
        {
            "image_url": "/static/img/instructor-3.jpg",
            "name": "Instructor Name 3",
            "designation": "Designation 3",
            "facebook_url": "#",
            "twitter_url": "#",
            "instagram_url": "#",
        },
        {
            "image_url": "/static/img/instructor-4.jpg",
            "name": "Instructor Name 4",
            "designation": "Designation 4",
            "facebook_url": "#",
            "twitter_url": "#",
            "instagram_url": "#",
        },
    ]
    return render(request, 'team.html')

def userpage(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('join')
    user = register.objects.get(email=email)
    return render(request, 'userpage.html', {'user': user})

def testimonial(request):
    testimonials = [
        {
            "image_url": "/static/img/goku.jpeg",
            "name": "Goku",
            "profession": "Universe Saver",
            "feedback": "“Thanks to Chinu, I mastered Sung Jin-Woo’s skills with ease. The training was intense, focused, and powerful—just like me. Now, I’m stronger than ever!” 💪🔥",
        },
        {
            "image_url": "/static/img/onepunch.jpeg",
            "name": "Saitama",
            "profession": "Punch King",
            "feedback": "“Thanks to Chinu, I mastered Naruto’s Shadow Clone technique. Now, I can handle multiple challenges effortlessly. The training is simple yet incredibly effective—making me truly unstoppable!”",
        },
        {
            "image_url": "/static/img/gojo.jpg",
            "name": "Saturo Gojo",
            "profession": "3rd year student at jujutsu tech",
            "feedback": "“Training with expert instructors at Chinu was an incredible experience. The sessions were challenging yet fun, pushing my limits and helping me grow stronger every day. Highly recommended!”",
        },
        {
            "image_url": "/static/img/gpt.png",
            "name": "Chat gpt",
            "profession": "AI Chatbot",
            "feedback": "“Chinu offers top-notch courses with expert instructors and practical projects. The platform’s flexibility and rich resources make learning enjoyable and effective. A perfect place to upskill anytime, anywhere!”",
        },
    ]
    return render(request, 'testimonial.html', {"testimonials": testimonials})

def join(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        # ... aur bhi fields ho toh unko bhi lo

        # User create karo (agar custom model hai toh)
        user = register.objects.create(
            firstname=name,
            email=email,
            password=password,  # NOTE: password ko hash karo production me!
            # ... aur bhi fields
        )
        user.save()

        # Django ka authenticate/login use nahi kar sakte agar custom model hai toh
        # Toh session me user ka regid ya email save kar lo
        request.session['user_email'] = email

        # User page pe redirect karo
        return redirect('userpage')  # 'userpage' url ka naam hai

    return render(request, 'join.html')

def join_course(request):
    course_name = request.GET.get('course_name', 'Unknown Course')
    course_price = request.GET.get('course_price', '0.00')
    return render(request, 'joincourse.html', {'course_name': course_name, 'course_price': course_price})

def read_more(request):
    return render(request, 'read_more.html')

def process_payment(request):
    if request.method == 'POST':
        course_name = request.POST.get('course')
        course_price = request.POST.get('price')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        # Stripe expects price in cents
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': course_name,
                        },
                        'unit_amount': int(float(course_price) * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                customer_email=email,
                success_url=request.build_absolute_uri(reverse('home')) + '?success=true',
                cancel_url=request.build_absolute_uri(reverse('home')) + '?canceled=true',
            )
            return redirect(session.url)
        except Exception as e:
            return render(request, 'joincourse.html', {
                'course_name': course_name,
                'course_price': course_price,
                'error': str(e)
            })
    return redirect('home')

@csrf_exempt
def verify_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            # Example: Check if email is already in use
            if User.objects.filter(email=email).exists():
                return JsonResponse({'valid': False, 'message': 'Email is already in use.'})

            # Example: Add external API email validation logic here
            # For now, assume all emails are valid
            return JsonResponse({'valid': True})
        except Exception as e:
            return JsonResponse({'valid': False, 'message': 'Invalid request.'}, status=400)

    return JsonResponse({'valid': False, 'message': 'Invalid method.'}, status=405)

@csrf_exempt
def send_verification_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            if not email:
                return JsonResponse({'sent': False, 'message': 'Email is required.'}, status=400)
            # Generate OTP
            otp = str(random.randint(100000, 999999))
            # Store OTP and email in session
            request.session['otp_email'] = email
            request.session['otp_code'] = otp
            # Send OTP email
            send_mail(
                'Your OTP for CHINU BHAI LEARNING',
                f'Your OTP code is: {otp}',
                'chinmay30joshi@gmail.com',
                [email],
                fail_silently=False,
            )
            return JsonResponse({'sent': True})
        except Exception as e:
            return JsonResponse({'sent': False, 'message': str(e)}, status=500)
    return JsonResponse({'sent': False, 'message': 'Invalid request.'}, status=400)

@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            otp = data.get('otp')
            email = data.get('email')
            session_otp = request.session.get('otp_code')
            session_email = request.session.get('otp_email')
            if not otp or not email:
                return JsonResponse({'verified': False, 'message': 'OTP and email are required.'}, status=400)
            if session_otp == otp and session_email == email:
                # Optionally clear OTP after successful verification
                del request.session['otp_code']
                del request.session['otp_email']
                return JsonResponse({'verified': True})
            else:
                return JsonResponse({'verified': False, 'message': 'Invalid OTP or email.'}, status=400)
        except Exception as e:
            return JsonResponse({'verified': False, 'message': str(e)}, status=500)
    return JsonResponse({'verified': False, 'message': 'Invalid request.'}, status=400)

def wtf(request):
    return render(request, 'wtf.html')

def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"output": ""})
    else:
        name = request.POST.get("firstName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        p = models.Register(
            firstname=name,
            email=email,
            password=password,
            phone=phone,
            address=address,
            course=course,
            gender=gender,
            status=0,
            role="user",
            info=time.asctime()
        )
        p.save()
        # emailAPI.sendMail(email, password)
        return redirect('/')
    return render(request, "register.html", {"output": "user register successful"})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.Register.objects.filter(email = username, password = password).first()
        print(user)
        if user:
            request.session['sunm'] = username
            return redirect('/')
        
    return render(request, 'login.html')

def admin_login(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "12345":
            request.session['is_admin'] = True
            return redirect('admin_dashboard')
        else:
            error = "Invalid credentials"
    return render(request, "admin_login.html", {"error": error})

def admin_logout(request):
    request.session['is_admin'] = False
    return redirect('admin_login')

def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    # Example: list of courses (replace with your actual model)
    from .models import Register  # Replace with Course model if you have
    courses = Register.objects.all()  # Replace with Course.objects.all()
    return render(request, "admin_dashboard.html", {"courses": courses})

def admin_delete_course(request, course_id):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    from .models import Register  # Replace with Course model if you have
    try:
        course = Register.objects.get(pk=course_id)  # Replace with Course
        course.delete()
    except:
        pass
    return redirect('admin_dashboard')

def admin_add_course(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    msg = ""
    if request.method == "POST":
        # Example: Add course (replace with your actual fields/model)
        title = request.POST.get("title")
        price = request.POST.get("price")
        instructor = request.POST.get("instructor")
        # Add more fields as needed
        Register.objects.create(firstname=title, email="dummy@dummy.com", password="dummy", phone="0", address="dummy", course=title, gender="N/A", status=1, role=instructor, info="Course Added")
        msg = "Course added!"
    return render(request, "admin_add_course.html", {"msg": msg})