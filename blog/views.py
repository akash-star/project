from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Signup
from .forms import CommentForm

# Create your views here.
def blog(request):
    if request.method == "POST":
        email=request.POST["email"]
        new_signup= Signup()
        new_signup.email=email
        new_signup.save()
    return render(request, 'blog/courses.html')

def curr(request):
    course_list = Course.objects.filter(categories__title='Current affair')

    context = {
        'course_list':course_list
    }
    return render(request, 'blog/curr.html', context)

def tech(request):
    course_list = Course.objects.filter(categories__title='Technology')

    context = {
        'course_list':course_list
    }
    return render(request, 'blog/tech.html', context)

def course_detail(request, blog_id):
    course= get_object_or_404(Course, id=blog_id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user= request.user
            form.instance.course = course
            form.save()
            return render(request,'blog/course_detail.html')
    context = {
        'course':course,
        'form':form
    }
    return render(request, 'blog/course_detail.html', context)

def contact(request):
    return render(request, 'blog/contact.html')
