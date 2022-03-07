
from asyncio.windows_events import NULL
import datetime
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from http.client import HTTPResponse
from io import BytesIO
from django.db.models.base import Model
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from .models import Cashier, PaymentMotif, PatientDepartments, Prescriptions, Departments, Doctors, Parameters, Patients, Appointments, Payments, PrincipalReceptionist, ServiceReceptionist
import random as r
from django.db.models import Q
from django.template.loader import get_template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def verifyActiveOrNot(staff):
    if staff.is_active==False:
        return False
    else:
        return True
def home(request):
    
    try:
        if request.user.username == ServiceReceptionist.objects.get(user=request.user).user.username:
            department = searchDepartment(request, ServiceReceptionist)
            patientCount = PatientDepartments.objects.filter(department = department).count()
            doctorCount = Doctors.objects.filter(department = department).count()
            serviceReceptionistCount = ServiceReceptionist.objects.filter(department = department).count()
            service_receptionist = ServiceReceptionist.objects.get(user=request.user)
            
            youAreActive = verifyActiveOrNot(service_receptionist)
                
               

            if request.method == 'POST':
                is_active = request.POST.get('is_active')
                
                if is_active == "True":
                    service_receptionist.is_active=True
                    service_receptionist.save()
                    youAreActive = True
                else:
                    service_receptionist.is_active=False
                    service_receptionist.save()
                    youAreActive = False
            
            departments = Departments.objects.all()
            work='Service receptionist'
            context = {
                'departments':departments,
                'work':work,
                'service_receptionist':service_receptionist,
                'patientCount':patientCount,
                'serviceReceptionist':service_receptionist,
                'user_department':department,
                'youAreActive':youAreActive,
                'serviceReceptionistCount':serviceReceptionistCount,
                'doctorCount':doctorCount
            }
        return render(request, 'management/serviceReceptionist/index.html', context)
        
    except Exception:


        try:
            if request.user.username == PrincipalReceptionist.objects.get(user=request.user).user.username:
                principal_receptionist = PrincipalReceptionist.objects.get(user=request.user)
                
                youAreActive = verifyActiveOrNot(principal_receptionist)

                if request.method == 'POST':
                    is_active = request.POST.get('is_active')
                    
                    if is_active == "True":
                        principal_receptionist.is_active=True
                        principal_receptionist.save()
                        youAreActive = True
                    else:
                        principal_receptionist.is_active=False
                        principal_receptionist.save()
                        youAreActive = False
                        
                departments = Departments.objects.all()
                work='Principal receptionist'
                context = {
                    'principal_receptionist':principal_receptionist,
                    'departments':departments,
                    'work':work,
                    'youAreActive':youAreActive,
                    'principalReceptionist':principal_receptionist
                }
            return render(request, 'management/principalReceptionist/index_principal_receptionist.html', context)
            
        except Exception:
            try:
                if request.user.username == Cashier.objects.get(user=request.user).user.username:
                    cashier = Cashier.objects.get(user=request.user)
                    
                    youAreActive = verifyActiveOrNot(cashier)

                    if request.method == 'POST':
                        is_active = request.POST.get('is_active')
                        
                        if is_active == "True":
                            cashier.is_active=True
                            cashier.save()
                            youAreActive = True
                        else:
                            cashier.is_active=False
                            cashier.save()
                            youAreActive = False
                    
                    departments = Departments.objects.all()
                    work='Cashier'
                    context = {
                        'cashier':cashier,
                        'departments':departments,
                        'work':work,
                        'cashier':cashier,
                        'youAreActive':youAreActive
                    }
                return render(request, 'management/cashier/index_cashier.html', context)
            
            except Exception as e:
                print(e)
                try:
                    if request.user.username == Doctors.objects.get(user=request.user).user.username:
                        doctor = Doctors.objects.get(user=request.user)
                        department = searchDepartment(request, Doctors)
                        patientCount = PatientDepartments.objects.filter(department = department).count()
                        doctorCount = Doctors.objects.filter(department = department).count()
                        serviceReceptionistCount = ServiceReceptionist.objects.filter(department = department).count()
            
                        youAreActive = verifyActiveOrNot(doctor)

                        if request.method == 'POST':
                            is_active = request.POST.get('is_active')
                            
                            if is_active == "True":
                                doctor.is_active=True
                                doctor.save()
                                youAreActive = True
                            else:
                                doctor.is_active=False
                                doctor.save()
                                youAreActive = False
                            
                        departments = Departments.objects.all()
                        work='Doctor'
                        context = {
                            'departments':departments,
                            'work':work,
                            'doctor':doctor,
                            'youAreActive':youAreActive,
                            'serviceReceptionistCount':serviceReceptionistCount,
                            'doctorCount':doctorCount,
                            'patientCount':patientCount,
                            'user_department':department
                        }
                    return render(request, 'management/doctor/profile1.html', context)
                except Exception as e:
                    print(e)
                        
    return render(request, 'management/index_accueil.html')

        

