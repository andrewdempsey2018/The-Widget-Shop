from django.db import models

from widget.models import Widget

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.full_name, self.country)

#class OrderLineItem(models.Model):
#    order = models.ForeignKey(Order, null=False, on_delete=models.DO_NOTHING)
#    widget = models.ForeignKey(Widget, null=False, on_delete=models.DO_NOTHING)
#    quantity = models.IntegerField(blank=False)

#   def __str__(self):
#        return "{0} {1} @ {2}".format(self.quantity, self.widget.name, self.widget.price)