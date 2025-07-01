# common/models.py
from django.db import models
from django.conf import settings
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-code')
    
    def __str__(self):
        return self.name

class Test(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tests')
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Test davomiyligi (daqiqada)")
    
    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    
    def __str__(self):
        return self.text[:50] + "..."

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text

class AssessmentResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    recommendations = models.TextField()
    
    def __str__(self):
        return f"{self.user.username} - {self.test.title} - {self.score}%"

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logos/')
    description = models.TextField()
    website = models.URLField()
    industry = models.CharField(max_length=100)
    employee_count = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    JOB_TYPES = [
        ('full-time', 'To\'liq stavka'),
        ('part-time', 'Yarim stavka'),
        ('remote', 'Masofadan'),
        ('internship', 'Internship'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=JOB_TYPES)
    posted_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    is_featured = models.BooleanField(default=False)
    is_for_interns = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} at {self.company.name}"

