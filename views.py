from django.shortcuts import render
from multioption.models import ColorsModel
from multioption.serialize import Colorserialize
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def insertcolors():
    if request.method=="POST":
        colorsserializeobj.is_valid():
        colorserializepbj.save()
        return Response(Colorserializeobj.data)

def insertdata(request):
    return render(request,'index.html')