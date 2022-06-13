from django.shortcuts import render

from django.shortcuts import render
from .serializers import movieSerializer
from .models import movies
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


@csrf_exempt
def crud(request):
    if request.method == "GET":
        movie = movies.objects.all()
        serializer = movieSerializer(movie,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")

    if request.method == "POST": 
        data = request.body
        strem = io.BytesIO(data)
        python_data = JSONParser().parse(strem)
        serializer = movieSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            msg={"message":"data created"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json") 

@csrf_exempt
def crudsingle(request,pk):
    if request.method == "GET":
        obj = movies.objects.get(id=pk)
        serializer = movieSerializer(obj)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")

    if request.method == "PUT":
        data = request.body
        strem = io.BytesIO(data)
        python_data = JSONParser().parse(strem)
        obj = movies.objects.get(id=pk)   
        serializer = movieSerializer(obj,data = python_data,partial=True) 
        if serializer.is_valid():
            serializer.save()
            msg={"message":"data updated"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")

    if request.method == "DELETE":
        obj = movies.objects.get(id=pk)
        obj.delete()
        msg={"message":"data deleted"}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type="application/json")

