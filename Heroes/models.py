from django.db import models

# Create your models here.


class Heroes(models.Model):
    hero = models.CharField(max_length = 120)
    info = models.TextField() 
    update = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    
    def ___unicode__(self):
        return self.hero
    
    def __str__(self):
        return self.hero
0