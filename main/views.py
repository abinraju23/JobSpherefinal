from employer.forms import JobForm, EmployerForm,UserForm
from employer.models import Job,Employer
from .forms import *
from .models import Employee,Jobstatus
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count
from django import template


#LOGIN VIEWS

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


#PAGE VIEWS



def home(request):
    jobs = Job.objects.all()[:5]
    employers = Employer.objects.all()
    return render(request, 'index.html', {
        'jobs': jobs,
        'employers': employers, # Pass the icons to the template
    })
    
def about(request):
    jobcount= Job.objects.count()
    empcount= Employer.objects.count()
    return render(request,'about.html',{'jobcount':jobcount,'empcount':empcount})

def filterjob(request,category):
    jobs = Job.objects.filter(category=category)
    return render(request, 'jobs.html', {'jobs': jobs})


def browse_jobs(request):

    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})


def job_details(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    employee = None
    job_status = None
    job_statuses = Jobstatus.objects.filter(job=job)  # Get all job statuses for this job
    
    # Check if user is authenticated and is an employee
    if request.user.is_authenticated and hasattr(request.user, 'employee'):
        employee = request.user.employee
        # Try to get the job status for this specific employee and job
        job_status = Jobstatus.objects.filter(job=job, employee=employee).first()
    
    context = {
        'job': job,
        'job_status': job_status,
        'employee': employee,
        'job_statuses': job_statuses,  # Add this to the context
    }
    
    return render(request, 'job_details.html', context)


def contact(request):
    return render(request, 'contact.html')


#EMPLOYER VIEWS

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user.employer 
            job.save()
            return redirect('job_details', job_id=job.pk)
    else:
        form = JobForm()
    return render(request, 'post_job.html', {'form': form})

@login_required
def post_job(request):
    return render(request,'post_job.html')

def create_employer(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employer_form = EmployerForm(request.POST, request.FILES)
        if user_form.is_valid() and employer_form.is_valid():
            user = user_form.save()
            employer = Employer.objects.create(
                user=user,
                name=employer_form.cleaned_data['name'],
                description=employer_form.cleaned_data['description'],
                location=employer_form.cleaned_data['location'],
                website=employer_form.cleaned_data['website'],
                logo=employer_form.cleaned_data['logo']
            )
            login(request, user)
            return redirect('home')
    else:
        user_form = UserForm()
        employer_form = EmployerForm()
    
    return render(request, 'register_employer.html', {
        'user_form': user_form,
        'employer_form': employer_form
    })

@login_required
def update_job_status(request, job_id, employee_id):
    if not hasattr(request.user, 'employer'):
        return redirect('home')  # Redirect if the user is not an employer

    job = get_object_or_404(Job, job_id=job_id)
    employee = get_object_or_404(Employee, wo_id=employee_id)
    
    # Get the existing job status or create a new one
    job_status, created = Jobstatus.objects.get_or_create(job=job, employee=employee)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        # Debug print should be here, before redirect
        print(f"New status: {new_status}")
        print(f"Job: {job}, Employee: {employee}")
        
        job_status.status = new_status
        job_status.save()
        return redirect('job_details', job_id=job.job_id)
    
    # If it's a GET request, show the form to update the status    
    context = {
        'job': job,
        'employee': employee,
        'job_status': job_status,  # Using the job_status we retrieved/created earlier
    }
    return render(request, 'update_job_status.html', context)

@login_required
def employer_detail(request, employer_id):
    """View for displaying employer details"""
    employer = get_object_or_404(Employer, id=employer_id)
    employer_jobs = employer.created_jobs.all().order_by('-published_on')
    
    context = {
        'employer': employer,
        'employer_jobs': employer_jobs,
    }
    return render(request, 'employer_detail.html', context)

@login_required
def edit_employer(request, employer_id):
    employer = get_object_or_404(Employer, id=employer_id)
    if request.user != employer.user:
        return HttpResponseForbidden("You don't have permission to edit this profile.")
    
    if request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES, instance=employer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('employer_detail', employer_id=employer.id)
    else:
        form = EmployerForm(instance=employer)
    
    context = {
        'form': form,
        'employer': employer,
    }
    return render(request, 'employer_edit.html', context)

@login_required
def delete_employer(request, employer_id):
    """View for deleting employer profile"""
    employer = get_object_or_404(Employer, id=employer_id)
    if request.user != employer.user:
        return HttpResponseForbidden("You don't have permission to delete this profile.")
    
    if request.method == 'POST':
        user = employer.user
        employer.delete()
        messages.success(request, 'Your employer profile has been deleted successfully.')
        return redirect('home')  # Assuming you have a home view
    return redirect('employer_detail', employer_id=employer.id)


#EMPLOYEE VIEWS

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if not form.is_valid():
            print(form.errors)
        else:
            if form.is_valid():
                user = form.save()
                employee = Employee.objects.create(
                    user=user,
                    wo_position=form.cleaned_data['wo_position'],
                    wo_name=form.cleaned_data['wo_name'],
                    wo_gender=form.cleaned_data['wo_gender'],
                    wo_dob=form.cleaned_data['wo_dob'],
                    wo_address=form.cleaned_data['wo_address'],
                    wo_email=form.cleaned_data['wo_email'],
                    wo_phone=form.cleaned_data['wo_phone'],
                    wo_resume=form.cleaned_data['wo_resume']
                )
                login(request, user)
                return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'register_employee.html', {'form': form})

@login_required
def edit_employee(request, wo_id):
    employee = get_object_or_404(Employee, wo_id=wo_id)
    if request.method == 'POST':
        form = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            if 'wo_resume' not in request.FILES:
                form.cleaned_data['wo_resume'] = employee.wo_resume
            form.save()
            return redirect('employee_list')
    else:
        form = EditEmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

@login_required
def delete_employee(request, wo_id):
    employee = get_object_or_404(Employee, wo_id=wo_id)
    if request.user.employee.wo_id != employee.wo_id:
        return HttpResponseForbidden("You don't have permission to delete this profile.")
    if request.method == 'POST':
        employee_name = employee.wo_name
        employee.delete()
        messages.success(request, f'Profile for {employee_name} has been successfully deleted.')
        return redirect('home')  
    return render(request, 'delete_employee_confirmation.html', {'employee': employee})

@login_required
def employee_list(request):
    
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

@login_required
def employee_detail(request,wo_id):
    employee = get_object_or_404(Employee, wo_id=wo_id)
    return render(request, 'employee_detail.html', {'employee': employee})



@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('browse_jobs')  # Redirect to the job list page or another appropriate page
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form})

