from tortoise import fields, models

class DataGeneral(models.Model):
    key = fields.CharField(pk=True, max_length=255)  # Primary key
    value = fields.TextField()                       # Text value

class DataAdBroadcast(models.Model):
    key = fields.CharField(pk=True, max_length=255)  # Primary key
    value = fields.TextField()                       # Text value

class DataEmbeds(models.Model):
    key = fields.CharField(pk=True, max_length=255)  # Primary key
    value = fields.TextField()                       # Text value

class DataEmbedThumbnails(models.Model):
    key = fields.CharField(pk=True, max_length=255)  # Primary key
    value = fields.TextField()  # Text value
