
from django.urls import path
from. import views

urlpatterns = [
    path('student-dashbord/',views.student_home),
    path('student-exam/',views.student_exam),
    path('student-marks/', views.student_marks,name='student-marks'),
    path('attend-exam/',views.attend_exam,name='attend-exam'),
    path('start-exam/',views.start_exam,name='start-exam'),
    path('view-result/', views.view_result,name='view-result'),
    path('check-marks/', views.check_marks,name='check-marks'),
    path('student-signup/', views.student_signup,name='student-signup'),
    path('student-login/', views.student_login,name='student-login'),


]
