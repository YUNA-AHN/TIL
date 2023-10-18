from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Music

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer

# Create your views here.
def music_html(request):
    musics = Music.objects.all()
    context = {
        "musics": musics,
    }
    return render(request, "music/music.html", context)


def music_json_1(request):
    musics = Music.objects.all()
    musics_json = []

    for music in musics:
        musics_json.append(
            {
                "id": music.pk,
                "title": music.title,
                "content": music.content,
            }
        )
    return JsonResponse(musics_json, safe=False)


def music_json_2(request):
    musics = Music.objects.all()
    data = serializers.serialize(
        "json",
        musics,
        fields=(
            "title",
            "content",
        ),
    )
    return HttpResponse(data, content_type="application/json")

@api_view(['GET'])
def music_json_3(request):
    musics =  Music.objects.all()
    serializers = MusicSerializer(musics, many=True)
    return Response(serializers.data)
