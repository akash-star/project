from django.db import models
from tinymce import HTMLField
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email


class Course(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    overview = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to= 'images/',default= 'None')
    content = HTMLField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('course_detail', kwargs={
    #             'course_id':self.id
    #     })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    course=models.ForeignKey('Course', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
