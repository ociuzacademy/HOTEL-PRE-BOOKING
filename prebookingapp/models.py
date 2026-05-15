from django.db import models

# Create your models here.

class tbl_register(models.Model):
    email=models.EmailField(max_length=100,default="")
    phn=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
    pswd=models.CharField(max_length=100,default="")
    adrs=models.CharField(max_length=100,default="")
    plc=models.CharField(max_length=100,default="")
    dob=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=100,default="")
    utype=models.CharField(max_length=100,default="")


class tbl_restaurant(models.Model):
    email=models.EmailField(max_length=100,default="")
    phn=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
    pswd=models.CharField(max_length=100,default="")
    adrs=models.CharField(max_length=100,default="")
    plc=models.CharField(max_length=100,default="")
    licence_number=models.CharField(max_length=100,default="")
    img=models.ImageField(upload_to='files',default='null.jpeg')
    status=models.CharField(max_length=100,default="")


class tbl_menu(models.Model):
    restaurant_id=models.ForeignKey(tbl_restaurant,on_delete=models.CASCADE, blank=True,null=True)
    foodcategory=models.CharField(max_length=100,default="")
    img=models.ImageField(upload_to='files',default='null.jpeg')
    description=models.CharField(max_length=100,default="")
    price=models.CharField(max_length=100,default="")
    qnty=models.CharField(max_length=100,default="")
    status=models.CharField(max_length=100,default="")


class tbl_booking(models.Model):
    name=models.CharField(max_length=100,default="")
    date=models.CharField(max_length=100,default="")
    time=models.CharField(max_length=100,default="")
    total_guest=models.CharField(max_length=100,default="")
    phn=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    user_id=models.ForeignKey(tbl_register,on_delete=models.CASCADE, blank=True,null=True)
    restaurant_id=models.ForeignKey(tbl_restaurant,on_delete=models.CASCADE, blank=True,null=True)
    # menu_id=models.ForeignKey(tbl_menu,on_delete=models.CASCADE, blank=True,null=True)
    status=models.CharField(max_length=100,default="")
    items = models.TextField(blank=True, null=True)
    booking_status=models.CharField(max_length=100,default="")
    


class tb_cart(models.Model):
    qnty = models.CharField(max_length=100, default='')
    date = models.CharField(max_length=100, default='')
    total_price = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='')
    menu_id = models.ForeignKey( tbl_menu, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(tbl_register, on_delete=models.CASCADE, blank=True, null=True)



class tbl_order(models.Model):
    user_id = models.ForeignKey(tbl_register, on_delete=models.CASCADE,blank=True, null=True)
    cart_id = models.ForeignKey(tb_cart, on_delete=models.CASCADE,blank=True, null=True)
    menu_id = models.ForeignKey(tbl_menu, on_delete=models.CASCADE,blank=True, null=True)
    total = models.CharField(max_length=30, default='')
    date = models.CharField(max_length=100, default='')
    time = models.CharField(max_length=100, default='')
    payment_status = models.CharField(max_length=30, default='')
    status= models.CharField(max_length=30, default='')
    order_id = models.CharField(max_length=100, default='')





class tbl_payment(models.Model):
    user_id = models.ForeignKey(tbl_register, on_delete=models.CASCADE,blank=True, null=True)
    order_id = models.ForeignKey(tbl_order, on_delete=models.CASCADE,blank=True, null=True)
    date = models.CharField(max_length=100, default='')
    # total_amt = models.CharField(max_length=100, default='')
    card_name = models.CharField(max_length=100, default='')
    card_number = models.CharField(max_length=100, default='')
    card_date = models.CharField(max_length=100, default='')
    card_cvv = models.CharField(max_length=100, default='')
    # card_expdate = models.CharField(max_length=100, default='')
    pay_status = models.CharField(max_length=100, default='')




class tbl_feedback(models.Model):
    user_id = models.ForeignKey(tbl_register, on_delete=models.CASCADE, blank=True, null=True,)
    # menu_id = models.ForeignKey(tbl_menu, on_delete=models.CASCADE, blank=True, null=True, )
    restaurant_id = models.ForeignKey(tbl_restaurant, on_delete=models.CASCADE, blank=True, null=True, )
    ratings = models.IntegerField(default=0, blank=True, null=True)
    msg=models.CharField(max_length=100, default='')

class tbl_menu_feedback(models.Model):
    user_id = models.ForeignKey(tbl_register, on_delete=models.CASCADE, blank=True, null=True,)
    menu_id = models.ForeignKey(tbl_menu, on_delete=models.CASCADE, blank=True, null=True, )
    ratings = models.IntegerField(default=0, blank=True, null=True)
    msg=models.CharField(max_length=100, default='')


class tbl_worker(models.Model):
    email=models.EmailField(max_length=100,default="")
    phn=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
    pswd=models.CharField(max_length=100,default="")
    adrs=models.CharField(max_length=100,default="")
    utype=models.CharField(max_length=100,default="")
    status=models.CharField(max_length=100,default="")
    restaurant_id=models.ForeignKey(tbl_restaurant,on_delete=models.CASCADE, blank=True,null=True)

    
class tbl_worker_status(models.Model):
    worker_id=models.ForeignKey(tbl_worker, on_delete=models.CASCADE,blank=True, null=True)
    order_id = models.ForeignKey(tbl_order, on_delete=models.CASCADE,blank=True, null=True)
    restaurant_id=models.ForeignKey(tbl_restaurant,on_delete=models.CASCADE, blank=True,null=True)
    work_status=models.CharField(max_length=100,default="")
   