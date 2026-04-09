from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Conversation
from .serializers import ConversationSerializer

from agents.graph import build_graph

graph = build_graph()


@api_view(['POST'])
def ask_question(request):
    question = request.data.get("question")

    if not question:
        return Response({"error": "Question required"}, status=400)

    # Run agents
    result = graph.invoke({"question": question})

    answer = result.get("answer")

    convo = Conversation.objects.create(
        question=question,
        answer=answer
    )

    return Response({
        "id": convo.id,
        "question": question,
        "answer": answer
    })

@api_view(['GET'])
def get_conversations(request):
    data = Conversation.objects.all().order_by('-created_at')
    serializer = ConversationSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_conversation(request, pk):
    try:
        convo = Conversation.objects.get(pk=pk)
    except Conversation.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = ConversationSerializer(convo)
    return Response(serializer.data)

@api_view(['PUT'])
def update_conversation(request, pk):
    try:
        convo = Conversation.objects.get(pk=pk)
    except Conversation.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = ConversationSerializer(convo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_conversation(request, pk):
    try:
        convo = Conversation.objects.get(pk=pk)
    except Conversation.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    convo.delete()
    return Response({"message": "Deleted successfully"})