from django.db import models

# Create your models here.
class hostel(models.Model):
    adhar = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    native = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name+"-"+str(self.mobile)
        