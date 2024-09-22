from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .context_processor import trainer
from .models import *
from datetime import timedelta
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Trainer Expiry

def trainer_expire(request):
    # Current date
    thirty_days_ago = timezone.now() - timedelta(days=30)
    expire_objects = Tbl_trainer_assign.objects.filter(payment_id__date__lte=thirty_days_ago)
    for i in expire_objects:
        i.payment_id.pstatus = False
        i.payment_id.save()
        i.delete()
    return 'cleared the expied trainers assign list'


def home(request):
    c = Tbl_Category.objects.all()
    scat = Tbl_SubCategory.objects.all()
    k = trainer_expire(request)
    print(k)
    return render(request, 'index.html', {'cat': c, 'scat': scat})


def contact(request):
    return render(request, 'contact.html')


def aboutus(request):
    return render(request, 'about-us.html')


def customer_registration(request):
    if request.method == 'POST':
        cust_fname = request.POST['cust_fname']
        cust_lname = request.POST['cust_lname']
        cust_age = request.POST['cust_age']
        cust_height = request.POST['cust_height']
        cust_weight = request.POST['cust_weight']
        cust_phno = request.POST['cust_phno']
        cust_prob = request.POST['cust_prob']
        cust_email = request.POST['cust_email']
        cust_pass = request.POST['cust_pass']
        cust_repass = request.POST['cust_repass']
        cust_gender = request.POST['gender']
        if User.objects.filter(username=cust_email).exists():
            print('Email Already exist')
            messages.info(request,"Email Already Exists..!")
        else:
            if cust_pass == cust_repass:
                user = User.objects.create_user(first_name=cust_fname, last_name=cust_lname, username=cust_email,
                                                password=cust_pass)
                user.save()
                register = Tbl_customer(cust_fname=cust_fname, cust_lname=cust_lname, cust_age=cust_age,
                                        cust_height=cust_height, cust_phone=cust_phno, cust_problem=cust_prob,
                                        cust_email=cust_email, user=user, cust_gender=cust_gender, cust_status=True,
                                        cust_weight=cust_weight)
                register.save()
                messages.info(request, "Sucessfuly created..!")
                if request.user.is_superuser:
                    return redirect('custall')
                else:
                    return redirect('homeorg')

    return render(request, 'customer_registration.html')


def trainer_registration(request):
    if request.method == 'POST':
        tname = request.POST['trainer_name']
        tage = request.POST['trainer_age']
        tphone = request.POST['trainer_phno']
        tgender = request.POST['gender']
        tlevel = request.POST['level']
        tcertificate = request.FILES['trainer_certificate']
        timage = request.FILES['trainer_image']
        temail = request.POST['trainer_email']
        tpassw = request.POST['trainer_pass']
        trepass = request.POST['trainer_repass']
        if User.objects.filter(username=temail).exists():
            print('email already taken')
            messages.info(request, "Email Already Exists..!")
        else:
            if tpassw == trepass:
                user = User.objects.create_user(username=temail, password=tpassw, first_name=tname)
                user.save()
                trainer = Tbl_Trainer(trainer_name=tname, trainer_age=tage, trainer_gender=tgender,
                                      trainer_email=temail,
                                      trainer_phone=tphone, trainer_certificate=tcertificate, trainer_level=tlevel,
                                      trainer_image=timage, trainer_approval=False,
                                      trainer_status=False, user=user)
                trainer.save()
                messages.info(request, "Trainer registration successfully..!")
                if request.user.is_superuser:
                    return redirect('tal')
                else:
                    return redirect('homeorg')
    return render(request, 'trainer_registration.html')


