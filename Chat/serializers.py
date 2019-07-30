from rest_framework import serializers
from .models import User , Messaging

class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id','username','password']



class Messagingserializer(serializers.ModelSerializer):

    class Meta:
        model = Messaging
        fields = ['message_id' , 'sender' , 'recevier' , 'content' , 'subject' , 'creation_date' , 'readable']


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Messaging.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.message_id = validated_data.get('message_id', instance.message_id)
    #     instance.sender = validated_data.get('sender', instance.sender)
    #     instance.recevier = validated_data.get('recevier', instance.recevier)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.subject = validated_data.get('subject', instance.subject)
    #     instance.creation_date = validated_data.get('creation_date', instance.creation_date)
    #     instance.readable = validated_data.get('readable', instance.readable)
    #     instance.save()
    #     return instance