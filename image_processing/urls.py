from django.urls import path
from .views import UploadCSV, CheckStatus

urlpatterns = [
    path('upload/', UploadCSV.as_view(), name='upload-csv'),
    path('status/<str:request_id>/', CheckStatus.as_view(), name='check-status'),
]
