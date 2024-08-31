from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def validate_apelido(self, value):
        if not value:
            raise serializers.ValidationError("Apelido é obrigatório.")
        return value

    def validate_nome(self, value):
        if not value:
            raise serializers.ValidationError("Nome é obrigatório.")
        return value

    def validate_nascimento(self, value):
        if not value:
            raise serializers.ValidationError("Data de nascimento é obrigatória.")
        return value

    def validate_stack(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Stack deve ser uma lista de strings.")
            for item in value:
                if not isinstance(item, str):
                    raise serializers.ValidationError("Cada elemento da stack deve ser uma string.")
                if len(item) > 32:
                    raise serializers.ValidationError("Cada elemento da stack deve ter no máximo 32 caracteres.")
        return value