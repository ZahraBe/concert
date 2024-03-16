from django.db import models
from jalali_date import date2jalali, datetime2jalali
from accounts.models import ProfileModel
# from accounts.models import ProfileModel
# Create your models here.

class concertModel(models.Model):

    class Meta:
        verbose_name="کنسرت"
        verbose_name_plural="کنسرت"


    Name = models.CharField(max_length=100, verbose_name="نام کنسرت")
    SingerName= models.CharField(max_length=100, verbose_name="نام خواننده")
    length=models.IntegerField(verbose_name="مدت زمان")
    Poster= models.ImageField(upload_to="concertImages/", verbose_name="پوستر")

    def __str__(self):
        return self.SingerName
    
    
class locationModel(models.Model):
    class Meta:
        verbose_name="محل برگزاری"
        verbose_name_plural="محل برگزاری"
    IdNumber=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100, verbose_name="نام محل")    
    Address=models.CharField(max_length=500, default="تهران-برج میلاد",verbose_name="آدرس ")    
    Phone=models.CharField(max_length=11, null=True,verbose_name="تلفن ")    
    capacity=models.IntegerField(verbose_name="ظرفیت") 

    def __str__(self):
        return self.Name   

class timeModel(models.Model):
    class Meta:
        verbose_name="سانس"
        verbose_name_plural="سانس"

    concertModel= models.ForeignKey(concertModel,on_delete=models.PROTECT,verbose_name="کنسرت")
    locationModel = models.ForeignKey(locationModel, on_delete=models.PROTECT, verbose_name="محل برگزاری")
    StartDateTime = models.DateTimeField(verbose_name="زمان برگزاری")
    Seats = models.IntegerField(verbose_name="تعداد صندلی")

    Start=1
    End=2
    Cancle=3
    Soon=4
    status_choices=((Start,".فروش بلیط شروع شده است"),
                    (End, ".فروش بلیط تمام شده است"),
                    (Cancle, ".این سانس کنسل شده است"),
                    (Soon, ".فروش بلیط به زودی شروع خواهد شد")) 

    Status=models.IntegerField(choices=status_choices,verbose_name="وضعیت", null=True)   
    def __str__(self):
       return "Time: {} Singer: {} Location: {}".format(self.StartDateTime,self.concertModel.SingerName,self.locationModel.Address)
       
    def get_jalali_date(self):
        return datetime2jalali(self.StartDateTime)


class ticketModel(models.Model):
    class Meta:
        verbose_name="بلیط"
        verbose_name_plural="بلیط"    
    ProfileModel= models.ForeignKey(ProfileModel, on_delete= models.PROTECT,verbose_name="کاربر")
    timeModel= models.ForeignKey(timeModel, on_delete= models.PROTECT,verbose_name="سانس")
    TicketImage= models.ImageField(upload_to="TicketImages/",verbose_name="عکس")


    Name= models.CharField(max_length=100,verbose_name="عنوان")
    Price= models.IntegerField(verbose_name="مبلغ")

    def __str__(self):
        return "TicketInfo: Profile:{}".format(self.timeModel.__str__())
   

# class Seat(models.Model):
#     class Meta:
#         verbose_name="صندلی"
#         verbose_name_plural="صندلی"
#     seat_number = models.CharField(max_length=10)
#     is_reserved = models.BooleanField(default=False)

#     def ــstrــ(self):
#         return f"Seat {self.seat_number}"  