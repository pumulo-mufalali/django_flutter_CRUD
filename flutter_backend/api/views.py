from rest_framework.response import Response
from .serializer import NoteSerializer
from .models import NoteModel
from rest_framework.decorators import api_view


@api_view(['GET'])
def getNotes(request):
    notes = NoteModel.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)