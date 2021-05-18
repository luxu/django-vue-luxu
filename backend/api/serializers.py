from rest_framework import serializers

from backend.api.models import Message, Sentenciado, Pavilhao


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class SentenciadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentenciado
        fields = ('nome', 'matricula', 'pavilhao')


class PavilhaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pavilhao
        fields = ('numero', 'capacidade', 'restante')