#****************************************VUES LIES A LA RECEPTIONNISTE DU SERVICE********************************************************#
def doctors(request):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    doctors = Doctors.objects.all()
    context = {
        'doctors': doctors,
        'user_department':searchDepartment(request, Doctors),
        'youAreActive':youAreActive,
        'work':"Service receptionist",
    }
    return render(request, 'management/serviceReceptionist/doctors.html', context)


def searchDepartment(request, model):
    try:
        user_department = model.objects.get(user=request.user).department
    except:
        user_department = 'No department'
    return user_department


    

    
def department(request):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    patients = Patients.objects.all().count()
    return render(request, 'management/serviceReceptionist/department.html',{'patients':patients})



def department_doctors(request): 
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    department = searchDepartment(request, ServiceReceptionist)
    doctors = Doctors.objects.filter(department = department)
    
    context = {
        'doctors': doctors,
        'service_receptionist': service_receptionist,
        'user_department':department,
        'youAreActive':youAreActive,
        'work':"Service receptionist"
    }
    return render(request, 'management/serviceReceptionist/department_doctors.html', context)

################################ceci n'est pas fini#####################################################
#
#
# 
def department_receptionist(request): 
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    department = searchDepartment(request, ServiceReceptionist)
    doctors = Doctors.objects.filter(department = department)
    
    context = {
        'doctors': doctors,
        'service_receptionist': service_receptionist,
        'user_department':department,
        'youAreActive':youAreActive,
        'work':"Service receptionist"
    }
    return render(request, 'management/serviceReceptionist/department_doctors.html', context)

def receptionist_profile(request, pk):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    doctor = Doctors.objects.get(pk=pk)
    appointments = Appointments.objects.filter(doctor = doctor)
    prescriptions = Prescriptions.objects.filter(doctor = doctor)
    context = {
        'doctor': doctor,
        'service_receptionist': service_receptionist,
        'appointments': appointments,
        'prescriptions': prescriptions,
        'user_department':searchDepartment(request, ServiceReceptionist),
        'youAreActive':youAreActive,
        'work':"Service receptionist",
    }
    return render(request, 'management/serviceReceptionist/profile.html', context)
#
#
# 
#####################################################################################################################

#def department_patients(request):
 #   service_receptionist = ServiceReceptionist.objects.get(user=request.user)
  #  youAreActive = verifyActiveOrNot(service_receptionist)
   # patients = Patients.objects.filter(department = service_receptionist.department)
    #context = {
     #   'patients': patients,
      #  'user_department':searchDepartment(request,ServiceReceptionist),
       # 'youAreActive':youAreActive,
        #'work':"Service receptionist",
    #}
    #return render(request, 'management/department_patients.html', context)


def doctors_profile(request, pk):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    doctor = Doctors.objects.get(pk=pk)
    appointments = Appointments.objects.filter(doctor = doctor)
    prescriptions = Prescriptions.objects.filter(doctor = doctor)
    context = {
        'doctor': doctor,
        'service_receptionist': service_receptionist,
        'appointments': appointments,
        'prescriptions': prescriptions,
        'user_department':searchDepartment(request, ServiceReceptionist),
        'youAreActive':youAreActive,
        'work':"Service receptionist",
    }
    return render(request, 'management/serviceReceptionist/profile.html', context)


