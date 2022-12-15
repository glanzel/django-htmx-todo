from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['url', 'name', 'status', 'description']


