# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

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


#class User(models.Model):
    #user_id = models.AutoField(primary_key=True)
    #user_name = models.CharField(max_length=255)
    #user_email = models.CharField(max_length=20)
    #password = models.CharField(max_length=255)

    #class Meta:
        #managed = False
        #db_table = 'user'






class Authors(models.Model):
    novel_id = models.PositiveBigIntegerField(primary_key=True)
    author = models.CharField(db_column='Author', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authors'
