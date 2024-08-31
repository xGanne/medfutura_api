from django.shortcuts import render
from django.db import models
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ValidationError
from .models import Pessoa
from .serializers import PessoaSerializer

# Create your views here.
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def list(self, request, *args, **kwargs):
        termo = request.query_params.get('t', None)
        
        if termo is not None and termo.strip() == "":
            raise ValidationError({"detail": "O termo de busca não foi informado."}, code=status.HTTP_400_BAD_REQUEST)
        
        if termo:
            pessoas = Pessoa.objects.filter(
                models.Q(apelido__icontains=termo) |
                models.Q(nome__icontains=termo) |
                models.Q(stack__icontains=termo)
            )
        else:
            pessoas = Pessoa.objects.all()
        
        serializer = self.get_serializer(pessoas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pessoa.DoesNotExist:
            print("Objeto não encontrado. Levantando NotFound.")
            raise NotFound(detail="Pessoa não encontrada", code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)