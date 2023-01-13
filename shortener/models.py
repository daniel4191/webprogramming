from django.db import models
from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser

# Create your models here.


class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


# 이 AbstractUser를 사용하려면 settings에가서 AUTH_USER_MODEL = '<앱이름>.<사용할클래스이름>'
# 이라고 적어 줘야함.

# 두번째로는 이방법을 사용시, 테이블이 한개만 생성된다.
class Users(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)


# 이방법은 사용시, 테이블이 두개 생성된다.
class UserDetail(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
