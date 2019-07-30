import self
import serializer as serializer
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.decorators import api_view , permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User ,Messaging
from .serializers import Userserializer , Messagingserializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q

@api_view(['GET', 'POST'])
def index(request):
    pass
    return HttpResponse("<h1>Messaging-system Task</h1>")



@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = Userserializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_message_by_id(request,user_id):

    if request.method == 'GET':
        messaging_sender = list(Messaging.objects.filter(sender=user_id))
        messaging_reciver = list(Messaging.objects.filter(recevier=user_id))
        messaging = messaging_sender + messaging_reciver
        serializer = Messagingserializer(messaging, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def unread_message_by_id(request,user_id):
    if request.method == 'GET':
        messaging_sender = list(Messaging.objects.filter(Q(sender=user_id) &Q(readable='false')))
        messaging_reciver = list(Messaging.objects.filter(Q(recevier=user_id) & Q(readable= 'false')))
        messaging = set(messaging_sender + messaging_reciver)
        serializer = Messagingserializer(messaging, many=True)
        #if  list(serializer.data['readable']) == "false":
        structure = serializer.data
        # check = structure[0]['readable']
        # if check == 'false':
        return Response(serializer.data)
        # else:
        #     return JsonResponse({'status': 'false', 'message': "All the message have beenn red"}, status=500)



@api_view(['GET', 'POST'])
def read_message_by_id(request,message_id):
    if request.method == 'GET':
        messaging = Messaging.objects.filter(message_id=message_id)
        serializer = Messagingserializer(messaging, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST','DELETE'])
def delete_message(request,message_id):
    if request.method == 'DELETE':
        messaging = Messaging.objects.filter(message_id=message_id)
        serializer = Messagingserializer(messaging, many=True)
        structure = serializer.data
        if len(structure) == 0:
            return HttpResponse({'error: The message id doesnt exits'}, status=204)
        else:
            check = structure[0]['message_id']
            if check == message_id:
                messaging.delete()
                return HttpResponse({'The message deleted'},status=200)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def create_message(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = Messagingserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)