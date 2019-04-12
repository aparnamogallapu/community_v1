from django.shortcuts import render
from django.views.generic import ListView

from app.models import UserRegister, UserPayment, Booking, ElectricityBill, WaterBill, Complaint, SalaryBill

d1 = {"A":
          {'2BHK':['A101','A103','A105','A107','A109','A111','A113','A115','A117','A119'],
            '3BHK':['A102','A104','A106','A108','A110','A112','A114','A116','A118','A120']},

          "B": {'2BHK':['B101','B103','B105','B107','B109','B111','B113','B115','B117','B119'],
                '3BHK':['B102','B104','B106','B108','B110','B112','B114','B116','B118','B120']},

          "C": {'2BHK':['C101','C103','C105','C107','C109','C111','C113','C115','C117','C119'],
                '3BHK':['C102','C104','C106','C108','C110','C112','C114','C116','C118','C120']},

          "D": {'2BHK':['D101','D103','D105','D107','D109','D111','D113','D115','D117','D119'],
                '3BHK':['D102','D104','D106','D108','D110','D112','D114','D116','D118','D120']}}

def openhome(request):
    type = request.GET.get("type")
    return render(request, 'index.html', {'type': type})

def openaboutus(request):
    type = request.GET.get("type")
    return render(request, 'index.html', {'type': 'abt_us'})

def opengallery(request):
    type=request.GET.get("type")
    return render(request,'index.html',{'type':'v_gallery'})

def openviewevent(request):
    type=request.GET.get("type")
    return render(request,'index.html',{'type':'v_event'})


def openadminlogin(request):
    type = request.GET.get("type")
    return render(request,'index.html',{'type':'a_log'})

def adminLogin(request):
    type=request.GET.get("type")
    uname = request.POST.get("a_name")
    pswd = request.POST.get("a_pass")
    if uname == 'admin':
        if pswd == 'admin123':
            return render(request, 'adminhome.html')
        else:
            return render(request, 'index.html', {'m1': 'Invalid','type':'a_log'})


def openuserlogin(request):
    type=request.GET.get("type")
    return render(request,'index.html',{'type':'u_log'})

def userLogin(request):
    type = request.GET.get("type")
    uname=request.POST.get("u_name")
    upass=request.POST.get("u_pass")

    sur=UserRegister.objects.filter(flat_no=uname,password=upass)
    if sur:
        res=UserRegister.objects.get(flat_no=uname)
        return render(request,'userhome.html',{'res':res})
    else:
        return render(request,'index.html',{'mess':'invalid','type':'u_log'})

def UserProfile(request):
    type = 'u_pro'
    flat=request.GET.get("type")
    #flat_no=request.GET.get("u_name")
    res = UserRegister.objects.get(flat_no=flat)
    return render(request, 'userhome.html', {'type':type,'res':res})


def bills(request):
    type = request.GET.get("type")
    return render(request, 'adminhome.html',{'type':'a_bill'})

def electricitypage(request):
    try:
        type = request.GET.get("type")
        res = ElectricityBill.objects.all()
        return render(request, 'adminhome.html',{'type':'e_bill','res':res})
    except:
        res = ElectricityBill.objects.all()
        return render(request, 'adminhome.html', {'type': 'e_bill', 'res': res})

def saveEBill(request):
    amount=request.POST.get('e_amt')
    date=request.POST.get('e_date')
    eb=ElectricityBill(amount=amount,date=date)
    eb.save()
    d={'message':'saved'}
    res=ElectricityBill.objects.all()
    return render(request,'adminhome.html',{'type':'e_bill','res':res})

def EbillDelete(request):
    dl_date=request.POST.get("delete_ebill")
    print(dl_date)
    ElectricityBill.objects.filter(date=dl_date).delete()
    res =ElectricityBill.objects.all()
    return render(request, 'adminhome.html', {'type':'e_bill',"res": res})

def OpenEbillUpdate(request):
    up_date=request.GET.get("update_ebill")
    eb=ElectricityBill.objects.get(date=up_date)

    return render(request, 'adminhome.html', {"type":'updateebilldata',"eb":eb})

