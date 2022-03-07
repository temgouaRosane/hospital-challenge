from django.urls import path, include
from django.conf.urls import url
from .views import   viewPrescriptionPatient, doctor_make_appointment, me_doctor, me_service_receptionist, receptionist_profile, department_receptionist, department_add_patients_accueil, doctor_appointments, doctor_make_prescription, doctor_patients, doctor_prescriptions, patient_informations, paymentReceiptCashier, other, paymentSortedByDepartmentCashier, addPaymentPatientDepartmentCashier, departmentCashier, patientDepartmentPrincipalReceptionist, departmentPrincipalReceptionist, parametres_profile, home, doctors_profile,patients,patients_profile_accueil,schedule,appointment,department_doctors, search
#department_patients,
app_name = 'management'

urlpatterns = [
    #****************************************ROUTES LIES A LA RECEPTIONNISTE DU SERVICE********************************************************#
    path('', home , name="home"),
    #path('doctors/', doctors, name="doctors"), affiche tous les docteurs de l'hopital
    #---------------------docteur-------------------------------#
    path('doctors/', department_doctors, name="department_doctors"), #ajouté
    path('doctors/profile/<int:pk>/', doctors_profile, name="doctors_profile"),
    #---------------------docteur-------------------------------#
   
   #---------------------receptionists-------------------------------#
    path('receptionists/', department_receptionist, name="department_receptionist"), #ajouté
    path('receptionists/profile/<int:pk>/', receptionist_profile, name="receptionist_profile"),
    #---------------------receptionists-------------------------------#
    
    #---------------------me-------------------------------#
    path('my_profile_Service_receptionist/', me_service_receptionist, name="meServiceReceptionist"), #ajouté
    #logout
    #---------------------me-------------------------------#
    
    

    #---------------------patient-------------------------------#
    path('patients/', patients, name="department_patients"),
    path('addpatients/', department_add_patients_accueil, name="department_add_patients"),
    #path('patients/add', add_patients, name="add_patients"),
    path('patients/profile/modifyprofile/<int:pk>/', patients_profile_accueil, name="patients_profile"),
    path('patients/profile/other/<int:pk>/', other, name="other_profile"),
    path('patients/profile/parameters/<int:pk>/', parametres_profile, name="parametres_profile"),#---------------------patient-------------------------------#
    #path('doctors/add/', add_doctors, name="add_doctors"),-----------------pour l'admin
    #---------------------patient-------------------------------#
    path('home/', home , name="homeReceptionist"),
    
    
    #---------------------appointment-------------------------------#
    path('appointment/', appointment , name="appointment"),
    path('schedule/', schedule , name="schedule"),
    #---------------------appointment-------------------------------#
    #****************************************FIN ROUTES LIES A LA RECEPTIONNISTE DU SERVICE********************************************************#
    
    #****************************************ROUTES LIES A LA RECEPTIONNISTE D'ACCUEIL********************************************************#
    path('principalReceptionist/department/<int:pk>/', departmentPrincipalReceptionist , name="department_principal_receptionist"),
    path('principalReceptionist/patient/department/<int:pk>/', patientDepartmentPrincipalReceptionist , name="patient_department_principal_receptionist"),
    


    #****************************************FIN ROUTES LIES A LA RECEPTIONNISTE D'ACCUEIL********************************************************#
    
    #****************************************ROUTES LIES A LA CAISSIERE********************************************************#
    path('cashier/department/<int:pk>/', departmentCashier, name="department_cashier"),
    path('cashier/department/patient/<int:pk>', addPaymentPatientDepartmentCashier, name="add_payment_patient_department_cashier"),
    path('cashier/department/informations/sortedByDepartment', paymentSortedByDepartmentCashier, name="payment_sorted_by_department_cashier"),
    path('cashier/department/informations/paymentReceipt/<int:pk>', paymentReceiptCashier, name="payment_receipt_cashier"),


    #****************************************FIN ROUTES LIES A LA CAISSIERE********************************************************#
    
    
    #****************************************ROUTES LIES AU DOCTEUR********************************************************#
    path('doctorAppointments/', doctor_appointments , name="doctorAppointments"),
    path('doctorPatients/', doctor_patients , name="doctorPatients"),
    path('doctorMakePrescription/<int:pk>/', doctor_make_prescription , name="doctorMakePrescriptions"),
    path('doctorPrescriptions/', doctor_prescriptions , name="doctorPrescriptions"),
    path('doctorPatients/informations/<int:pk>/', patient_informations, name="informations"),
    path('patients/prescriptions/<int:pk>/', viewPrescriptionPatient, name="view_prescription_patient"),
    path('doctorMakePrescription/', doctor_make_appointment , name="doctorMakeAppointment"),
    #---------------------me-------------------------------#
    path('my_profile_doctor/', me_doctor, name="meDoctor"), #ajouté
    #logout
    #---------------------me-------------------------------#
    #****************************************FIN ROUTES LIES AU DOCTEUR********************************************************#
     



        ##########################principal RECEPTIONIST#######################

    #path('', index , name="index"),
    #path('home/', homePrincipalReceptionnist , name="homePrincipalReceptionist"),
    #path('<name>/info/', department_info, name="department_info"),
    #path('all_patients/', all_patients , name="all_patients"),
    path('search/', search , name="search"),
#############################################################################
    
    #path('add_payments/', add_payments , name="add_payments"),
    #path('payments/', payments , name="payments"),
    #path('departments/', departments, name="departments"),
    
    path('search/', search, name="search"),
    #path('department/', department, name="department"),
    #path('patients/', department_patients, name="department_patients"),
    
    
]