def me(request, NomBD):
    me = NomBD.objects.get(user=request.user)
    
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        maritalStatus = request.POST.get('marital_status')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')
        #ajouer marital_status, proche_phone, age, location et profession
        
        location = request.POST.get('location')
        profile = request.POST.get('profile')
        
        try:
            with transaction.atomic():
               me.first_name = first_name
               me.last_name = last_name
               me.phone = phone
               me.gender = gender
               me.date_of_birth = date_of_birth
               me.email = email
               me.marital_status = maritalStatus
               me.location = location
               me.profile = profile
               me.description = description
               me.save()
               message = "Succesfully save"
        except IntegrityError:
                message = "Une erreur interne est apparue. Merci de recommencer votre requête."       
        return message


def me_service_receptionist(request):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    context = {
        'service_receptionist': service_receptionist,
        'user_department': searchDepartment(request, ServiceReceptionist),
        'youAreActive': youAreActive,
        'work': "Service receptionist",
    }
    if request.method == 'POST':
        context['message'] = me(request, ServiceReceptionist)
        return redirect('management:home')
    
    return render(request, 'management/serviceReceptionist/me_service_receptionist.html', context)


def patients(request):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    patients = PatientDepartments.objects.filter(department = service_receptionist.department)
    parameters = Parameters.objects.all()
    context = {
        'parameters': parameters,
        'service_receptionist': service_receptionist,
        'patients': patients,
        'user_department':searchDepartment(request, ServiceReceptionist),
        'youAreActive':youAreActive,
        'work':"Service receptionist",
    }
    return render(request, 'management/serviceReceptionist/patients.html', context)

def parametres_profile(request, pk):#AJOUTER LES TRANSACTIONS___________________________________________________________________
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    patient = Patients.objects.get(pk=pk)
    department = searchDepartment(request, ServiceReceptionist)
    context = {
        'patient':patient,
         'pk':pk,
         'service_receptionist': service_receptionist,
        'user_department':department,
        'youAreActive':youAreActive,
        'work':"Service receptionist",
    }

    if request.method == 'POST':
        try:
            with transaction.atomic(): 
                blood_pressure = request.POST.get('blood_pressure')
                pulse = request.POST.get('pulse')
                breathing_rate = request.POST.get('breathing_rate')
                heart_rate = request.POST.get('heart_rate')
                weight = request.POST.get('weight')
                height = request.POST.get('height')
                blood_sugar = request.POST.get('blood_sugar')
                temperature = request.POST.get('temperature')
                other = request.POST.get('other')
                
            
                Parameters.objects.create(  
                    department = department,
                    service_receptionist = service_receptionist,
                    patient = patient,  
                    blood_pressure = blood_pressure,
                    pulse = pulse,
                    breathing_rate = breathing_rate,
                    heart_rate = heart_rate,
                    weight = weight,
                    height = height,
                    blood_sugar = blood_sugar,
                    temperature = temperature,
                    other = other
                )
                message = "Succesfully save"
        except IntegrityError:
                message = "Une erreur interne est apparue. Merci de recommencer votre requête."       
        context['message'] = message
                
    return render(request, 'management/serviceReceptionist/parametres-profile.html', context)

def pagination(request, list, number, nameOfPageInHTML):
    paginator = Paginator(list, number)
    page = request.GET.get(nameOfPageInHTML)
    try:
        currentPage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        currentPage = paginator.page(1)
    except EmptyPage:
        currentPage = paginator.page(paginator.num_pages)
    return currentPage

def schedule(request):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    department = searchDepartment(request, ServiceReceptionist)
    appointments_list = Appointments.objects.filter(service_receptionist = service_receptionist).order_by('-state', 'date_appointment', 'hour_appointment')
    allAppointments_list = Appointments.objects.filter(department = department).order_by('-state', 'date_appointment')
    allAppointments = pagination(request, allAppointments_list, 15, 'pageAll')
    appointments = pagination(request, appointments_list, 15, 'page')

    context = {
        'allAppointments': allAppointments,
        'service_receptionist': service_receptionist,
        'paginate': True,
        'appointments': appointments,
        'user_department':department,
        'youAreActive':youAreActive,
        'work':"Service receptionist",
    }
    return render(request,'management/serviceReceptionist/doctor-schedule.html', context )


