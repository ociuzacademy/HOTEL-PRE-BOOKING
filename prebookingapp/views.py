from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import datetime
from datetime import date
import uuid
from django.db.models import F

# Create your views here.
def index(request):
    return render(request,'index.html')



def user_register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pswd=request.POST.get('pswd')
        adrs=request.POST.get('adrs')
        phn=request.POST.get('phn')
        plc=request.POST.get('plc')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        tbl_register(name=name,email=email,pswd=pswd,adrs=adrs,phn=phn,dob=dob,gender=gender,plc=plc,utype='user').save()
        return render(request,'index.html')
    else:
        return render(request,'user_register.html')
    


def restaurant_register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pswd=request.POST.get('pswd')
        adrs=request.POST.get('adrs')
        phn=request.POST.get('phn')
        plc=request.POST.get('plc')
        print('.....',plc)
        licence_number=request.POST.get('licence_number')
        img=request.FILES.get('img')
        print('img',img)
        data=tbl_restaurant(name=name,email=email,pswd=pswd,adrs=adrs,phn=phn,licence_number=licence_number,img=img,plc=plc,status='pending').save()
        print(data)
        return render(request,'index.html')
    else:
        return render(request,'restaurant_register.html')
    



def login(request):
    if request.method == "POST":
        pswd = request.POST['pswd']
        email = request.POST['email']
        var = tbl_register.objects.all().filter(pswd=pswd, email=email, utype='user')
        var2 = tbl_restaurant.objects.all().filter(pswd=pswd, email=email,status='approved')
        var3= tbl_register.objects.all().filter(pswd=pswd, email=email, utype='admin')
        var4= tbl_worker.objects.all().filter(pswd=pswd, email=email, utype='worker')

        if var:
            for x in var:
                request.session['id'] = x.id
            return render(request, 'user/user_home.html')
        if var2:
            for x in var2:
                request.session['id'] = x.id
            return render(request, 'restaurant/restaurant_home.html')        
        elif var3:
            for x in var3:
                request.session['id'] = x.id
            return render(request, 'admin/admin_home.html')
        
        elif var4:
            for x in var4:
                request.session['id'] = x.id
            return render(request, 'worker/worker_home.html')

        else:
            txt = """<script>alert("Invalid user Credentials....");window.location='/';</script>"""
            return HttpResponse(txt) 
    else:
        return render(request, "login.html")
    


def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        logout(request)
    return render(request,'index.html')





def user_home(request):
    return render(request,'user/user_home.html')





def user_profile(request):
    id=request.session['id']
    data=tbl_register.objects.all().filter(id=id)
    return render(request,'user/user_profile.html',{'data':data})




def user_edit_profile(request):
    id=request.session['id']
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pswd=request.POST.get('pswd')
        adrs=request.POST.get('adrs')
        phn=request.POST.get('phn')
        plc=request.POST.get('plc')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        tbl_register.objects.all().filter(id=id).update(name=name,email=email,pswd=pswd,adrs=adrs,phn=phn,dob=dob,gender=gender,plc=plc)
        return HttpResponseRedirect('/user_profile/')
    else:
        data=tbl_register.objects.all().filter(id=id)
        return render(request,'user/user_edit_profile.html',{'data':data})
        

from django.db.models import Avg
def user_view_restaurant(request):
    data = tbl_restaurant.objects.all()

    for restaurant in data:
        ratings = tbl_feedback.objects.filter(restaurant_id=restaurant)
        overall_rating = ratings.aggregate(Avg('ratings'))['ratings__avg']
        restaurant.overall_rating = overall_rating
    return render(request, 'user/user_view_restaurant.html', {'data': data})


