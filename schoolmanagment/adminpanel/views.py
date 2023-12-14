from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def admin_login(request):
    return render(request,'admin_login.html')


def admin_dashboard(request):
    dict={
    'total_student':5,
    'total_course':4,
    'total_question':10,
    }
    return render(request,'admin_dashboard.html',context=dict)

def admin_student_view(request):
    dict={
    'total_student':10,
    }
    return render(request,'admin_student.html',context=dict)

def admin_view_student_marks(request):
    students = [
        {
            'id': 1,
            'name': 'John Doe',
            'profile_pic': 'path/to/john_doe.jpg',
        },
        {
            'id': 2,
            'name': 'Jane Doe',
            'profile_pic': 'path/to/jane_doe.jpg',
        },
        # Add more student entries as needed
    ]

    return render(request,'admin_view_student_marks.html',{'students':students})


def admin_view_marks(request):
    courses = [
        {
            'id': 1,
            'course_name': 'Mathematics Exam',
        },
        {
            'id': 2,
            'course_name': 'Science Exam',
        },
        # Add more exam entries as needed
    ]
    return render(request,'admin_view_marks.html',{'courses':courses})


def admin_view_student_view(request):
    students = [
        {
            'id': 1,
            'name': 'John Doe',
            'profile_pic': 'path/to/john_doe.jpg',
            'mobile': '123-456-7890',
            'address': '123 Main St, City',
        },
        {
            'id': 2,
            'name': 'Jane Doe',
            'profile_pic': 'path/to/jane_doe.jpg',
            'mobile': '987-654-3210',
            'address': '456 Oak St, Town',
        },
        # Add more student entries as needed
    ]

    
    return render(request,'admin_view_student.html',{'students':students})

def update_student(request):
    
    return render(request,'update_student.html')


def delete_student(request):
    
    return redirect('admin-view-student')





def admin_view_question(request):
    courses = [
        {
            'id': 1,
            'course_name': 'Mathematics',
            'question_number': 20,
            'total_marks': 100,
        },
        {
            'id': 2,
            'course_name': 'Science',
            'question_number': 15,
            'total_marks': 75,
        },
        # Add more course entries as needed
    ]


    return render(request,'admin_view_question.html',{'courses':courses})


def view_question(request):
    questions = [
        {
            'id': 1,
            'question': 'What is the capital of France?',
            'marks': 10,
        },
        {
            'id': 2,
            'question': 'Who discovered gravity?',
            'marks': 8,
        },
        # Add more question entries as needed
    ]

    return render(request,'view_question.html',{'questions':questions})

def delete_question_view(request):

    return redirect('admin-view-question')


def admin_question(request):
    return render(request,'admin_question.html')

from django.shortcuts import render, redirect
from .models import Question

def admin_add_question_view(request):
    if request.method == 'POST':
        # Retrieve data from the form
        course_id = request.POST.get('courseID')
        question_text = request.POST.get('question')
        marks = request.POST.get('marks')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        answer = request.POST.get('answer')

        Question.objects.create(
            course=course_id,
            question=question_text,
            marks=marks,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            answer=answer
        )

        return redirect('admin-view-question')  

    return render(request, 'admin_add_question.html')
