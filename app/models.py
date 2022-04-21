from django.db import models

class Area(models.Model):
    msa = models.CharField(max_length=255, null=True, blank=True)
    name_msa = models.CharField(max_length=255, null=True, blank=True)
    fipstate = models.CharField(max_length=255, null=True, blank=True)
    name_country = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.msa