def updateebillsave(request):
    amount=request.POST.get('amount')
    date=request.POST.get('date')
    eb=ElectricityBill(amount=amount,date=date)
    eb.save()
    return  electricitypage(request)
    # return render(request,"adminhome.html",{"type":"e_bill"})



def waterpage(request):
    try:
        type = request.GET.get("type")
        res = WaterBill.objects.all()
        return render(request, 'adminhome.html',{'type':'w_bill','res':res})
    except:
        res=WaterBill.objects.all()
        return render(request,'adminhome.html',{'type':'w_bill','res':res})



def saveWBill(request):
    amount=request.POST.get("w_amt")
    date=request.POST.get('w_date')
    wb=WaterBill(amount=amount,date=date)
    wb.save()
    res=WaterBill.objects.all()
    return render(request,'adminhome.html',{'type':'w_bill','res':res})

def WbillDelete(request):
    dl_date=request.POST.get("delete_wbill")
    WaterBill.objects.filter(date=dl_date).delete()
    res=WaterBill.objects.all()

    return render(request,'adminhome.html',{ 'type':'w_bill',"res":res})


def OpenWbillUpdate(request):
    up_date=request.GET.get("update_wbill")
    wb=WaterBill.objects.get(date=up_date)

    return render(request, 'adminhome.html', {"type":'updatewbilldata',"wb":wb})

def updatewbillsave(request):
    amount=request.POST.get('amount')
    date=request.POST.get('date')
    wb=WaterBill(amount=amount,date=date)
    wb.save()
    return  waterpage(request)
    # return render(request,"adminhome.html",{"type":"w_bill"})

def salarypage(request):
    type = request.GET.get("type")
    salbil = SalaryBill.objects.all()
    print(salbil)
    return render(request, 'adminhome.html',{'type':'s_bill','salbil':salbil})

def saveSBill(request):
    mname=request.POST.get('m_name')
    msal=request.POST.get('m_sal')
    in1_name=request.POST.get('inch1_name')
    in1_sal=request.POST.get('inch1_sal')
    in2_name = request.POST.get('inch2_name')
    in2_sal = request.POST.get('inch2_sal')
    in3_name = request.POST.get('inch3_name')
    in3_sal = request.POST.get('inch3_sal')
    in4_name = request.POST.get('inch4_name')
    in4_sal = request.POST.get('inch4_sal')
    sec_no = request.POST.get('sec_no')
    sec_sal = request.POST.get('sec_sal')
    date=request.POST.get('s_date')
    sb=SalaryBill(manager_name=mname,manager_salary=msal,incharege1_name=in1_name,incharege1_salary=in1_sal,incharege2_name=in2_name,incharege2_salary=in2_sal,incharege3_name=in3_name,incharege3_salary=in3_sal,incharege4_name=in4_name,incharege4_salary=in4_sal,security_salary=sec_sal,total_security=sec_no,date=date)
    sb.save()
    tsal=float(msal)+float(in1_sal)+float(in2_sal)+float(in3_sal)+float(in4_sal)+float(sec_sal)
    print(tsal)
    salbil=SalaryBill.objects.all()
    return render(request,'adminhome.html',{'res':tsal,"date":date,'salbil':salbil,'type':'s_bill'})

def registerpage(request):
    type = request.GET.get("type")
    return render(request, 'index.html',{'type':'u_reg'})

class ViewBooking(ListView):
    model= Booking
    template_name= 'adminhome.html'
    context_object_name = 'book'

class Viewuserpage(ListView):
    model = UserRegister
    template_name = 'adminhome.html'
    context_object_name = 'display'
    # type = request.GET.get("type")
    # return render(request, 'adminhome.html', {'type': 'v_user'})

def block(request):
    type ='u_reg'
    b1=request.POST.get("block_name")
    res=d1[b1]
    print(res)
    return render(request,'index.html',{'res':res,'type':type,'b1':b1})