def appointment(request):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    
    youAreActive = verifyActiveOrNot(service_receptionist)
    patients = PatientDepartments.objects.filter(department=service_receptionist.department)
    doctors = Doctors.objects.filter(department=service_receptionist.department)
    context = {
        'doctors':doctors,
        'service_receptionist': service_receptionist,
        'current_date': datetime.datetime.now().date().__str__(),
        'max_date': (datetime.datetime.now().date() + datetime.timedelta(days=14)).__str__(),
        'patients': patients,
        'user_department':searchDepartment(request, ServiceReceptionist),
        'youAreActive':youAreActive,
        'work':"Service receptionist",
    }
    if request.method == 'POST':
        try:
            with transaction.atomic():
                patient = Patients.objects.get(pk=request.POST.get('patient'))
                doctor = request.POST.get('doctor')
                date = request.POST.get('date')
                hour = request.POST.get('hour')
                
                Appointments.objects.create(
                    
                    doctor = Doctors.objects.get(pk=doctor),
                    patient = patient,
                    date_appointment = date,
                    hour_appointment = hour,
                    department = service_receptionist.department,
                    service_receptionist = service_receptionist
                )
                message = "Successfully created"
                return redirect('management:schedule')
                
        except IntegrityError:
                message = "Une erreur interne est apparue. Merci de recommencer votre requête."       
        context['message'] = message    
    
    
    return render(request,'management/serviceReceptionist/book-appointment.html', context )

def other(request, pk):
    service_receptionist = ServiceReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(service_receptionist)
    patient = Patients.objects.get(pk=pk)
    #parameters = Parameters.objects.filter(service_receptionist__isnull = False)
    appointments = Appointments.objects.filter(patient = patient)
    parameters = Parameters.objects.filter(Q(patient = patient),
                                            Q(service_receptionist__isnull = False)
                                            )
    
    context = {
        'patient':patient,
        'service_receptionist': service_receptionist,
        'appointments': appointments,
        'parameters':parameters,
        'user_department':searchDepartment(request, ServiceReceptionist),
        'youAreActive':youAreActive,
        'work':"Service receptionist",
    }
    return render(request, 'management/serviceReceptionist/other.html', context)
def search(request):
    if request.method == 'POST':
        results = request.POST.get('search')
        patients = Patients.objects.filter(first_name__icontains = results)
        if patients is None:
            patients = Patients.objects.filter(last_name__icontains = results).order_by('date_creation')
        context = {
            'patients':patients,
            'work':"Service receptionist",
        }
    return render(request, 'management/search_results.html',context)

#****************************************FIN VUES LIES A LA RECEPTIONNISTE DU SERVICE********************************************************#

#****************************************VUES LIES A LA RECEPTIONNISTE PRINCIPALE*************************************************************#
def me_principal_receptionist(request):
    principal_receptionist = PrincipalReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(principal_receptionist)
    context = {
        'principal_receptionist': principal_receptionist,
        'user_department': searchDepartment(request, PrincipalReceptionist),
        'youAreActive': youAreActive,
        'work': "Principal receptionist",
    }
    if request.method == 'POST':
        context['message'] = me(request, PrincipalReceptionist)
        return redirect('management:home')
    
    return render(request, 'management/principalReceptionist/me_principal_receptionist.html', context)

