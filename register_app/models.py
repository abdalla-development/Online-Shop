from django.db import models

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=5000)
    last_name = models.CharField(max_length=5000)
    email = models.CharField(max_length=5000)
    password = models.CharField(max_length=5000)


    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    #     return self.item_name, self.image, self.category, self.price, self.quantity, self.description, self.amount, self.colors, self.sizes, self.user_id, self.done
        # return self.task + " - " + str(self.done)