from rest_framework import serializers, fields
from ckuser.models import CKUser

class CKUserSerializer(serializers.ModelSerializer):
    mobile_no = serializers.ReadOnlyField(source='get_mobile_number')
    class Meta:
        model = CKUser
        fields = ("id","name","email","mobile_no")