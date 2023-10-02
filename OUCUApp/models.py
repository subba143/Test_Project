from django.db import models
# Create your models here.

class OperationUser(models.Model):
    username = models.CharField(max_length=33)
    password = models.CharField(max_length=70)
    is_ops_user = models.BooleanField(default=False)

class UploadFile(models.Model):
    user = models.ForeignKey(OperationUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=10)  # 'pptx', 'docx', or 'xlsx'

class AccessToken(models.Model):
    user = models.ForeignKey(OperationUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=90)
