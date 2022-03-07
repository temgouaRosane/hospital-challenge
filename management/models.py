from email.policy import default
from enum import unique
from tkinter import S
from django.db import models
from django.conf import settings
from django.db.models.fields import BooleanField
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.

    


class Departments(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(default=" ")
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('management:nom_service', kwargs={
            'pk': self.pk
        })
    
    def get_absolute_url3(self):
        return reverse('management:department_principal_receptionist', kwargs={
            'pk': self.pk
        })
    def get_absolute_url4(self):
        return reverse('management:patient_department_principal_receptionist', kwargs={
            'pk': self.pk
        })
    def get_absolute_url5(self):
        return reverse('management:department_cashier', kwargs={
            'pk': self.pk
        })

class PrincipalReceptionist(models.Model):
    GENDER = (
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN'),
        
    )
    MARITALSTATUS = (
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        
    )
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    is_active = BooleanField(default=False) #________________________________________________________________________________________________________________________le docteur va renseigner ici s'il est actif ou pas
    activate_by_admin = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=GENDER)
    marital_status = models.CharField(max_length=8, choices=MARITALSTATUS)
    date_of_birth = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    location = models.CharField(max_length = 230)
    description = models.TextField(null = True, blank = True)
    profile = models.ImageField(null = True, blank = True)
    date_creation = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('management:doctors_profile', kwargs={
            'pk': self.pk
        })

class Cashier(models.Model):
    GENDER = (
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN'),
        
    )
    MARITALSTATUS = (
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        
    )
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    is_active = BooleanField(default=False) #________________________________________________________________________________________________________________________le docteur va renseigner ici s'il est actif ou pas
    activate_by_admin = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=GENDER)
    marital_status = models.CharField(max_length=8, choices=MARITALSTATUS, default="SINGLE")
    date_of_birth = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    location = models.CharField(max_length = 230)
    description = models.TextField(null = True, blank = True)
    profile = models.ImageField(null = True, blank = True)
    date_creation = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('management:doctors_profile', kwargs={
            'pk': self.pk
        })


    
    
class Doctors(models.Model):
    GENDER = (
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN'),
        
    )
    MARITALSTATUS = (
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        
    )
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    is_active = BooleanField(default=False) #________________________________________________________________________________________________________________________le docteur va renseigner ici s'il est actif ou pas
    activate_by_admin = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=GENDER)
    marital_status = models.CharField(max_length=8, choices=MARITALSTATUS, default="SINGLE")
    date_of_birth = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    location = models.CharField(max_length = 230)
    department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    description = models.TextField(null = True, blank = True)
    profile = models.ImageField(null = True, blank = True)
    date_creation = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('management:doctors_profile', kwargs={
            'pk': self.pk
        })

    def  get_absolute_url2(self):
        return reverse('management:doctors_appointments1', kwargs={
            'pk': self.pk
        })
    
    def  get_absolute_url3(self):
        return reverse('management:doctors_patients', kwargs={
            'pk': self.pk
        })

    def  get_absolute_url4(self):
        return reverse('management:doctors_prescriptions', kwargs={
            'pk': self.pk
        })

    def  get_absolute_url5(self):
        return reverse('management:doctors_makePrescription', kwargs={
            'pk': self.pk
        })
    
    
    


class ServiceReceptionist(models.Model):
    GENDER = (
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN'),
        
    )
    MARITALSTATUS = (
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        
    )
    
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    is_active = BooleanField(default=False) #________________________________________________________________________________________________________________________le docteur va renseigner ici s'il est actif ou pas
    activate_by_admin = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=GENDER)
    marital_status = models.CharField(max_length=8, choices=MARITALSTATUS, default="SINGLE")
    date_of_birth = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    location = models.CharField(max_length = 230)
    department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    description = models.TextField(null = True, blank = True)
    profile = models.ImageField(null = True, blank = True)
    date_creation = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self, g):
        return reverse('management:doctors_profile', kwargs={
            'pk': self.pk
        })




class Registration(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    duty = models.CharField(max_length = 200)
    ward_no = models.CharField(max_length = 200)
    date = models.CharField(max_length = 200)
    
    def __str__(self):
        return f"{self.doctor} - {self.duty}"




class Patients(models.Model):
    MARITALSTATUS = (
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        
    )
    GENDER = (
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN'),
        
    )
    principal_receptionist = models.ForeignKey(PrincipalReceptionist, on_delete = models.CASCADE, null=True) #ajouté_______________________________________________________________
    #ajouter les principal receptionist
    first_name = models.CharField(max_length = 200, null = True, blank = True)
    last_name = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 200, null = True, blank = True)
    emergency_phone = models.CharField(max_length = 200, null = True, blank = True)
    marital_status = models.CharField(max_length=8, choices=MARITALSTATUS, default="SINGLE")
    gender = models.CharField(max_length=5, choices=GENDER)
    date_of_birth = models.CharField(max_length = 200, null = True, blank = True)
    email = models.CharField(max_length = 200, null = True, blank = True)
    location = models.CharField(max_length = 230, null = True, blank = True)
    profile = models.ImageField(null = True, blank = True)
    profession = models.CharField(max_length = 200, null = True, blank = True)#à remplacer par work ou job
    id_number = models.CharField(max_length = 200, null = True, blank = True)
    date_creation = models.DateTimeField(auto_now_add=True)
    has_paid = BooleanField(default=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('management:patients_profile', kwargs={
            'pk': self.pk
        })
    
    
    def get_absolute_url3(self):
        return reverse('management:parametres_profile', kwargs={
            'pk': self.pk
        })

    def get_absolute_url4(self):
        return reverse('management:other_profile', kwargs={
            'pk': self.pk
        })
    def get_absolute_url5(self):
        return reverse('management:informations', kwargs={
            'pk': self.pk
        })
    

class PatientDepartments(models.Model):
    department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete = models.CASCADE)
    def get_absolute_url2(self):
       
        return reverse('management:add_payment_patient_department_cashier', kwargs={
            'pk': self.pk,
            
        })
    


