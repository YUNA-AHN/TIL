from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Music
from .serializers import MusicListSerializers, MusicSerializers

@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializers(musics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE','PUT'])
def music_detail(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializers(music)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete' : f'데이터 {music_pk}번 글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MusicSerializers(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)