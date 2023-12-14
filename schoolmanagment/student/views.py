from django.shortcuts import render

# Create your views here.
def student_home(request):
    return render(request,'student_dashboard.html')
def student_exam(request):
    return render(request,'student_exam.html')


def attend_exam(request):
    
    return render(request,'take_exam.html',{'course':"msc cs",'total_questions':10,'total_marks':100})

def start_exam(request):
    questions = [
    {
        'question': "What is the capital of France?",
        'marks': 2,
        'option1': "Paris",
        'option2': "Berlin",
        'option3': "Madrid",
        'option4': "Rome",
    },
    {
        'question': "Who wrote 'Romeo and Juliet'?",
        'marks': 3,
        'option1': "William Shakespeare",
        'option2': "Charles Dickens",
        'option3': "Jane Austen",
        'option4': "Mark Twain",
    },
    
    ]

    return render(request,'start_exam.html',{'course':"Msc Maths",'questions':questions})

def view_result(request):
    courses = [
        {'id': 1, 'course_name': 'Mathematics'},
        {'id': 2, 'course_name': 'Science'},
        {'id': 3, 'course_name': 'History'},
        # Add more courses as needed
    ]
    return render(request,'view_result.html',{'courses':courses})


def student_marks(request):
    return render(request,'student_marks.html',{'courses':"courses"})

def check_marks(request):
    return render(request,'check_marks.html',{'results':""})

def student_signup(request):
    return render(request,'student_signup.html')

def student_login(request):
    return render(request,'student_login.html')
