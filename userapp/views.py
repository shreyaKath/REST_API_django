from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Users
from . serialisers import UsersSerializer

class UsersList(APIView):
    @api_view(['GET'])
    def user_list(request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def user_detail(request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = UsersSerializer(user)
            return Response(serializer.data)

