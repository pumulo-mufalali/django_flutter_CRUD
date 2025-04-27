from django.core.serializers import serialize
from rest_framework.response import Response
from .serializer import NoteSerializer
from .models import NoteModel
from rest_framework.decorators import api_view


@api_view(['GET'])
def getNotes(request):
    notes = NoteModel.objects.all()
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = NoteModel.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data

    note = NoteModel.objects.create(
        text=data['text']
    )
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = NoteModel.objects.get(id=pk)

    serializer = NoteSerializer(note, data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = NoteModel.objects.get(id=pk)

    note.delete()
    return Response("Note was deleted!")