from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    occupants = models.PositiveIntegerField()
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    bio = models.TextField()
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=50)
    profile_pic = ImageField(upload_to='images/')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Business(models.Model):
    bName = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    bEmail = models.EmailField(max_length=100)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.save()
    
    @classmethod
    def find_business(cls,business_id):
        business= cls.objects.get(id=business_id)
        return business

    @classmethod   
    def update_business(cls,id,name):
        cls.objects.filter(pk = id).update(bName=name)
        new_name_object = cls.objects.get(bName = name)
        new_name = new_name_object.bName
        return new_name

    def __str__(self):

        return self.name

    class Meta:
        order_by =['name']

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    
    @classmethod
    def get_single_post(cls,id):
        return cls.objects.get(id=id)

    @classmethod   
    def update_post(cls,id,title):
        cls.objects.filter(pk = id).update(title=title)
        new_name_object = cls.objects.filte(title__icontains = title)
        new_name = new_name_object.title
        return new_name
