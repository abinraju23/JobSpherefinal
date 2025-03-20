
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('employee/delete/<int:wo_id>/', views.delete_employee, name='delete_employee'),
    path('reshome/', views.reshome, name = 'reshome'), 
    path('resume/', views.gen_resume, name = 'resume'),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('browsejobs/', views.browse_jobs, name='browse_jobs'),
    path('job_details/<int:job_id>/', views.job_details, name='job_details'),
    path('filter_jobs/', views.filterjob, name='filterjob'),
    path('about/', views.about, name='about'),
    path('post_job/', views.post_job, name='post_job'),
    path('create_job/', views.create_job, name='create_job'),
    path('employer_register/', views.create_employer, name='create_employer'),
    path('employee_register/', views.create_employee, name='create_employee'),
    path('employee_detail/<int:wo_id>/', views.employee_detail, name='employee_detail'),
    path('employee_list/',views.employee_list,name='employee_list'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'), 
    path('employee/edit/<int:wo_id>/', views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:wo_id>/',views.delete_employee, name='delete_employee'),
    path('edit-job/<int:job_id>/',views.edit_job, name='edit_job'),
    path('delete-job/<int:job_id>/',views.delete_job, name='delete_job'),
    path('employer/<int:employer_id>/', views.employer_detail, name='employer_detail'),
    path('employer/<int:employer_id>/edit/', views.edit_employer, name='edit_employer'),
    path('employer/<int:employer_id>/delete/', views.delete_employer, name='delete_employer'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('job/<int:job_id>/update_status/<int:employee_id>/', views.update_job_status, name='update_job_status'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)