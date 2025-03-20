from django.db import models
from django.contrib.auth.models import User
from employer.models import Job

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=0)
    type = models.CharField(max_length=200,default='Employee')
    wo_id=models.AutoField(primary_key=True)
    wo_name=models.CharField(max_length=200)
    wo_position=models.CharField(max_length=200)
    wo_email=models.EmailField()
    wo_phone=models.CharField(max_length=200,default='1234567890')
    wo_resume=models.FileField(upload_to='employee_resume',default='default.pdf')
    wo_gender=models.CharField(max_length=200,choices=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ])
    wo_dob=models.DateField()
    wo_address=models.TextField()
    wo_applied_jobs=models.ManyToManyField('employer.Job', related_name='applied_jobs',default=None)
    
    def __str__(self):
        
        return self.wo_name

class Jobstatus(models.Model):
    status = models.CharField(max_length=200, choices=[
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected')
    ], default='Applied')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_statuses')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='job_statuses')
    
    def __str__(self):
        return f"{self.employee.wo_name} - {self.job.title} - {self.status}"