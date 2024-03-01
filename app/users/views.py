from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
from .models import UserModel
from .serializers.serializers import RegisterUserSerializer, AllUserSerializer
from django.contrib.auth.hashers import make_password


class CreateUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            # Encripta la contraseña antes de guardar el usuario
            validated_data = serializer.validated_data
            validated_data['password'] = make_password(
                validated_data['password'])
            print(validated_data)

            serializer.save()
            return Response(data={'msg': 'Se ha creado exitosamente el usuario', 'data': serializer.data}, status=201)
        return Response(data={'msg': 'Ah ocurrido un error dentro de la creacion del usuario', 'data': serializer.errors}, status=400)


class AllUserView(ListAPIView):
    serializer_class = AllUserSerializer
    queryset = UserModel.objects.all()


class DeleteUserView(DestroyAPIView):
    serializer_class = AllUserSerializer

    def delete(self, request, pk: int, **kwargs):
        user = UserModel.objects.filter(id=pk).first()
        serializer = AllUserSerializer(user)
        if user is None:
            return Response(data={'msg': 'El usuario que enviaste no existe'}, status=404)
        user.delete()
        return Response(data={'msg': 'Se logro eliminar exitosamente', 'data': serializer.data}, status=201)
