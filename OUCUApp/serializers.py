from rest_framework import serializers
from .models import OperationUser, UploadFile

class OperationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationUser
        fields = ('id', 'username', 'is_ops_user')

class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = ('id', 'user', 'file', 'file_type')
