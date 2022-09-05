from tkinter import Image
from django.shortcuts import render

# Create your views here.
from .models import Tables

# Assuming the data to be entered is presnet in these lists
table_img = ['https://freeimage.host/i/img1.6lRFGn','https://freeimage.host/i/6lRHTN','https://freeimage.host/i/6lRK4s','https://freeimage.host/i/6lRJjI','https://freeimage.host/i/6lRdQt','https://freeimage.host/i/6lR3CX','https://freeimage.host/i/6lRq3G','https://freeimage.host/i/6lRBaf','https://freeimage.host/i/6lRCv4','https://freeimage.host/i/6lRnyl','https://freeimage.host/i/6lRxu2','https://freeimage.host/i/6lRzjS','https://freeimage.host/i/6lRIZ7','https://freeimage.host/i/6lRun9']

table_red = [1,1,4,3,5,3,6,2,3,2,2,4,6,4]
table_yellow = [2,2,2,4,1,4,1,3,1,5,1,3,2,3]
table_white = [3,8,1,2,3,2,5,4,5,4,6,2,4,1]
table_orange = [4,4,6,5,2,1,2,1,4,6,3,1,1,2]
table_violet = [0,5,5,1,4,6,7,5,6,1,5,0,3,5]
table_green = [5,3,7,0,6,7,4,0,2,3,4,5,5,0]
table_pink = [0,6,3,6,0,5,3,0,0,0,7,0,7,0]

def my_view(request, *args, **kwargs):
    
    # Iterate through all the data items
    for i in range(len(table_img)):

        # Insert in the database
        Tables.objects.create(Image = table_img[i], red = table_red[i],yellow = table_yellow[i],white = table_white[i],orange = table_orange[i],violet = table_violet[i],green = table_green[i],pink = table_pink[i] )


    # Getting all the stuff from database
    query_results = Tables.objects.all();

    # Creating a dictionary to pass as an argument
    context = { 'query_results' : query_results }

    # Returning the rendered html
    return render(request, "template/index.html", context)