def user_booking_restaurant(request,r_id):
    data = tbl_restaurant.objects.get(id=r_id)
    success = False
    if request.method == 'POST':
        user_id = request.session['id']
        restaurant_id = request.POST.get('restaurant_id') 
        # menu_id = request.POST.get('menu_id')
        name = request.POST.get('name') 
        total_guest = request.POST.get('totalguest')
        phn = request.POST.get('phn')
        email = request.POST.get('email')
        items = request.POST.get('items')
        date = request.POST.get('date')
        time = request.POST.get('time')
        uid = tbl_register.objects.get(id=user_id)
        rid = tbl_restaurant.objects.get(id=r_id)
        # mid = tbl_menu.objects.get(id=menu_id)
        tbl_booking(user_id=uid, restaurant_id=rid,name=name,total_guest=total_guest,phn=phn,email=email,date=date, time=time,booking_status="pending" ,items=items, status='pending').save()
        success=True
        return render(request, 'user/user_booking_restaurant.html', {'data': data,'success':success})
    else:
        
        return render(request, 'user/user_booking_restaurant.html', {'data': data})




def user_cancel_bookings(request):
    id=request.GET['id']
    tbl_booking.objects.all().filter(id=id).update(status='cancel')
    return HttpResponseRedirect('/user_view_booking_status/')




def user_view_booking_status(request):
    id=request.session['id']
    data=tbl_booking.objects.all().filter(user_id=id,status__in=['confirmed', 'canceled'])
    return render(request,'user/user_view_booking_status.html',{'data':data})



def user_view_restaurant_details(request):
    data = tbl_restaurant.objects.all()

    for restaurant in data:
        ratings = tbl_feedback.objects.filter(restaurant_id=restaurant)
        overall_rating = ratings.aggregate(Avg('ratings'))['ratings__avg']
        restaurant.overall_rating = overall_rating
    return render(request, 'user/user_view_restaurant_details.html', {'data': data})



def user_view_menu(request):
    id=request.GET['id']
    data=tbl_menu.objects.all().filter(restaurant_id=id)
    for menu in data:
        ratings = tbl_menu_feedback.objects.filter(menu_id=menu)
        overall_rating = ratings.aggregate(Avg('ratings'))['ratings__avg']
        menu.overall_rating = overall_rating
    return render(request,'user/user_view_menu.html',{'data':data})


def user_view_menu_details(request):  
    id = request.GET['id']  
    print('....',id)
    data=tbl_menu.objects.all().filter(id=id).select_related('restaurant_id')
    return render(request,'user/user_view_menu_details.html',{'data':data,})





def add_to_cart(request):
    myid = request.session['id']
    ii = request.GET['id']
    print('miid',ii)
    mid = tbl_menu.objects.get(id=ii)
    uid = tbl_register.objects.get(id=myid)
    number = request.GET['number']
    date = datetime.date.today()
    aq = int(mid.qnty)
    qu = int(number)
    if(aq < qu):
         error_message = "Requested Quantity is Not Available"
         print('....',error_message)
         return render(request, 'user/user_view_menu_details.html', {'error': error_message})
    else:
        proprice = (mid.price)
        total = int(proprice)*int(number)
        tb_cart(qnty=number, user_id=uid, status='pending',date=date, menu_id=mid, total_price=total).save()
        new_qty = int(mid.qnty)-int(number)
        tbl_menu.objects.all().filter(id=(mid.id)).update(qnty=new_qty)
        rid = (mid.restaurant_id.id)
        return HttpResponseRedirect('/user_cartpage/')



def user_cartpage(request):
    myid = request.session['id']
    data = tb_cart.objects.all().filter(user_id=myid, status='pending')
    sum1 = 0
    for x in data:
        a = x.total_price
        sum1 = sum1+int(a)
        print(sum1)
    return render(request, 'user/user_cartpage.html', {'data': data, 'sum': sum1})



def delete_cart(request):
    ii = request.GET['id']
    tb_cart.objects.all().filter(id=ii).delete()
    return HttpResponseRedirect('/user_cartpage/')



