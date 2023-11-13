from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from api.models import Task
from api.serializers import TaskSerializer, RegisterUserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for the Task model.
    """

    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the tasks
        for the currently authenticated user.
        """
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Save the post data when creating a new task.
        """
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a task instance.
        """
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {"error": "You don't have permission to view this task."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Update a task instance.
        """
        task = self.get_object()
        if task.user != request.user:
            return Response(
                {"error": "You don't have permission to edit this task."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a task instance.
        """
        task = self.get_object()
        if task.user != request.user:
            return Response(
                {"error": "You don't have permission to delete this task."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request):
        """
        Create a new user.

        - **username**: User's username.
        - **password**: User's password.

        Returns:
        - **id**: User ID.
        - **username**: User's username.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        user = User.objects.create_user(username=username, password=password)
        return Response(
            {"id": user.id, "username": user.username}, status=status.HTTP_201_CREATED
        )
