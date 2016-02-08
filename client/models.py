from django.db import models

"""
TODO:
Create models for companies and metrics. Be sure to include all required fields
(company name, company founded date, company description, company series,
company valuation, metric name, metric start and end date, and metric value).
Be mindful of the field types you use as well as the relationships you create.
Also, consider which constraints you'd want to impose. Fields for founded date,
description, series, and valuation should be able to accept NULL values. Since it
will only store currency values, the company valuation field should be a Decimal
field, whereas the metric value field need not be. You may consider adding a
__unicode__() function to each model to help with debugging.
Most of all, this should be very straightforward - don't overthink it!

You can read more about Django models here:
https://docs.djangoproject.com/en/1.8/topics/db/models/
"""
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    founded = models.CharField(max_length=12, null=True)
    description = models.CharField(max_length=2048, null=True)
    series = models.CharField(max_length=32, null=True)
    valuation = models.DecimalField(max_digits=32, decimal_places=5, null=True)
    
    class Meta:
        db_table = 'Company'

    def __unicode__(self):
        return ("%s %s %s %s %s" % (self.founded, self.name, self.series, self.valuation, self.description))

class Metric(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    start_date = models.CharField(max_length=12)
    end_date = models.CharField(max_length=12)
    value = models.IntegerField()
    company = models.ForeignKey(Company, to_field='id')
    
    class Meta:
        db_table = 'Metric'

    def __unicode__(self):
        return ("%s %s %s %s %s" % (self.name, self.start_date, self.end_date, self.company, self.value))