# def cart_menu_payment(request):
#     if request.method == 'POST':
#          user_id=request.session.get('id')
#          menu_id = request.POST.get('menu_id')
#          cart_id= request.POST.get('cart_id')
#          if not menu_id or not cart_id:
#             error_message = "Your Cart Is Empty"
#             return render(request, 'user/user_cartpage.html', {'error': error_message})
#          amount = request.POST["subtotal"]
#          current_date = date.today()
#          now = datetime.datetime.now()
#          current_time = now.strftime("%H:%M:%S")
#          uid=tbl_register.objects.get(id=user_id)
#          mid=tbl_menu.objects.get(id=menu_id)
#          cid=tb_cart.objects.get(id=cart_id)
#          order_id = int(uuid.uuid4().int)
#          tbl_order(cart_id=cid,user_id=uid, menu_id=mid,date=current_date,time=current_time,total=amount,payment_status='pending',order_id=order_id,status='pending').save()
#          return render(request,'user/user_payment.html',{"order_id":order_id})
#     else:
#         return render(request, 'user/user_payment.html')

def cart_menu_payment(request):
    if request.method == 'POST':
        user_id = request.session.get('id')
        cart_id = request.POST.get('cart_id')

        if not cart_id:
            error_message = "Your Cart Is Empty"
            return render(request, 'user/user_cartpage.html', {'error': error_message})
        amount = request.POST.get("subtotal")
        current_date = date.today()
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        uid = tbl_register.objects.get(id=user_id)
        cid = tb_cart.objects.get(id=cart_id)
        menu_ids = request.POST.getlist('menu_id')
        for menu_id in menu_ids:
            mid = tbl_menu.objects.get(id=menu_id)
            order_id = int(uuid.uuid4().int)
            tbl_order(
                cart_id=cid,
                user_id=uid,
                menu_id=mid,
                date=current_date,
                time=current_time,
                total=amount,
                payment_status='pending',
                order_id=order_id,
                status='pending'
            ).save()

        return render(request, 'user/user_payment.html', {"order_id": order_id})
    else:
        return render(request, 'user/user_payment.html')





def user_payment(request):
    if request.method == 'POST':
        user_id=request.session.get('id')
        order_id = request.POST.get('order_id')
        cardname = request.POST['cardname']
        cardnumber = request.POST['cardnumber']
        carddate = request.POST['carddate']
        cardcvv = request.POST['cardcvv']
        uid=tbl_register.objects.get(id=user_id)
        oid=tbl_order.objects.get(order_id=order_id)
        tbl_payment(order_id=oid,user_id=uid,card_cvv=cardcvv,card_date=carddate,card_number=cardnumber,card_name=cardname,pay_status='paid').save()
        tb_cart.objects.all().filter(user_id=uid).update(status='paid')
        tbl_order.objects.all().filter(user_id=uid).update(payment_status='paid')
        return render(request, 'user/user_home.html',) 
    else:
       ii=request.POST.get('order_id')
       data1=tbl_order.objects.all().filter(id=ii)
       return render(request, 'user/user_payment.html', {'data1': data1}) 


def user_search_restaurants(request):
    if request.method=="POST":
         plc=request.POST.get('plc')
         if tbl_restaurant.objects.filter(plc=plc).exists():
             data=tbl_restaurant.objects.filter(plc=plc)
             return render(request,'user/user_view_restaurant.html',{'data':data})        
         else:
             msg = "No Restaurants Found...."
             return render(request, 'user/user_search_restaurants.html', {'msg': msg})       
    return render(request,'user/user_search_restaurants.html') 




def user_send_feedback(request, r_id):
    if request.method == 'POST':
        user_id = request.session.get('id')
        if user_id is not None:
            restaurant_id = r_id  # Use the provided r_id parameter
            msg = request.POST.get('msg')
            ratings = request.POST.get('ratings')
            uid = tbl_register.objects.get(id=user_id)
            rid = tbl_restaurant.objects.get(id=restaurant_id)
            tbl_feedback(user_id=uid, restaurant_id=rid, msg=msg, ratings=ratings).save()
            return render(request, 'user/user_home.html')
        else:
            # Handle the case when 'id' is not in session
            return HttpResponse("User not authenticated.")
    else:
        # Use r_id instead of request.GET['id']
        data = tbl_restaurant.objects.get(id=r_id)
        return render(request, 'user/user_send_feedback.html', {'data': data})


