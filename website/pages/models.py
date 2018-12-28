from django.db import models
from django.utils import timezone

class Event(models.Model):
    #author = models.ForeignKey('auth.User')
    event_name = models.CharField(max_length=200)
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    event_location = models.CharField(max_length=200)
    event_info = models.TextField()
    rockSoc_event = models.BooleanField(default=False)
    WUS = models.BooleanField(default=False)
    event_image = models.ImageField(upload_to='images/')
    image_caption = models.TextField(blank=True, default="")
    link_to_Facebook_event = models.CharField(max_length=200, blank=True, null=True)

    def publish(self):
        #self.published_date = timezone.now()
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name

class News(models.Model):
    news_title = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    info = models.TextField()
    #image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = "News"

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.news_title

class Quote(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    quote = models.TextField()
    info = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Quote"

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Album_Category(models.Model):
    album_category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Album_categories"
    
    def __str__(self):
        return self.album_category_name

class Album(models.Model):
    album_category = models.ForeignKey(Album_Category, default=None)
    album_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.album_name

class Image(models.Model):
    album = models.ForeignKey(Album, default=None)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    caption = models.TextField(blank=True, default="")

    def __str__(self):
        return self.album.album_name + ' Image'

#class Category(models.Model):
#    name = models.CharField(max_length=32)

    #class Meta:
    #    verbose_name_plural = "Categories"
    
   # def __str__(self):
    #    return self.name

#class Item(models.Model):
 #   name = models.CharField(max_length=32)
  #  description = models.TextField()
   # category = models.ForeignKey(Category)

  #  def __str__(self):
   #     return self.name
