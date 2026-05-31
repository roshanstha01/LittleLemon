from django.db import models


class Booking(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Booking'


class Menu(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

    class Meta:
        db_table = 'Menu'