# trainer edit
def traineredit(request, cid):
    cus = Tbl_Trainer.objects.get(id=cid)
    if request.method == 'POST':
        trainer_name = request.POST['trainer_name']
        trainer_age = request.POST['trainer_age']
        trainer_gender = request.POST['gender']
        trainer_email = request.POST['trainer_email']
        trainer_phone = request.POST['trainer_phone']
        trainer_level = request.POST['level']
        cus.trainer_name = trainer_name
        cus.trainer_age = trainer_age
        cus.trainer_gender = trainer_gender
        cus.trainer_email = trainer_email
        cus.trainer_phone = trainer_phone
        cus.trainer_level = trainer_level
        cus.save()
        print('Succesfully updated')
        messages.info(request, "Updated..!")
        if request.user.is_superuser:
            return redirect('tal')
        else:
            return redirect('/')

    return render(request, 'traineredit.html', {'c': cus})


# Login function

def LoginFunction(request):
    trainer = str(Tbl_Trainer.objects.filter(trainer_status=True).values_list('trainer_email'))
    if request.method == 'POST':
        name = request.POST['name']
        pas = request.POST['pas']
        user = authenticate(username=name, password=pas)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('home')
            elif request.user.is_staff:
                return redirect('custall')
            elif name in trainer:
                tr = list(Tbl_Trainer.objects.filter(trainer_status=True, trainer_approval=True).values_list('user',
                                                                                                             flat=True))
                print('trainer = ', tr)
                if request.user.id in tr:
                    return redirect('tcl')
                else:
                    print("You are not approved by our admin")
                    return redirect('/')
            else:
                return redirect('/')
        else:
            return redirect('login')
    return render(request, 'login.html')


# Logout Function

def LogoutFunction(request):
    logout(request)
    return redirect('/')


# custhome
@login_required(login_url='login')
def custhome(request, id, scid=0):
    c = Tbl_Category.objects.all()
    scat = Tbl_SubCategory.objects.filter(category=id)

    try:
        tutvideos = Tbl_tutorial.objects.filter(sub_category_name__category=id).first()
        tut = Tbl_tutorial.objects.filter(sub_category_name=scid)
    except:
        pass
    return render(request, 'custhome.html', {'mcid': id, 'cat': c, 'scat': scat, 'tut': tut, 'tutv': tutvideos})


def custhomevideos(request, tid, cid):
    scat = Tbl_SubCategory.objects.filter(category=cid)
    tutvideos = Tbl_tutorial.objects.get(id=tid)
    tutdetails = Tbl_tutorial.objects.get(id=tid)
    scid = tutvideos.sub_category_name
    tut = Tbl_tutorial.objects.filter(sub_category_name=scid)
    print(tut)

    return render(request, 'custhome.html',
                  {'tutv': tutvideos, 'tut': tut, 'mcid': cid, 'scat': scat, 'tutd': tutdetails})


# diet function
def custDiet(request):
    user = request.user
    try:
        diet = Tbl_diet.objects.filter(customer=user).last()
        if diet.status == True:
            d = diet
        else:
            d = ''
        print(d)
        w = Tbl_diet.objects.filter(customer=user,status=False)
        print('w == ',w)
    except:
        pass
        w = ''
        d = ''
    return render(request, 'custDiet.html', {'d': d, 'w': w})



@login_required(login_url='login')
def request_diet(request):
    u = request.user
    diet = Tbl_diet(customer=u)
    diet.save()
    return redirect('paym')






# Payment Function
def Payment_Function(request):
    u = request.user
    card = ''
    try:
        card = Tbl_card.objects.get(customer=u)
    except:
        pass
    if request.method == 'POST':
        cno = request.POST['cardNumber']
        exp = request.POST['expiryDate']
        c, s = Tbl_card.objects.get_or_create(customer=u, card_number=cno,expiry_date=exp)
        c.customer = u
        c.card_number = cno
        c.expiry_date = exp
        c.save()
        return redirect('pcfm')
    return render(request, 'card_details.html', {'card': card})


def payment_confirm(request):

    if request.method == 'POST':
        p = Tbl_payment(type='D', card=Tbl_card.objects.get(customer=request.user), amount=500)
        p.save()
        return redirect('billdiet',id=p.id)
    return render(request, 'paymentconfm.html')


