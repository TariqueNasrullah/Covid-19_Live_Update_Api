from django.db import models

class CoronaData(models.Model):
    total_case = models.IntegerField(default=0, null=False)
    death = models.IntegerField(default=0, null=False)
    recovered = models.IntegerField(default=0, null=False)
    active = models.IntegerField(default=0, null=False)
    closed = models.IntegerField(default=0, null=False)

    mild = models.IntegerField(default=0, null=False)
    mild_percentage = models.FloatField(default=0.0, null=False)

    serious = models.IntegerField(default=0, null=False)
    serious_percentage = models.FloatField(default=0.0, null=False)

    recovered_or_discharged = models.IntegerField(default=0, null=False)
    recovered_or_discharged_percentage = models.FloatField(default=0.0, null=False)

    death_percentage = models.FloatField(default=0.0, null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Corona Virus Data'
        get_latest_by = 'created_at'
    
    def __str__(self):
        return str(self.created_at)
    

class CountryData(models.Model):
    name = models.CharField(max_length=500, default='_', null=False)
    total_case = models.IntegerField(default=0, null=False)
    new_case = models.IntegerField(default=0, null=False)
    death = models.IntegerField(default=0, null=False)
    new_death = models.IntegerField(default=0, null=False)
    recovered = models.IntegerField(default=0, null=False)
    active = models.IntegerField(default=0, null=False)
    serious = models.IntegerField(default=0, null=False)

    class Meta:
        verbose_name = 'Contry Data'
        ordering = ['-total_case']

    def __str__(self):
        return self.name
    
    

