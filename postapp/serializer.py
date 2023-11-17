from rest_framework import serializers
from postapp.models import *

class PostSerializer(serializers.Serializer):
    class Meta:
        fields:(
            'user_id',
            'title',
            'message',
        )
class UserSerializer(serializers.Serializer):
    class Meta:
        fields=(
            'user_id',
            'name',
            'email',
            'password',
            'password'
        )