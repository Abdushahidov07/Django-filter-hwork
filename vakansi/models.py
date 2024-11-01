from django.db import models
# Create your models here.

class Cotegory(models.Model):
    cotegory_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.cotegory_name
    


class Vakaansi(models.Model):
    title = models.CharField(max_length=50)
    discraption = models.TextField()
    time_work = models.TimeField(auto_now=False, auto_now_add=False)
    time_notwork = models.TimeField(auto_now=False, auto_now_add=False)
    salary = models.IntegerField()
    image = models.ImageField(upload_to="static/images", height_field=None, width_field=None, max_length=None)
    cotegory = models.ForeignKey(Cotegory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
    

class Application(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    emal = models.EmailField(max_length=254)
    vakansi = models.ForeignKey(Vakaansi, on_delete=models.CASCADE, null=True)
    discraptions = models.TextField()
    resume = models.FileField(upload_to='static/files',)
