from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from .models import Message


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_messages(request):
    messages = Message.objects.filter(parent_message__isnull=True)\
        .select_related('sender', 'receiver', 'parent_message')\
        .prefetch_related('replies')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unread_messages(request):
    messages = Message.unread.unread_for_user(request.user).only(
        'id', 'sender', 'receiver', 'content', 'timestamp', 'read'
    )
    serializer = MessageSerializer(messages, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sender=request.user)  # sender is auto-set
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({"message": "User account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)