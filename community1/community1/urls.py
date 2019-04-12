"""community1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views
from app.models import Complaint
from app.views import Viewuserpage, ViewBooking, ViewComplaint

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.openhome),
    path('home/',views.openhome),
    path('about/',views.openaboutus),
    path('gallery/',views.opengallery),
    path('viewevent/',views.openviewevent),
    #path('viewcomplaints/',views.openviewcomplaints),
    path('admin/',views.openadminlogin),
    path('adminlogin/', views.adminLogin),
    path('user/',views.openuserlogin),
    path('userlogin/',views.userLogin),
    path('bills/',views.bills),
    path('electricity/',views.electricitypage),
    path('saveebill/',views.saveEBill),
    path('deletee/',views.EbillDelete),
    path('openupdatee/',views.OpenEbillUpdate),
    path('updateebillsave/',views.updateebillsave),

    path('water/',views.waterpage),
    path('savewbill/',views.saveWBill),
    path('deletew/',views.WbillDelete),
    path('openupdatew/',views.OpenWbillUpdate),
    path('updatewbillsave/',views.updateebillsave),
    path('savesbill/',views.saveSBill),
    path('tot/',views.UpdatesaveSBill),
    path('deletesal/',views.deletesal),
    #path('tot1/',views.uptbil),
    path('register/',views.registerpage),
    path('block/',views.block),
    path('flat/',views.flat),
    path('salary/',views.salarypage),
    path('viewbooking/',ViewBooking.as_view()),
    #path('viewsuggestion/',views.viewsuggestionpage),
    path('viewuser/',Viewuserpage.as_view()),
    path('saveregister/',views.saveUserRegister),
    path('payment/',views.openpaymentpage),
    path('booking/',views.openbookingpage),
    path('savepayment/',views.savepayment),
    path('savebooking/',views.saveBooking),
    path('complaint/',views.opencomplaintpage),
    path('savecomplaint/',views.savecomplaint),
    path('viewcomplaint/',ViewComplaint.as_view()),
    path('profile/',views.UserProfile),
    path('profiledelete/',views.profileDelete),
    path('prodel/',views.prodel),
    path('profileupdate/',views.profileupdate),
    path('updatesave/',views.updateSave),
    path('userlogout/',views.userlogout),
    path('adminlogout/',views.adminlogout),
    # path('userdel/',views.userdel),
    path('allbills/',views.viewAllBills),
    path('openupdatesal/',views.openupdatesal),

]
