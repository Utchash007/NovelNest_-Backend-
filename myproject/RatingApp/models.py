from django.db import models

from myapp.models import AuthUser
from NovelApp.models import Novel
# Create your models here.
class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    id = models.ForeignKey(AuthUser, models.CASCADE, db_column='id', blank=True, null=True)
    novel_id = models.ForeignKey(Novel, models.CASCADE, db_column='novel_id',blank=True, null=True,related_name='ratings')
    user_rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'