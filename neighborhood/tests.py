from django.test import TestCase

from django.test import TestCase
from .models import *



class ProfileTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.new_user = User(username='Titus', email='titusouko@gmail.com', password='1234')
        self.new_user.save()
        self.new_hood = Neighborhood(name="Lavington", location="Nairobi", occupants="333",health_contact="123", police_contact="444", hood_pic="me.png", admin=self.new_user)
        self.new_hood.save()
        self.new_profile = Profile(user=self.new_user,hood=self.new_hood,bio="just testing", email='titusouko@gmail.com',name="Titus",profile_pic="image.jpeg")
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
    # def test_save_method(self):
    #     self.new_profile.save_profile()
    #     profile = Profile.objects.all()
    #     self.assertTrue(len(profile)>0)

    # def test_delete_method(self):
    #     self.new_profile.save_profile()
    #     self.new_profile.delete_profile()
    #     profile = Profile.objects.all()
    #     self.assertTrue(len(profile)==0)   
class PostTestClass(TestCase):

    def setUp(self):
        
        self.new_user = User(username='Titus', email='titusouko@gmail.com', password='1234')
        self.new_user.save()
        self.new_hood = Neighborhood(name="Lavington", location="Nairobi", occupants="333",health_contact="123", police_contact="444", hood_pic="me.png", admin=self.new_user)
        self.new_hood.save()
        self.new_post=Post(title="techs",content="test app stuff",image='image.png',user=self.new_user, hood=self.new_hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))    

    def test_save_post(self):
        self.new_post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)

    def test_delete_post(self):
        self.new_post.save_post()
        self.new_post.delete_post()
        post = Post.objects.all()
        self.assertTrue(len(post)==0)

class BuninessTestClass(TestCase):

    def setUp(self):
        
        self.new_user = User(username='Titus', email='titusouko@gmail.com', password='1234')
        self.new_user.save()
        self.new_hood = Neighborhood(name="Lavington", location="Nairobi", occupants="333",health_contact="123", police_contact="444", hood_pic="me.png", admin=self.new_user)
        self.new_hood.save()
        self.new_business=Business(bName="techs",user=self.new_user, hood=self.new_hood, bEmail="titusouko@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))    

    def test_save_business(self):
        self.new_business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business)>0)

    # def test_delete_business(self):
    #     self.new_business.create_business()
    #     self.new_business.delete_business()
    #     business = Business.objects.all()
    #     self.assertTrue(len(business)==0)

class NeighborhoodTestClass(TestCase):

    def setUp(self):
        
        self.new_user = User(username='Titus', email='titusouko@gmail.com', password='1234')
        self.new_user.save()
        self.new_hood = Neighborhood(name="Lavington", location="Nairobi", occupants="333",health_contact="123", police_contact="444", hood_pic="me.png", admin=self.new_user)
       
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood,Neighborhood))    

    def test_save_post(self):
        self.new_hood.create_neigborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_post(self):
        self.new_hood.create_neigborhood()
        self.new_hood.delete_neigborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood)==0)