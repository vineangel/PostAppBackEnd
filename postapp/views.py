from django.shortcuts import render
from postapp.models import *
from postapp.serializer import*
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
# Create your views here.

@csrf_exempt
def viewAll(request):
    if request.method == "GET":
        postlist = PostDetails.objects.all()
        serialise_data=PostSerializer(postlist,many=True)
        return HttpResponse(json.dumps(serialise_data.data))
    
@csrf_exempt
def add(request):
    if request.method=="POST":
        received_data = json.loads(request.body)
        print(received_data)
        serializer_check = PostSerializer(data=received_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status": "success"}))
        else:
            return HttpResponse(json.dumps({"status": "fail"}))

@csrf_exempt 
def search(request):
    if request.method=="POST":
        received_data = json.loads(request.body)
        getAdmno=received_data["admno"]
        # here use list instead of array
        data=list(PostDetails.objects.filter(Q(admno__icontains=getAdmno)))
        return HttpResponse(json.dumps(data))
 
