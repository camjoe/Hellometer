from django.db import models

class VendorClients(models.Model):
    vendor_id = models.IntegerField()
    arrival_time = models.DateTimeField()
    order_time = models.IntegerField()
    wait = models.IntegerField()
    payment = models.IntegerField()
    total_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendor_clients'