class Parameters(models.Model):
    department = models.ForeignKey(Departments, on_delete = models.CASCADE) #Pas besoin. Voir comment supprimer_______________________________________________________________
    service_receptionist = models.ForeignKey(ServiceReceptionist, on_delete = models.CASCADE, null = True) #ajouté_______________________________________________________________
    patient = models.ForeignKey(Patients, on_delete = models.CASCADE)
    blood_pressure = models.CharField(max_length = 200, null = True, blank = True)
    pulse = models.CharField(max_length = 200, null = True, blank = True)
    breathing_rate = models.CharField(max_length = 200, null = True, blank = True)
    heart_rate = models.CharField(max_length = 200, null = True, blank = True)
    #haemoglobin = models.CharField(max_length = 200, null = True, blank = True)
    weight = models.CharField(max_length = 200, null = True, blank = True) 
    height = models.CharField(max_length = 200, null = True, blank = True) 
    blood_sugar = models.CharField(max_length = 200, null = True, blank = True)
    temperature = models.CharField(max_length = 200, null = True, blank = True)
    other = models.TextField(null = True, blank = True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    
    
    
     #___________________________________________________________________relier appointments, patients et service    
#patient = models.ForeignKey(Patients, on_delete = models.CASCADE)
#department = models.ForeignKey(Departments, on_delete = models.CASCADE)
#date et heure aussi
class Appointments(models.Model):
    date_appointment = models.DateField()
    hour_appointment = models.CharField(max_length=9999999999, default='00:00')
    patient = models.ForeignKey(Patients, on_delete = models.CASCADE)
    department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    service_receptionist = models.ForeignKey(ServiceReceptionist, on_delete = models.PROTECT, null=True) #ajouté_______________________________________________________________
    doctor = models.ForeignKey(Doctors, on_delete = models.CASCADE) #ajouté_______________________________________________________________
    date_creation = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=9999999999, default='Non consulté')
    #def __str__(self):
     #   return f"{self.first_name} {self.last_name}"
    def get_absolute_url(self):
        return reverse('management:other_profile', kwargs={
            'pk': self.pk
        })
    def  get_absolute_url8(self):
        return reverse('management:doctorMakePrescriptions', kwargs={
            'pk': self.pk
        })
    
class Prescriptions(models.Model):
    patient = models.ForeignKey(Patients, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete = models.CASCADE)
    appointment = models.ForeignKey(Appointments, on_delete = models.CASCADE) #ajouté_______________________________________________________________
    symptoms = models.TextField(max_length=999999)
    drug_prescription = models.TextField(max_length=999999, null=True)
    examinations = models.TextField(max_length=999999, null=True)
    recommendations = models.TextField(max_length=999999, null=True)
    prescripted_date = models.DateTimeField(auto_now_add=True)
    
    
    def  get_absolute_url(self):
        return reverse('management:get_pdf', kwargs={
            'pk1': self.pk
        })
    def  get_absolute_url2(self):
        return reverse('management:view_prescription_patient', kwargs={
            'pk': self.pk
        })
class DoctorsSchedule(models.Model):
    date = models.DateField()
    event = models.TextField()
    
    def __str__(self):
        return f"{self.event} {self.date}"
    
class PaymentMotif(models.Model):
    payment_motif = models.CharField(max_length = 999999, unique=True)
    amount_motif = models.CharField(max_length = 999999)
    durée_en_jours = models.CharField(max_length = 999999)
    def __str__(self):
        return f"{self.payment_motif} {self.amount_motif}F"

class Payments(models.Model):
    cashier = models.ForeignKey(Cashier, on_delete = models.PROTECT)
    patient = models.ForeignKey(Patients, on_delete = models.CASCADE)
    department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    motif = models.ForeignKey(PaymentMotif, on_delete = models.PROTECT)
    amount = models.CharField(max_length = 999999)
    
    payment_method = models.CharField(max_length = 999999)
    
    def __str__(self):
        return f"{self.pk} {self.patient}"
    
    def get_absolute_url(self):
        return reverse('management:payment_receipt_cashier', kwargs={
            'pk': self.pk
        })