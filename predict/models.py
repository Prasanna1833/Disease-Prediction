from django.db import models

# Create your models here.
class History(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    symptoms = models.TextField()
    predicted_disease = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


