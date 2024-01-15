from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from accounts.models import Vendor
from accounts.serializers import VendorSerializer


class VendorRegistrationSerializer(serializers.ModelSerializer):
    """Serializer class for Vendor registration

    Args:
        serializers (class): ModelSerializer
    """
    # password = serializers.CharField(write_only=True)
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        required=True,
        style={"input_type": "password"},
    )
    confirm_password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        required=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = Vendor
        fields = [
            "name",
            "username",
            "contact_details",
            "address",
            "email",
            "password",
            "confirm_password",
        ]

    def validate_username(self, username):
        if len(username) < 6 or len(username) > 15:
            raise serializers.ValidationError(
                "Username must be between 6 and 15 characters long"
            )
        return username

    def validate_password(self, password):
        special_symbols = ["$", "@", "#", "%", "!", "^", "*", "_", "=", "+", "-"]
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError(
                "Password should have at least one numeral"
            )
        if not any(char in special_symbols for char in password):
            raise serializers.ValidationError(
                "Password should have atleast one of the symbols $@#%!^*_=+-"
            )
        if not any(char.isupper() for char in password):
            raise serializers.ValidationError(
                "Password should have at least one uppercase letter"
            )
        if not any(char.islower() for char in password):
            raise serializers.ValidationError(
                "Password should have at least one lowercase letter"
            )
        return password

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                "Password and Confrim Password didn't matched"
            )
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        confirm_password = validated_data.pop("confirm_password")
        vendor = Vendor(**validated_data)
        vendor.set_password(password)
        vendor.save()
        return vendor




class VendorLoginSerializer(TokenObtainPairSerializer):
    """Serializer class for Vendor Login

    Args:
        TokenObtainPairSerializer (class): Token 
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        # data["user"] = VendorSerializer(self.user).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