def department_add_patients_accueil(request):
    principal_receptionist = PrincipalReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(principal_receptionist)
    departments = Departments.objects.all()
    context = {
        'principal_receptionist': principal_receptionist,
        'youAreActive':youAreActive,
        'work':"Principal receptionist",
        "departments":departments
    }
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                depart = Departments.objects.get(id=request.POST.get('department'))  
                profile = request.POST.get('profile')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                date_of_birth = request.POST.get('date_of_birth')
                gender = request.POST.get('gender')
                maritalStatus = request.POST.get('marital_status')
                phone = request.POST.get('phone')
                emergencyPhone = request.POST.get('emergency_phone')
                email = request.POST.get('email')
                profession = request.POST.get('profession')
                location = request.POST.get('location')
                
                
                id_number = r.randint(9999, 1000000)
                
                #mettre l'erreur______________________________________________________________________
                #mettre le cas d'erreur_______________________________________________________________
                
                Patients.objects.create(
                    principal_receptionist = principal_receptionist,
                    first_name = first_name,
                    last_name = last_name,
                    phone = phone,
                    emergency_phone = emergencyPhone,
                    gender = gender,
                    date_of_birth = date_of_birth,
                    email = email,
                    marital_status = maritalStatus,
                    location = location,
                    profession = profession,
                    profile = profile,
                    id_number = 'POLYCLINIC' + str(id_number)
                )
                PatientDepartments.objects.create(
                    patient = Patients.objects.get(id_number= 'POLYCLINIC' + str(id_number)),
                    department = depart
                )
                
                Parameters.objects.create(
                    
                    department = depart,
                    patient = Patients.objects.get(id_number='POLYCLINIC' + str(id_number)),
                    blood_pressure = 'null',
                    pulse = 'null',
                    breathing_rate = 'null',
                    heart_rate = 'null',
                    weight = 'null',
                    height = 'null',
                    blood_sugar = 'null',
                    temperature = 'null',
                    other = 'null',
                
                )
                message = "succesfully add"
        except IntegrityError:
                message = "Une erreur interne est apparue. Merci de recommencer votre requête."       
        context['message'] = message


    
    
    return render(request, 'management/principalReceptionist/department_add_patients.html', context)

def patients_profile_accueil(request, pk):
    principal_receptionist = PrincipalReceptionist.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(principal_receptionist)
    patient = Patients.objects.get(pk=pk)
    context = {
        'principal_receptionist': principal_receptionist,
        'patient':patient,
         'pk':pk,
        'youAreActive':youAreActive,
        'work':"Principal receptionist",
    }
    

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        maritalStatus = request.POST.get('marital_status')
        phone = request.POST.get('phone')
        emergencyPhone = request.POST.get('emergency_phone')
        email = request.POST.get('email')
        #ajouer marital_status, proche_phone, age, location et profession
        profession = request.POST.get('profession')
        location = request.POST.get('location')
        profile = request.POST.get('profile')
        
    
        patient.first_name = first_name
        patient.last_name = last_name
        patient.phone = phone
        patient.emergency_phone = emergencyPhone
        patient.gender = gender
        patient.date_of_birth = date_of_birth
        patient.email = email
        patient.marital_status = maritalStatus
        patient.location = location
        patient.profession = profession
        patient.profile = profile
        patient.save()
        
       

    return render(request, 'management/principalReceptionist/patient-profile.html', context)


def departmentPrincipalReceptionist(request, pk):
    principal_receptionist = PrincipalReceptionist.objects.get(user=request.user)
    department = Departments.objects.get(pk=pk)
    serviceReceptionists_list = ServiceReceptionist.objects.filter(department = department)
    doctors_list = Doctors.objects.filter(department = department)
    youAreActive = verifyActiveOrNot(principal_receptionist)
    doctors = pagination(request, doctors_list, 15, 'pageD')
    serviceReceptionists = pagination(request, serviceReceptionists_list, 15, 'pageS')
    context = {
        'principal_receptionist': principal_receptionist,
        'department':department,
        'pk':pk,
        'paginate': True,
        'doctors': doctors,
        'serviceReceptionists': serviceReceptionists,
        'youAreActive':youAreActive,
        'work':"Principal receptionist",
    }
    return render(request, 'management/principalReceptionist/department_principal_receptionist.html', context)

def patientDepartmentPrincipalReceptionist(request, pk):
    principal_receptionist = PrincipalReceptionist.objects.get(user=request.user)
    department = Departments.objects.get(pk=pk)
    patients_list = PatientDepartments.objects.filter(department = department)#******************************modifier************************************************
    patients = pagination(request, patients_list, 15, 'pageP')
    youAreActive = verifyActiveOrNot(principal_receptionist)
    
    context = {
        'principal_receptionist': principal_receptionist,
        'department':department,
        'pk':pk,
        'paginate': True,
        'patients': patients,
        'youAreActive':youAreActive,
        'work':"Principal receptionist",
    }
    return render(request, 'management/principalReceptionist/patient_department_principal_receptionist.html', context)

#****************************************FIN VUES LIES A LA RECEPTIONNISTE PRINCIPALE*********************************************************#

