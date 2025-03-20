from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type=models.CharField(max_length=200,default='Employer')
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    website = models.URLField()
    logo = models.ImageField(upload_to='employer_logo', default='default.jpg')
    email=models.EmailField(default='abinraju63@gmail.com')

    def __str__(self):
        return self.name

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='created_jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    benefits = models.TextField()
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')])
    published_on = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    vacancy = models.PositiveIntegerField()
    category = models.CharField(max_length=100, choices=[
        ('Design & Creative', 'Design & Creative'),
        ('Marketing', 'Marketing'),
        ('Telemarketing', 'Telemarketing'),
        ('Software & Web', 'Software & Web'),
        ('Administration', 'Administration'),
        ('Teaching & Education', 'Teaching & Education'),
        ('Engineering', 'Engineering'),
        ('Garments / Textile', 'Garments / Textile'),
        ('Others', 'Others')
    ])
    experience = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return self.title
