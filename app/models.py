from django.db import models

# Create your models here.

class CustomUser(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(null= True)    
    

    LOGIN_CHOICES =(
        ('ADMIN', 'Admin'),
        ('PATIENT', 'Patient'),
        ('NURSE', 'Nurse'),
    )
    login = models.CharField(max_length=7, choices=LOGIN_CHOICES)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.email


class Patient(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)
    phone_number = models.TextField(max_length=20, null=True, blank=False)
    city = models.CharField(max_length=50, null = True, blank=True)
    street = models.TextField(max_length=100, null=True, blank=False)
    national_image = models.ImageField() 

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(max_length=50)
    

    DEGREE_CHOICES = (
        ('A', 'Associate Degree in Nursing'),
        ('D', 'Diploma in Nursing'),
        ('L', 'Licensed Practical Nurse'),
        ('AD', 'Advanced practice registered nurses'),
    )
    degree = models.CharField(max_length=7, choices=DEGREE_CHOICES)

    SEPCIALTY_CHOICES = (
        ('1', 'قسم تمريض الباطني والجراحي'),
        ('2', 'قسم تمريض العناية الحرجة والطوارئ'),
        ('3', 'قسم تمريض النسا والتوليد'),
        ('4', 'قسم تمريض الأطفال'),
        ('5', 'قسم التمريض النفسي والصحة العقلية'),
        ('6', 'قسم إدارة التمريض'),
        ('7', 'قسم تمريض المسنين'),
        ('8', 'قسم تمريض صحة المجتمع')
    )
    

    specialty = models.CharField(max_length=50, null=True, blank=True, choices=SEPCIALTY_CHOICES )

    
    GRADE_CHOICES = (
        ('1', 'Pass'),
        ('2', 'Good'),
        ('3', 'Verygood'),
        ('4', 'Excellent'),
        ('5', 'Superior'),


    )

    university_grade = models.CharField(max_length=10, choices=GRADE_CHOICES)


    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)



    def __str__(self):
        return self.name


class reservation(models.Model):

    SEPCIALTY_CHOICES = (
        ('1', 'قسم تمريض الباطني والجراحي'),
        ('2', 'قسم تمريض العناية الحرجة والطوارئ'),
        ('3', 'قسم تمريض النسا والتوليد'),
        ('4', 'قسم تمريض الأطفال'),
        ('5', 'قسم التمريض النفسي والصحة العقلية'),
        ('6', 'قسم إدارة التمريض'),
        ('7', 'قسم تمريض المسنين'),
        ('8', 'قسم تمريض صحة المجتمع')
    )
    specialty = models.CharField(max_length=50, null=True, blank=True, choices=SEPCIALTY_CHOICES)
    
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Visit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    comments = models.TextField()
    rate = models.FloatField(max_length=10, null = True, blank=True)

    def __str__(self):
        return self.reason
    

class Appointment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    satuts = models.BooleanField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __bol__(self):
        return self.satuts


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.service_name


class Task(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    last_task = models.CharField(max_length=200, null = True, blank=True)
    now_task = models.CharField(max_length=200, null = True, blank=True)
    next_task = models.CharField(max_length=200, null = True, blank=True)

    def __str__(self):
        return self.now_task
    