def delete_job(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('browse_jobs')  # Redirect to the job list page or another appropriate page
    return render(request, 'confirm_delete_job.html', {'job': job})

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    employee = get_object_or_404(Employee, user=request.user)
    addemployer=f'{ job.employer.email }'
    subemployer='New Application Received'
    mesemployer= f"""
    Dear {job.employer.name},

    We are pleased to inform you that a new application has been received for the position of **{job.title}** at **{job.employer.name}**.

    Here are the details of the applicant and the job:

    ### Applicant Details:
    - **Name**: {employee.wo_name}
    - **Email**: {employee.wo_email} 

    ### Job Details:
    - **Position**: {job.title}
    - **Location**: {job.location}
    
    ### Next Steps:
    Please review the application and contact the applicant at {employee.user.email} for further steps.

    Thank you for using our platform to find the best talent for your organization.

    Best regards,
    Your JobSphere Team
    """
    mesemployer = "\n".join(line.strip() for line in mesemployer.split("\n"))   
    ## Email to Employee    
    address = f'{ employee.wo_email }'
    subject = "Application Successful"
    message = f"""
    Dear {employee.wo_name},

    We are pleased to inform you that you have successfully applied for the position of **{job.title}** at **{job.employer.name}**.

    Here are some details about the job and the employer:

    ### About {job.employer.name}:
    {job.employer.description}
    
    ### Job Details:
    - **Position**: {job.title}
    - **Location**: {job.location}
    - **Responsibilities**:
    {job.responsibilities}
    - **Qualifications**:
    {job.qualifications}
    - **Benefits**:
    {job.benefits}

    ### Next Steps:
    Please wait for further communication from {job.employer.name}. If you have any questions, feel free to reach out to them via their website: {job.employer.website} or 
    contact them at {job.employer.email}.

    Thank you for applying, and we wish you the best of luck in your application!

    Best regards,
    The JobSphere Team
    """
    message = "\n".join(line.strip() for line in message.split("\n"))
    if job in employee.wo_applied_jobs.all():
        messages.warning(request, 'You have already applied for this job.')
    else:
        employee.wo_applied_jobs.add(job)
        Jobstatus.objects.create(
            job=job,
            employee=employee,
            status='Applied'
        )
        messages.success(request, 'You have successfully applied for this job.')
        send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
        send_mail(subemployer, mesemployer, settings.EMAIL_HOST_USER, [addemployer])
    
    return redirect('job_details', job_id=job.job_id)

###Resume Creator

from django.shortcuts import render
def reshome(request):
    return render(request, 'resumeindex.html')

def gen_resume(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        about = request.POST.get('about', '')
        age = request.POST.get('age', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skill4 =request.POST.get('skill4', '')
        skill5 =request.POST.get('skill5', '')
        degree1 = request.POST.get('degree1', '')
        college1 = request.POST.get('college1', '')
        year1 = request.POST.get('year1', '')
        degree2 = request.POST.get('degree2', '')
        college2 = request.POST.get('college2', '')
        year2 = request.POST.get('year2', '') 
        college3 = request.POST.get('college3', '')
        year3 = request.POST.get('year3', '')
        degree3 = request.POST.get('degree3', '') 
        lang1 = request.POST.get('lang1', '')
        lang2 = request.POST.get('lang2', '')
        lang3 = request.POST.get('lang3', '')     
        project1= request.POST.get('project1', '')
        durat1 = request.POST.get('duration1', '')
        desc1 = request.POST.get('desc1', '')
        project2 = request.POST.get('project2', '')
        durat2 = request.POST.get('duration2', '')
        desc2 = request.POST.get('desc2', '')
        company1 = request.POST.get('company1', '')
        post1 = request.POST.get('post1', '')
        duration1 = request.POST.get('duration1', '')
        lin11 = request.POST.get('lin11', '')
        company2 = request.POST.get('company2', '')
        post2 = request.POST.get('post2', '')
        duration2 = request.POST.get('duration2', '')
        lin21 = request.POST.get('lin21', '') 
        ach1 = request.POST.get('ach1', '')
        ach2 = request.POST.get('ach2', '')
        ach3 = request.POST.get('ach3', '') 
        return render(request, 'resume.html', {'name':name, 
                                               'about':about, 'skill5':skill5,  
                                               'age':age, 'email':email, 
                                               'phone':phone, 'skill1':skill1,
                                               'skill2':skill2,  'skill3':skill3, 
                                               'skill4':skill4,  'degree1':degree1, 
                                               'college1':college1, 'year1':year1, 
                                               'college3':college3, 'year3':year3, 
                                               'degree3':degree3, 'lang1':lang1, 
                                               'lang2':lang2,  'lang3':lang3,
                                               'degree2':degree2,  'college2':college2, 
                                               'year2':year2, 'project1':project1,
                                               'durat1':durat1, 'desc1':desc1, 
                                               'project2':project2,  'durat2':durat2,
                                               'desc2':desc2, 'company1':company1, 
                                               'post1':post1, 'duration1': duration1, 
                                               'company2':company2, 'post2':post2, 
                                               'duration2': duration2,'lin11':lin11,
                                                'lin21':lin21, 'ach1':ach1,
                                                'ach2':ach2,'ach3':ach3 })
    
    return render(request, 'resumeindex.html')
        
