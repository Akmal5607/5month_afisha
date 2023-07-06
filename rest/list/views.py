import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def tasks_api_view(request):
    dict_ = {
        'title': 'Hello World!',
        'description': 'Дом и двор',
        'completed': True,
        'created_at': datetime,
        }
    return Response(data=dict_)
