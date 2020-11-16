from django.db import models
from django.db.models.signals import pre_save, post_save
from oyichesports.utils import unique_slug_generator
from django.urls import reverse

# Create your models here.
class Shop (models.Model):
    image       = models.ImageField(upload_to='food/', null=True, blank=True )
    title       = models.CharField(max_length=120)
    price       = models.DecimalField(max_digits=6,decimal_places=2,default=39.99)
    description = models.TextField()
    slug        = models.SlugField(blank=True, unique=True)
    timestamp   =models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        # return '/products/{slug}/'.format(slug=self.slug)
        return reverse('shop:shop_fullwidth')
        # , kwargs={'slug': self.slug}
   


    def __str__(self):
       return self.title

def shop_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)    

pre_save.connect(shop_pre_save_receiver, sender=Shop)         
