from django.db import models

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.product