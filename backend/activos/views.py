from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.conf import settings
import os
from rest_framework.decorators import api_view

# Create your views here.

class ActivosImportantesExcelAPIView(APIView):
    def get(self, request):
        excel_path = os.path.join(settings.BASE_DIR, '..', 'data', 'data.xlsx')
        try:
            df = pd.read_excel(excel_path)
            df = df[['type', 'name', 'ubication', 'code']]
            df = df.where(pd.notnull(df), None)
            data = df.to_dict(orient='records')
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def dashboard(request):
    return render(request, '../../frontend/templates/dashboard.html')

@api_view(['GET'])
def health_check(request):
    return Response({'status': 'ok', 'backend': 'online'})
