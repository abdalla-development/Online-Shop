from django.db import models

# Create your models here.

class Girls(models.Model):
    item_name  = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    price = models.IntegerField()  
    quantity = models.IntegerField()  
    description = models.CharField(max_length=500)
    amount = models.IntegerField()  
    colors = models.CharField(max_length=500)  # list
    sizes = models.CharField(max_length=500)  # list
    user_id = models.IntegerField()  
    done = models.BooleanField(default=False)  # test



    def __str__(self) -> str:
        return self.item_name
    #     return self.item_name, self.image, self.category, self.price, self.quantity, self.description, self.amount, self.colors, self.sizes, self.user_id, self.done
        # return self.task + " - " + str(self.done)