#****************************************VUES LIES A LA CAISSIERE*************************************************************#
def me_cashier(request):
    cashier = Cashier.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(cashier)
    context = {
        'cashier': cashier,
        'user_department': searchDepartment(request, Cashier),
        'youAreActive': youAreActive,
        'work': "Principal receptionist",
    }
    if request.method == 'POST':
        context['message'] = me(request, Cashier)
        return redirect('management:home')
    
    return render(request, 'management/cashier/me_cashier.html', context)

def departmentCashier(request, pk):
    cashier = Cashier.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(cashier)
    department = Departments.objects.get(pk=pk)
    patients = PatientDepartments.objects.filter(department = department)
    
    context = {
        'cashier': cashier,
        'department':department,
        'pk':pk,
        'patients': patients,
        'youAreActive':youAreActive,
        'work':"Cashier",
    }
    return render(request, 'management/cashier/patient_department_cashier.html', context)

def addPaymentPatientDepartmentCashier(request, pk):
    cashier = Cashier.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(cashier)
    patient = PatientDepartments.objects.get(pk=pk)
    department =  patient.department#*************problème*********************************************************************************************
    
    motifs = PaymentMotif.objects.all()
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        motif = PaymentMotif.objects.get(pk=request.POST.get('motif'))
        payment_method = request.POST.get('payment_method')
        
        if amount == motif.amount_motif:
            Payments.objects.create(
                
                patient = patient,
                department = department,#*************problème*********************************************************************************************
                cashier = cashier,
                amount = amount,
                motif = motif,
                payment_method = payment_method
                
            )
            patient.has_paid=True
            patient.save()
            context = {
            'pk':pk,
            'cashier':cashier,
            'department': department,#*************problème*********************************************************************************************
            'patient': patient,
            'motifs': motifs,
            'message':"Successfully paid...",
            'youAreActive': youAreActive,
            'work':"Cashier",
            }
        else:
            context = {
            'pk':pk,
            'cashier':cashier,
            'department': department,
            'patient': patient,
            'motifs': motifs,
            'message':"amount must be equal to "+str(motif.amount_motif),
            'youAreActive':youAreActive,
            'work':"Cashier",
            }
        
        return render(request, 'management/cashier/add_payment_patient_department_cashier.html', context)   
         
    context = {
        'pk':pk,
        'cashier':cashier,
        'department': department,
        'patient': patient,
        'motifs': motifs,
        'youAreActive':youAreActive,
        'work':"Cashier",
    }
    return render(request,'management/cashier/add_payment_patient_department_cashier.html', context )

def paymentSortedByDepartmentCashier(request):
    cashier = Cashier.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(cashier)
    departments = Departments.objects.all().order_by('name')
    patients = Patients.objects.all()
    payments = Payments.objects.all()
    context = {
        'cashier': cashier,
        'departments':departments,
        'payments':payments,
        'patients': patients,
        'youAreActive':youAreActive,
        'work':"Cashier",
    }
    return render(request, 'management/cashier/payment_sorted_by_department_cashier.html', context)

def paymentReceiptCashier(request, pk):
    cashier = Cashier.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(cashier)
    payment = Payments.objects.get(pk=pk)
    patient = payment.patient
    message = "Successfully paid..."
    context = {
        'cashier': cashier,
        'payment':payment,
        'message': message,
        'youAreActive':youAreActive,
        'patient':patient,
        'work':"Cashier",
    }
    return render(request, 'management/cashier/payment_receipt_cashier.html', context)



#****************************************FIN VUES LIES A LA CAISSIERE*********************************************************#


#****************************************VUES LIES AU DOCTEUR*************************************************************#
def me_doctor(request):
    doctor = Doctors.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(doctor)
    context = {
        'doctor': doctor,
        'user_department': searchDepartment(request, Doctors),
        'youAreActive': youAreActive,
        'work': "Doctor",
    }
    if request.method == 'POST':
        context['message'] = me(request, Doctors)
        return redirect('management:home')
    return render(request, 'management/doctor/me_doctor.html', context)
   

