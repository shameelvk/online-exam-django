from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('home/',views.show),
    path('admin-dashboard/', views.admin_dashboard,name='admin-dashboard'),
    path('admin-student/', views.admin_student_view,name='admin-student'),
    path('admin-student/admin-view-student-marks', views.admin_view_student_marks,name='admin-view-student-marks'),
    path('admin-view-marks/', views.admin_view_marks,name='admin-view-marks'),
    path('admin-student/admin-view-student/', views.admin_view_student_view,name='admin-view-student'),
    path('update-student/', views.update_student,name='update-student'),
    path('delete-student/', views.delete_student,name='delete-student'),




    path('admin-question', views.admin_question,name='admin-question'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    path('admin-view-question', views.admin_view_question,name='admin-view-question'),
    path('view-question/', views.view_question,name='view-question'),
    path('delete-question/', views.delete_question_view,name='delete-question'),
]