def flat(request):
    type='u_reg'
    b1 = request.POST.get('b1')
    b2=request.POST.get("flats")
    res1=d1[b1][b2]
    print(res1)
    return render(request,'index.html',{'res1':res1,'type':'u_reg',"b1":b1,"ft":b2})

def saveUserRegister(request):
    block=request.POST.get("b1")
    f_type=request.POST.get("ft")
    flat_no=request.POST.get("flat_no")
    name=request.POST.get("u_name")
    contact=request.POST.get("u_cno")
    email=request.POST.get("u_email")
    occupation=request.POST.get("u_occupation")
    password=request.POST.get("u_upass")
    ur=UserRegister(block_name=block,flat_type=f_type,flat_no=flat_no,name=name,contact=contact,email=email,occupation=occupation,
                    password=password)
    ur.save()
    return render(request,'index.html',{'mes':'saved','type':'u_log'})

def profileDelete(request):
    dl_profile = request.POST.get("delete_pro")
    res = UserRegister.objects.get(flat_no=dl_profile)
    type = 'del'
    # UserRegister.objects.filter(flat_no=dl_profile).delete()
    # res = UserRegister.objects.all()
    return render(request, 'userhome.html', {'type':type,'res':res})

def prodel(request):
    type = 'u_log'
    option = request.POST.get('d1')
    delete = request.POST.get('delete')
    if option == 'Yes':
        UserRegister.objects.filter(flat_no=delete).delete()
        return render(request, 'index.html',{'type':type})
    else:
        type = 'u_pro'
        dl_profile = request.POST.get("delete")
        res = UserRegister.objects.get(flat_no=dl_profile)
        return render(request, 'userhome.html',{'type':type,'res':res})


def profileupdate(request):
    type = 'profileupdate'
    flat_no = request.GET.get('type')
    res = UserRegister.objects.get(flat_no=flat_no)
    return render(request,'userhome.html',{'type':type,'res':res})

def updateSave(request):
    flat_no=request.POST.get("fno")
    flat_type=request.POST.get("ft")
    block_name=request.POST.get("b")
    name = request.POST.get("u_name")
    contact = request.POST.get("u_cno")
    email = request.POST.get("u_email")
    occupation = request.POST.get("u_occupation")
    password = request.POST.get("u_upass")
    ur=UserRegister(flat_no=flat_no,flat_type=flat_type,block_name=block_name,name=name,contact=contact,email=email,occupation=occupation,password=password)
    ur.save()
    return render(request,'userhome.html',{'res':ur,'type':'u_pro'})




def openpaymentpage(request):
    type = 'u_pay'
    flat_no = request.GET.get("type")
    res = UserRegister.objects.get(flat_no=flat_no)
    return render(request, "userhome.html", {"type":type,'res':res})

def savepayment(request):
    block_name=request.POST.get("bn")
    flat_no=request.POST.get("fno")
    flat_type=request.POST.get("ft")
    amount=request.POST.get("amt")
    paymode=request.POST.get("paymode")
    date=request.POST.get("date")
    print(block_name,flat_no,flat_type,amount,paymode,date)
    up=UserPayment(flat_no=flat_no,total_amt=amount,type_of_payment=paymode,date=date,block_name=block_name,flat_type=flat_type)
    up.save()
    res = UserRegister.objects.get(flat_no=flat_no)
    return render(request,'userhome.html',{'mes':'paid','type':'u_pay','res':res})

def openbookingpage(request):
    type = 'u_book'
    flat=request.GET.get("type")
    res=UserRegister.objects.get(flat_no=flat)
    return render(request,'userhome.html',{'type':type,'res':res})


def saveBooking(request):
    name=request.POST.get('u_name')
    block_name=request.POST.get('bn')
    flat_type=request.POST.get('ft')
    flat_no=request.POST.get('fno')
    email=request.POST.get('u_email')
    purpose=request.POST.get('u_pur')
    date=request.POST.get('u_date')
    message=request.POST.get('u_mes')
    # print(name,block_name,flat_type,flat_no,email,purpose,date,message)
    bk=Booking(name=name,flat_no=flat_no,booking_purpose=purpose,booking_date=date,message=message,email=email,flat_type=flat_type,
               block_name=block_name)
    bk.save()
    res = UserRegister.objects.get(flat_no=flat_no)
    return render(request,'userhome.html',{'res':res})