# Request Diet Function Button


# Trainer customer view

def trainercustview(request):
    tr = Tbl_Trainer.objects.filter(trainer_approval=True, trainer_status=True)
    if Tbl_trainer_assign.objects.filter(customer=request.user).exists():
        trainer_exit = Tbl_trainer_assign.objects.filter(customer=request.user).first()
        return redirect('tcust2', id=trainer_exit.trainer.id)
    return render(request, 'trainercust.html', {'tr': tr})


def trainercustview2(request, id):
    tr = Tbl_Trainer.objects.get(id=id)
    if Tbl_trainer_assign.objects.filter(customer=request.user).exists():
        tex = '1'
    else:
        tex = ''
    return render(request, 'trainercust2.html', {'tr': tr, 'tex': tex})


# Trainer Payment

def Payment_Function2(request, tid):
    u = request.user
    card = ''
    try:
        card = Tbl_card.objects.get(customer=u)
    except:
        pass
    if request.method == 'POST':
        cno = request.POST['cardNumber']
        exp = request.POST['expiryDate']
        c, s = Tbl_card.objects.get_or_create(customer=u, card_number=cno,expiry_date=exp)
        c.customer = u
        c.card_number = cno
        c.expiry_date = exp
        c.save()
        return redirect('pc2', tid)
    return render(request, 'card_details2.html', {'card': card})


# trainer payment2
def payment_confirm2(request, tid):
    try:
        dt = Tbl_diet.objects.get(customer=request.user)
        diet = str(dt.id)
    except:
        diet = ''
    if request.method == 'POST':
        if Tbl_payment.objects.filter(type='T', card=Tbl_card.objects.get(customer=request.user), amount=1000).exists():
            print("Trainer Plan Already Exists")
            messages.info(request, "Trainer Plan Already Exists")
        else:
            p = Tbl_payment(type='T', card=Tbl_card.objects.get(customer=request.user), amount=1000)
            p.save()
            tta = Tbl_trainer_assign(trainer_id=tid, customer=request.user, payment_id=p)
            tta.save()
            return redirect('billtrainer',id=p.id)

    return render(request, 'paymentconfm2.html')


def trainer_cust_all(request):
    if request.user.is_superuser:
        return redirect('/')
    else:
        call = Tbl_trainer_assign.objects.filter(trainer__user=request.user).order_by('-id')
        return render(request, 'trainer_cust_list.html', {'cust': call})


def trainer_customer_view(request, id):
    cust = Tbl_customer.objects.get(user_id=id)
    print(cust)
    return render(request, 'trainer_cust_list2.html', {'cust': cust})


# Adding Leader Points
@csrf_exempt
def LeaderPoint(request):
    point, pt = Tbl_LeaderBoard.objects.get_or_create(customer=request.user)
    point.points += 1
    point.save()
    print('POINT SAVED')
    message = 'One point added to your leader board..!'
    return render(request, 'status.html', {'messages': message})


def leadertable(request):
    po = Tbl_LeaderBoard.objects.all().order_by('-points')
    return render(request, 'leaderboard.html', {'po': po})


def feedback(request):
    if request.method == 'POST':
        user = request.user
        cust = Tbl_customer.objects.get(user=user)

        msg = request.POST['Feedback']

        f = Tbl_Feedback(customer=cust, msg=msg)
        f.save()

    return render(request, 'feedback.html', )


def billdiet(request,id):
    return render(request, 'billdiet.html',{'id':id})


def billtrainer(request,id):

    return render(request, 'billtrainer.html',{'id':id})







from django.db.models import Q
### Search ###

def Search(request):
    query = ''
    query = request.GET.get('q')
    print('query == ',query)
    cat = Tbl_Category.objects.filter(Q(category_name__icontains=query) | Q(category_desc=query))

    print("result == ",cat)
    return redirect('/')
    #return render(request,"search.html",{'cat':cat})