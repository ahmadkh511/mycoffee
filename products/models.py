from django.db import models
from datetime import datetime  # يجب استيرادها عند التعامل مع الوقت و التاريخ


# Create your models here.

class Product (models.Model):
    name = models.CharField (max_length=150)
    Descriptor = models.TextField ()
    price = models.DecimalField (max_digits=6 , decimal_places=2)
    photo = models.ImageField (upload_to='photos/%y/%m/%d/')  #  تحتاج الى pip install pillow
    is_active = models.BooleanField (default=True)
    publish_date = models.DateTimeField ( default = datetime.now ) #  تحتاج الى from datetime import datetime

    def __str__(self):
        return self.name   # اختار بماذا سوف انته على الكلاس


    class Meta :
        ordering = ['-publish_date']  # علامة الناقص تنازلي   دون علامة الناقص تصاعدي
