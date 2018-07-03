from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework import permissions

from .models import Snippet


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permissoin_classss = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