def userlogout(request):
    #type=request.GET.get("type")
    return render(request,'index.html')




def opencomplaintpage(request):
    type='u_comp'
    flat = request.GET.get("type")
    res = UserRegister.objects.get(flat_no=flat)
    return render(request, 'userhome.html', {'type': type, 'res': res})

def savecomplaint(request):
    name=request.POST.get('u_name')
    block_name=request.POST.get('bn')
    flat_type=request.POST.get('ft')
    flat_no=request.POST.get('fno')
    email=request.POST.get('u_email')
    date=request.POST.get('u_date')
    complaint=request.POST.get('u_com')
    print(name,block_name,flat_no,flat_type,email,date,complaint)
    cp=Complaint(name=name,flat_no=flat_no,date=date,complaint=complaint,email=email,flat_type=flat_type,
               block_name=block_name)
    cp.save()
    res = UserRegister.objects.get(flat_no=flat_no)
    return render(request,'userhome.html',{'res':res})

class ViewComplaint(ListView):
    model = Complaint
    template_name = 'adminhome.html'
    context_object_name = 'complaint'


def adminlogout(request):
    return render(request,'index.html')


def viewAllBills(request):
    type='bills'
    flat_no=request.GET.get("type")
    wbill=WaterBill.objects.all().latest('date')
    ele = ElectricityBill.objects.all().latest('date')
    sal = SalaryBill.objects.all().latest('date')
    print(wbill,ele,sal)
    ftype=UserRegister.objects.get(flat_no=flat_no)
    tobhk=UserRegister.objects.filter(flat_type='2BHK')
    print(len(tobhk))
    thbhk=UserRegister.objects.filter(flat_type='3BHK')
    user=UserRegister.objects.all()
    for x in user:

        if x.flat_type=='2BHK' and ftype.flat_type == '2BHK':
            wb=(wbill.amount*40)/100
            sb=(sal.total_sal*40)/100
            eb=(ele.amount*40)/100
            # print(wb,sb,eb)
            twb=wb/len(tobhk)
            teb=eb/len(tobhk)
            tsal=sb/len(tobhk)
            return render(request,"userhome.html",{'waterbill':twb,'electricitybill':teb,"salarybill":tsal,'type':type})
        elif x.flat_type == '3BHK' and ftype.flat_type == '3BHK':
            wb = (wbill.amount * 60) / 100
            sb = (sal.total_sal * 60) / 100
            eb = (ele.amount * 60) / 100
            # print(wb,sb,eb)
            twb = wb / len(thbhk)
            teb = eb / len(thbhk)
            tsal = sb / len(thbhk)
            return render(request, "userhome.html",
                          {'waterbill': twb, 'electricitybill': teb, "salarybill": tsal, 'type': type})



def UpdatesaveSBill(request):
    tsal=request.POST['tol_sal']
    print(tsal)
    tdate=request.POST['tdate']
    # print(tdate)
    SalaryBill.objects.filter(date=tdate).update(total_sal=tsal)
    salbill = SalaryBill.objects.all()
    return render(request,"adminhome.html",{'type':'s_bill',"msg":"bill saved",'tsal':tsal,'tdate':tdate,'salbil':salbill})


def openupdatesal(request):
    date = request.GET['update_sbill']
    uptbil = SalaryBill.objects.get(date=date)
    print(uptbil)
    return render(request,'adminhome.html',{'date':date,'uptbil':uptbil,'type':'uptb'})


# def uptbil(request):
#     return render(request,'adminhome.html','type':)


def deletesal(request):
    dl_date=request.POST.get("delete_sbill")
    SalaryBill.objects.filter(date=dl_date).delete()
    res=SalaryBill.objects.all()
    print(res)
    return render(request,'adminhome.html',{ 'type':'s_bill',"salbil":res})
