from django.db import models


# Create your models here.


class Transaction(models.Model):
    PROCESSING = 'processing'
    FINISHED = 'finished'
    CANCELED = 'canceled'
    STATUS = ((PROCESSING, PROCESSING), (FINISHED, FINISHED), (CANCELED, CANCELED))
    click_trans_id = models.CharField(max_length=255)
    merchant_trans_id = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    sign_string = models.CharField(max_length=255)
    sign_datetime = models.DateTimeField(max_length=255)
    status = models.CharField(max_length=25, choices=STATUS, default=PROCESSING)

    def __str__(self):
        return self.click_trans_id