def user_send_menu_feedback(request, m_id):
    if request.method == 'POST':
        user_id = request.session.get('id')
        if user_id is not None:
            menu_id = m_id  # Use the provided r_id parameter
            msg = request.POST.get('msg')
            ratings = request.POST.get('ratings')
            uid = tbl_register.objects.get(id=user_id)
            mid = tbl_menu.objects.get(id=menu_id)
            tbl_menu_feedback(user_id=uid, menu_id=mid, msg=msg, ratings=ratings).save()
            # Use r_id instead of request.GET['id']
            data = tbl_menu.objects.get(id=m_id)
            return render(request, 'user/user_send_menu_feedback.html', {'data': data})

        else:
            # Handle the case when 'id' is not in session
            return HttpResponse("User not authenticated.")
    else:
        # Use r_id instead of request.GET['id']
        data = tbl_menu.objects.get(id=m_id)
        return render(request, 'user/user_send_menu_feedback.html', {'data': data})




def user_view_booking(request):
    id=request.session['id']
    data=tbl_booking.objects.all().filter(user_id=id,booking_status='pending', status='pending')
    return render(request,'user/user_view_booking.html',{'data':data})




def user_cancel_bookings(request):
    id=request.GET['id']
    tbl_booking.objects.all().filter(id=id).update(booking_status='canceled')
    return HttpResponseRedirect('/user_view_booking/')

# .....................restaurant...........





def restaurant_home(request):
    return render(request,'restaurant/restaurant_home.html')



def restaurant_profile(request):
    id=request.session['id']
    data=tbl_restaurant.objects.all().filter(id=id)
    return render(request,'restaurant/restaurant_profile.html',{'data':data})


def restaurant_edit_profile(request):
    id=request.session['id']
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pswd=request.POST.get('pswd')
        adrs=request.POST.get('adrs')
        phn=request.POST.get('phn')
        plc=request.POST.get('plc')
        licence_number=request.POST.get('licence_number')
        try:
            img_c = request.FILES['img']
            fs = FileSystemStorage()
            image = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            image = tbl_restaurant.objects.get(id=id).img
        tbl_restaurant.objects.all().filter(id=id).update(name=name,email=email,pswd=pswd,adrs=adrs,phn=phn,licence_number=licence_number,img=image,plc=plc)
        return HttpResponseRedirect('/restaurant_profile/')
    else:
        data=tbl_restaurant.objects.all().filter(id=id)
        return render(request,'restaurant/restaurant_edit_profile.html',{'data':data})
    

def restaurant_menu(request):
    if request.method=='POST':
        id=request.session['id']
        foodcategory=request.POST.get('foodcategory')
        description=request.POST.get('description')
        price=request.POST.get('price')
        qnty=request.POST.get('qnty')
        img=request.FILES.get('img')
        instance=tbl_restaurant.objects.get(id=id)
        tbl_menu(restaurant_id=instance,foodcategory=foodcategory,description=description,price=price,qnty=qnty,img=img,status='pending').save()
        return render(request,'restaurant/restaurant_home.html')
    else:
        return render(request,'restaurant/restaurant_menu.html')




def restaurant_view_menu(request):
    id=request.session['id']
    data=tbl_menu.objects.all().filter(restaurant_id=id)
    return render(request,'restaurant/restaurant_view_menu.html',{'data':data})



def restaurant_edit_menu(request):
    if request.method=='POST':
        id=request.POST.get('id')
        foodcategory=request.POST.get('foodcategory')
        description=request.POST.get('description')
        price=request.POST.get('price')
        qnty=request.POST.get('qnty')
        try:
            img_c = request.FILES['img']
            fs = FileSystemStorage()
            image = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            image = tbl_menu.objects.get(id=id).img
        tbl_menu.objects.all().filter(id=id).update(foodcategory=foodcategory,description=description,price=price,qnty=qnty,img=image)
        return HttpResponseRedirect('/restaurant_view_menu/')
    else:
        id=request.GET['id']
        data=tbl_menu.objects.all().filter(id=id)
        return render(request,'restaurant/restaurant_edit_menu.html',{'data':data,'id':id})



