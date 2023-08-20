from django.db import models


# Create your models here.

class ShopSupply(models.Model):
    el_name = models.CharField('Name', max_length=80)
    company_name = models.CharField('Manufacturer', max_length=50)
    type_el = models.CharField('Category', max_length=50)
    quantity = models.IntegerField('Quantity')
    availability = models.BooleanField('Availability', default=True)
    image_item = models.ImageField('Image', default='no_image.jpg', upload_to='service/images/shop/')

    def __str__(self):
        return self.el_name

    class Meta:
        verbose_name = 'Spare part'
        verbose_name_plural = 'Spare parts'
