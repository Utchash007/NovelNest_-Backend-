# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authors(models.Model):
    novel_id = models.PositiveBigIntegerField(primary_key=True)
    author = models.CharField(db_column='Author', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authors'


class Bookmark(models.Model):
    id = models.IntegerField()
    novel_id = models.PositiveBigIntegerField()
    cpt_no = models.BigIntegerField(blank=True, null=True)
    bookmark_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bookmark'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    descript_id = models.AutoField(db_column='Descript_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'novel_chapter'


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id', blank=True, null=True)
    novel = models.ForeignKey(Novel, models.DO_NOTHING, blank=True, null=True)
    user_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class ReadHistory(models.Model):
    id = models.IntegerField()
    novel_id = models.PositiveBigIntegerField()
    cpt_no = models.BigIntegerField(blank=True, null=True)
    timeline = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'read_history'


class UserBackup(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_backup'