def restaurant_view_bookings(request):
    id=request.session['id']
    data=tbl_booking.objects.all().filter(restaurant_id=id,status='pending',booking_status='pending')
    return render(request,'restaurant/restaurant_view_bookings.html',{'data':data})





def restaurant_confirm_bookings(request):
    id=request.GET['id']
    tbl_booking.objects.all().filter(id=id).update(status='confirmed')
    return HttpResponseRedirect('/restaurant_view_bookings/')


def restaurant_cancel_bookings(request):
    id=request.GET['id']
    tbl_booking.objects.all().filter(id=id).update(status='canceled')
    return HttpResponseRedirect('/restaurant_view_bookings/')


def restaurant_view_canceled_bookings(request):
    id=request.session['id']
    data=tbl_booking.objects.all().filter(restaurant_id=id,status='canceled')
    return render(request,'restaurant/restaurant_view_canceled_bookings.html',{'data':data})


def restaurant_view_feedback(request):
    id=request.session['id']
    data=tbl_feedback.objects.all().filter(restaurant_id=id)
    return render(request,'restaurant/restaurant_view_feedback.html',{'data':data})

def restaurant_view_menu_feedback(request, m_id):
    data=tbl_menu_feedback.objects.all().filter(menu_id=m_id)
    return render(request,'restaurant/restaurant_view_feedback.html',{'data':data})


def restaurant_view_orders(request):
    id = request.session.get('id') 
    data = tbl_order.objects.filter(payment_status='paid', menu_id__restaurant_id=id, status='pending').select_related('menu_id', 'user_id', 'cart_id')
    return render(request, 'restaurant/restaurant_view_orders.html', {'data': data})




def restaurant_add_worker(request):
    if request.method=='POST':
        id=request.session['id']
        name=request.POST.get('name')
        email=request.POST.get('email')
        pswd=request.POST.get('pswd')
        adrs=request.POST.get('adrs')
        phn=request.POST.get('phn')
        rid=tbl_restaurant.objects.get(id=id)
        tbl_worker(restaurant_id=rid,name=name,email=email,pswd=pswd,adrs=adrs,phn=phn,utype='worker',status='pending').save()
        return render(request,'restaurant/restaurant_home.html')
    else:
        return render(request,'restaurant/restaurant_add_worker.html')



def restaurant_view_workers(request):
    id=request.session['id']
    data=tbl_worker.objects.all().filter(restaurant_id=id, )
    return render(request,'restaurant/restaurant_view_workers.html',{'data':data})



def restaurant_delete_worker(request):
    ii = request.GET['id']
    tbl_worker.objects.all().filter(id=ii).delete()
    return HttpResponseRedirect('/restaurant_view_workers/')




def restaurant_view_workers_status(request):
    id=request.session['id']
    data=tbl_worker_status.objects.all().filter(restaurant_id=id)
    return render(request,'restaurant/restaurant_view_workers_status.html',{'data':data})




 



# def restaurant_allocate_work(request):
#     if request.method == 'POST':
#         worker_id = request.POST.get('worker_id')
#         order_id = request.POST.get('order_id')
#         tbl_worker.objects.filter(id=worker_id).update(work_status='Allocate', order_id=order_id)
#         return redirect('/restaurant_view_orders/')
#     else:
#         id = request.session['id']
#         oid = request.GET.get('id')
#         data = tbl_worker.objects.all().filter(restaurant_id=id)
#         return render(request, 'restaurant/restaurant_allocate_work.html', {'data': data, 'oid': oid})