def doctor_make_appointment(request):
    doctor = Doctors.objects.get(user=request.user)
    
    youAreActive = verifyActiveOrNot(doctor)
    patients = PatientDepartments.objects.filter(department=doctor.department)
    
    context = {
        'doctor': doctor,
        'current_date': datetime.datetime.now().date().__str__(),
        'max_date': (datetime.datetime.now().date() + datetime.timedelta(days=14)).__str__(),
        'patients': patients,
        'user_department':doctor.department,
        'youAreActive':youAreActive,
        'work':"Doctor",
    }
    if request.method == 'POST':
        try:
            with transaction.atomic():
                patient = Patients.objects.get(pk=request.POST.get('patient'))
                
                date = request.POST.get('date')
                hour = request.POST.get('hour')
                
                Appointments.objects.create(
                    
                    doctor = doctor,
                    patient = patient,
                    date_appointment = date,
                    hour_appointment = hour,
                    department = doctor.department,
                    
                )
                return redirect('management:doctorAppointments')
        except IntegrityError:
                message = "Une erreur interne est apparue. Merci de recommencer votre requête."       
        context['message'] = message    
    
    
    return render(request,'management/doctor/book-appointment-doctor.html', context )

def doctor_appointments(request):
    
    doctor = Doctors.objects.get(user=request.user)
    appointments_list = Appointments.objects.filter(doctor=doctor).order_by('-state', 'date_appointment', 'hour_appointment')
    appointments = pagination(request, appointments_list, 15, 'page')

    youAreActive = verifyActiveOrNot(doctor)
    context = {
        'paginate': True,
        'appointments': appointments,
        'doctor':doctor,
        'doctor':doctor,
        'youAreActive':youAreActive,
        'work':'Doctor',
        'user_department':searchDepartment(request, Doctors)
    }
    return render(request,'management/doctor/doctorAppointments.html', context )

