from django.db import models

# Create your models here.

'''定义模型对象（其实就是数据库中的“表的模板”）'''
'''django\db\models\fields\__init__.py中有所有的类型'''
class UserInfo(models.Model):
    # 定义属性 也就是  表中列的定义
    UserID=models.BigIntegerField(primary_key=True)  
    UserPassword=models.CharField(max_length=100,null=True)
    Name=models.CharField(max_length=50,null=True)
    Gender=models.BooleanField(null=True)
    Email=models.EmailField(unique=True,null=True) #学生与邮箱必须一一对应


'''签到模块'''
class SignInfo(models.Model):
    UserID=models.ForeignKey(to=UserInfo,on_delete=models.CASCADE,null=True)
    ReservationID=models.ForeignKey(to=ReservationInfo,on_delete=models.CASCADE)
    Deadline=models.SmallIntegerField(null=True)

    
