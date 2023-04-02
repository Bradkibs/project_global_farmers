from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            full_name=validated_data['full_name'],
            government_id=validated_data['government_id'],
            user_type=validated_data['user_type'],
            mobile_number=validated_data['mobile_number'],
            country=validated_data['country'],
            email=validated_data['email'],
            location=validated_data['location'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['full_name', 'password', 'government_id', 'user_type', 'country', 'mobile_number', 'email', 'location']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    government_id = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        government_id = attrs.get('government_id')
        user = authenticate(email=email, password=password, government_id=government_id)
        if not user:
            raise serializers.ValidationError('Unable to log in with provided credentials.')
        if not user.is_active:
            raise serializers.ValidationError('User account is disabled.')
        refresh = RefreshToken.for_user(user)
        return user

    class Meta:
        model = User
        fields = ['full_name', 'government_id', 'email', 'password']
