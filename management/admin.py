from django.contrib import admin
from .models import PaymentMotif, PatientDepartments, Prescriptions, Cashier, PrincipalReceptionist, ServiceReceptionist, Parameters, Departments, Doctors, Patients, Appointments, Registration, DoctorsSchedule, Payments
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user' , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation']
    search_fields = ('first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user' , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

class ServiceReceptionistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user', 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation' ]
    search_fields = ('first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user', 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'principal_receptionist', 'has_paid', 'marital_status', 'location', 'profession', 'date_creation']
    search_fields = ('first_name', 'last_name', 'principal_receptionist', 'has_paid','marital_status', 'location', 'profession', 'date_creation')

class ParametersAdmin(admin.ModelAdmin):
    list_display = ['blood_pressure', 'pulse', 'breathing_rate', 'heart_rate', 'weight', 'height', 'blood_sugar', 'temperature', 'department', 'service_receptionist', 'patient', 'date_creation']
    search_fields = ('blood_pressure', 'pulse', 'breathing_rate', 'heart_rate', 'weight', 'height', 'blood_sugar', 'temperature', 'department', 'service_receptionist', 'patient' , 'date_creation')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['date_appointment', 'patient', 'service_receptionist', 'doctor', 'state', 'date_creation']
    search_fields = ('date_appointment', 'patient', 'service_receptionist', 'doctor', 'state', 'date_creation')

class PatientDepartmentsAdmin(admin.ModelAdmin):
    list_display = [ 'patient', 'department']
    search_fields = ( 'patient', 'department')



class PrincipalReceptionnistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_active', 'activate_by_admin', 'user'  , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation' ]
    search_fields = ('first_name', 'last_name', 'is_active', 'activate_by_admin', 'user' , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

class CashierAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_active', 'activate_by_admin', 'user'  , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation' ]
    search_fields = ('first_name', 'last_name', 'is_active', 'activate_by_admin', 'user' , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

    
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['cashier', 'patient', 'department', 'motif', 'amount', 'payment_method']
    search_fields = ('cashier', 'patient', 'department' 'motif', 'amount', 'payment_method')

class PaymentMotifAdmin(admin.ModelAdmin):
    list_display = ['payment_motif', 'amount_motif', 'durée_en_jours']
    search_fields = ('payment_motif', 'amount_motif', 'durée_en_jours')

    
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'symptoms', 'drug_prescription', 'examinations', 'recommendations', 'prescripted_date']
    search_fields = ('patient', 'doctor', 'symptoms', 'drug_prescription', 'examinations', 'recommendations', 'prescripted_date')

admin.site.register(Departments)
admin.site.register(Doctors, DoctorAdmin)
admin.site.register(ServiceReceptionist, ServiceReceptionistAdmin)
admin.site.register(PrincipalReceptionist, PrincipalReceptionnistAdmin)
admin.site.register(Patients, PatientAdmin)
admin.site.register(Appointments, AppointmentAdmin)
admin.site.register(Registration)
admin.site.register(DoctorsSchedule)
admin.site.register(Payments, PaymentsAdmin)
admin.site.register(Parameters, ParametersAdmin)
admin.site.register(Cashier, CashierAdmin)
admin.site.register(Prescriptions, PrescriptionAdmin)
admin.site.register(PaymentMotif, PaymentMotifAdmin)
admin.site.register(PatientDepartments, PatientDepartmentsAdmin)