def doctor_make_prescription(request, pk):
    doctor = Doctors.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(doctor)
    appointment = Appointments.objects.get(pk=pk)
    patient = appointment.patient
    department = searchDepartment(request, Doctors)
    context = {
        'patient':patient,
         'pk':pk,
        'user_department':department,
        'youAreActive':youAreActive,
        'doctor':doctor,
        'work':"Doctor",
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():
                symptoms = request.POST.get('symptoms')
                drugPrescription = request.POST.get('drugPrescription')
                examinations = request.POST.get('examinations')
                recommendations = request.POST.get('recommendations')
            
                Prescriptions.objects.create( 
                    appointment = appointment, 
                    patient = patient,
                    doctor = doctor,
                    symptoms = symptoms,
                    drug_prescription = drugPrescription,
                    examinations = examinations,
                    recommendations = recommendations,  
                    
                    
                )
                patient.has_paid=False
                patient.save()
                appointment.state="Consulté"
                appointment.save()
                prescriptions = Prescriptions.objects.filter(doctor=doctor).order_by('prescripted_date')
                message = "Succesfully save"
        except IntegrityError:
            message = "Une erreur interne est apparue. Merci de recommencer votre requête."       
            

        context = {
            'prescriptions': prescriptions,
            'doctor':doctor,
            'youAreActive':youAreActive,
            'user_department':department,
            'work':"Doctor",
            'message':message
        }
        return render(request, 'management/doctor/doctorPrescriptions.html', context)
        
    return render(request, 'management/doctor/doctorMakePrescription.html', context)

def doctor_prescriptions(request):
    
    doctor = Doctors.objects.get(user=request.user)
    prescriptions = Prescriptions.objects.filter(doctor=doctor).order_by('prescripted_date')
    youAreActive = verifyActiveOrNot(doctor)
    context = {
        'prescriptions': prescriptions,
        'doctor':doctor,
        'youAreActive':youAreActive,
        'user_department':searchDepartment(request, Doctors),
        'work':"Doctor",
        
    }
    return render(request,'management/doctor/doctorPrescriptions.html', context )

def patient_informations(request, pk):
    patient = Patients.objects.get(pk=pk)
    appointments = Appointments.objects.filter(patient = patient)
    prescriptions = Prescriptions.objects.filter(patient = patient)
    parameters = Parameters.objects.filter(Q(patient = patient),
                                            Q(service_receptionist__isnull = "null")
                                            )
    
    doctor = Doctors.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(doctor)
    
    context = {
        'patient':patient,
        'doctor':doctor,
        'appointments': appointments,
        'parameters':parameters,
        'user_department':searchDepartment(request, Doctors),
        'youAreActive':youAreActive,
        'prescriptions':prescriptions,
        'work':'Doctor'
    }
    return render(request, 'management/doctor/other1.html', context)

def doctor_patients(request):
    doctor = Doctors.objects.get(user=request.user)
    patients = PatientDepartments.objects.filter(department = doctor.department)
    youAreActive = verifyActiveOrNot(doctor)
    parameters = Parameters.objects.filter(service_receptionist__isnull = False)
    prescription = Prescriptions.objects.all()
    context = {
        'prescription': prescription,
        'patients': patients,
        'doctor': doctor,
        'user_department':searchDepartment(request,Doctors),
        'work':"Doctor",
        'youAreActive':youAreActive,
    }
    return render(request,'management/doctor/doctorPatients.html', context )

def viewPrescriptionPatient(request, pk):
    doctor = Doctors.objects.get(user=request.user)
    youAreActive = verifyActiveOrNot(doctor)
    prescription = Prescriptions.objects.get(pk=pk)
    patient = prescription.patient
    
    context = {
        'prescription':prescription,
        'doctor':doctor,
        'youAreActive':youAreActive,
        'work':"Doctor",
        'patient':patient,
        'pk':pk,
        'user_department':searchDepartment(request,Doctors),
    }
    return render(request, 'management/doctor/view_prescription_patient.html', context)



#****************************************FIN VUES LIES AU DOCTEUR*********************************************************#




"""def searchPrincipalsReceptionist(request):
    patients = []
    if request.method == 'POST':
        search = request.POST.get('search')
        if search is not None:
            users = CustomUser.objects.filter(Q(username__icontains=search) | Q(first_name__icontains=search) | Q(last_name__icontains=search))
            if len(users) > 0:
                for user in users:
                    try:
                        patients.append(Patient.objects.get(first_name=user))
                    except ObjectDoesNotExist:
                        pass
                if len(patients) == 0:
                        messages.info(request, "Patient with Name '"+ search + "' does not exist")
                        return redirect('management:homePrincipalsReceptionist')
                else:
                    context = {'patients': patients,
                               }
                    return render(request, "management/patients.html",context)
                    
            else:
                messages.info(request, "Patient with Name '"+ search + "' does not exist")
                return redirect('management:homePrincipalsReceptionist')
        else:
            messages.info(request, "Please enter a keyword to search")
            return redirect('management:homePrincipalsReceptionist')
    
    messages.info(request, "Please enter a keyword to search")
    return redirect('management:homePrincipalsReceptionist')"""

"""def index(request):
    return render(request, 'management/index.html')

def homePrincipalReceptionnist(request):
    context = {
        'departments': Departments.objects.all(),
    }
    return render(request, 'management/homePrincipalsReceptionist.html', context)


def department_info(request, name):
    context={
        'patients': Departments.objects.get(name=name).patient_set.all(),

        'doctors': Departments.objects.get(name=name).doctor_set.all()
    }
    return render(request, 'management/'+name+'.html',context)

def all_patients(request):

    context = {
        'patients': Patients.objects.all().order_by('-created')
        
    }
    return render(request, 'management/patients.html',context)
    

"""



"""def payments(request):
    payments = Payments.objects.all()
    return render(request, 'management/payments.html', {'payments': payments})

def add_payments(request):
    if request.method == 'POST':
        payment_number = request.POST.get('payment_number')
        patient_name = request.POST.get('patient_name')
        doctor_name = request.POST.get('doctor_name')
        payment_date = request.POST.get('payment_date')
        amount = request.POST.get('amount')
        payment_method= request.POST.get('payment_method')
        payment_status = request.POST.get('payment_status')
        
        Payments.objects.create(
            payment_number = payment_number,
            patient = patient_name,
            doctor = doctor_name,
            date = payment_date,
            amount = amount,
            payment_method = payment_method,
            payemtn_status = payment_status,
        )
        
        messages.info(request, 'Your payment has been received')
        return redirect("management:payments")
        
    return render(request, 'management/add-payments.html')"""

    
