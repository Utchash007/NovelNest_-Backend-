from django.db import models

# Create your models here.
class Bookmark(models.Model):
    id = models.IntegerField()
    novel_id = models.PositiveBigIntegerField()
    cpt_no = models.BigIntegerField(blank=True, null=True)
    bookmark_id = models.AutoField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'bookmark'


class ReadHistory(models.Model):
    id = models.IntegerField()
    novel_id = models.PositiveBigIntegerField()
    cpt_no = models.BigIntegerField(blank=True, null=True)
    timeline = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'read_history'
