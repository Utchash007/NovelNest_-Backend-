from django.db import models

# Create your models here.
class Novel(models.Model):
    novel_id = models.PositiveBigIntegerField(primary_key=True)
    novel_name = models.CharField(max_length=255)
    status = models.IntegerField()
    intro = models.TextField()
    novel_img_link = models.CharField(max_length=255)
    rating = models.FloatField(db_column='Rating')  # Field name made lowercase.
    action = models.IntegerField(db_column='Action')  # Field name made lowercase.
    adventure = models.IntegerField(db_column='Adventure')  # Field name made lowercase.
    fantasy = models.IntegerField(db_column='Fantasy')  # Field name made lowercase.
    isekai = models.IntegerField(db_column='Isekai')  # Field name made lowercase.
    slice_of_life = models.IntegerField(db_column='Slice_of_Life')  # Field name made lowercase.
    read_count = models.IntegerField(db_column='Read_Count')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'novel'


class NovelChapter(models.Model):
    novel_id = models.PositiveBigIntegerField()
    cpt_no = models.BigIntegerField()
    chapter_title = models.CharField(max_length=255)
    cpt_text = models.TextField()
    descript_id = models.AutoField(primary_key=True, db_column='Descript_ID')  # AutoField for auto-increment

    class Meta:
        managed = False
        db_table = 'novel_chapter'

class Authors(models.Model):
    novel_id = models.PositiveBigIntegerField(primary_key=True)
    author = models.CharField(db_column='Author', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authors'