def restaurant_allocate_work(request):
    if request.method == 'POST':
        id=request.session['id']
        worker_id = request.POST.get('worker_id')
        order_id = request.POST.get('order_id')
        rid=tbl_restaurant.objects.get(id=id)
        wid=tbl_worker.objects.get(id=worker_id)
        oid=tbl_order.objects.get(id=order_id)
        oid.status = 'allocate'
        oid.save()

        tbl_worker_status(work_status='Allocate', order_id=oid,worker_id=wid,restaurant_id=rid).save()
        return redirect('/restaurant_view_orders/')
    else:
        id = request.session['id']
        oid = request.GET.get('id')
        data = tbl_worker.objects.all().filter(restaurant_id=id)
        return render(request, 'restaurant/restaurant_allocate_work.html', {'data': data, 'oid': oid})



# ..............admin................


def admin_home(request):
    return render(request,'admin/admin_home.html')



def admin_view_restaurant(request):
    data=tbl_restaurant.objects.all().filter(status='pending')
    return render(request,'admin/admin_view_restaurant.html',{'data':data})



def admin_approve_restaurant(request):
    id=request.GET['id']
    tbl_restaurant.objects.all().filter(id=id).update(status='approved')
    return render(request,'admin/admin_view_restaurant.html')



def admin_reject_restaurant(request):
    id=request.GET['id']
    tbl_restaurant.objects.all().filter(id=id).update(status='rejected')
    return render(request,'admin/admin_view_restaurant.html')



def admin_view_user(request):
    data=tbl_register.objects.all().filter(utype='user')
    return render(request,'admin/admin_view_user.html',{'data':data})



def admin_view_feedback(request):
    data=tbl_feedback.objects.all()
    return render(request,'admin/admin_view_feedback.html',{'data':data})




def admin_view_bookings(request):
    data=tbl_booking.objects.all().filter(status='confirmed')
    return render(request,'admin/admin_view_bookings.html',{'data':data})



def admin_view_orders(request):
    data = tbl_order.objects.filter(payment_status='paid').select_related('menu_id', 'user_id', 'cart_id')
    # data = data.annotate(restaurant_name=F('menu_id__restaurant__name'))
    return render(request, 'admin/admin_view_orders.html', {'data': data})



#.................worker.................



def worker_home(request):
    return render(request,'worker/worker_home.html')





def worker_view_alloted_work(request):
    id=request.session['id']
    data=tbl_worker_status.objects.all().filter(worker_id=id,work_status='allocate')
    return render (request,'worker/worker_view_alloted_work.html',{'data':data})



def worker_accept_work(request):
    id=request.GET['id']
    tbl_worker_status.objects.all().filter(id=id).update(work_status='Accepted')
    return redirect('/worker_view_alloted_work/')



def worker_view_accepted_work(request):
    id=request.session['id']
    data=tbl_worker_status.objects.all().filter(worker_id=id,work_status='Accepted')
    return render (request,'worker/worker_view_accepted_work.html',{'data':data})


def worker_complete_work(request):
    id=request.GET['id']
    tbl_worker_status.objects.all().filter(id=id).update(work_status='Completed')
    return redirect('/worker_view_accepted_work/')


def worker_view_completed_work(request):
    id=request.session['id']
    data=tbl_worker_status.objects.all().filter(worker_id=id,work_status='Completed')
    return render (request,'worker/worker_view_completed_work.html',{'data':data})




def worker_edit_profile(request):
    id=request.session['id']
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        adrs=request.POST.get('adrs')
        phn=request.POST.get('phn')
        tbl_worker.objects.all().filter(id=id).update(name=name,email=email,adrs=adrs,phn=phn)
        return HttpResponseRedirect('/worker_profile/')
    else:
        data=tbl_worker.objects.all().filter(id=id)
        return render(request,'worker/worker_edit_profile.html',{'data':data})
    

    

def worker_profile(request):
    id=request.session['id']
    data=tbl_worker.objects.all().filter(id=id)
    return render(request,'worker/worker_profile.html',{'data':data})