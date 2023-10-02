from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import OperationUser, UploadFile
from .serializers import OperationUserSerializer, UploadFileSerializer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

class OperationUserViewSet(viewsets.ModelViewSet):
    queryset = OperationUser.objects.all()
    serializer_class = OperationUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UploadFileViewSet(viewsets.ModelViewSet):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer
    permission_classes = [permissions.IsAuthenticated]

def upload_file(request):
    if not request.user.is_ops_user:
        return JsonResponse({'error': 'Permission denied'}, status=403)


    return JsonResponse({'message': 'File upload successfully'})

