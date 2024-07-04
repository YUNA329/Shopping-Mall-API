from rest_framework import serializers
from members.models import Member, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city', 'street', 'zipcode']

class MemberSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    
    class Meta: 
        model = Member
        fields = ['id', 'name', 'address']
        
    def create(self, validated_data):
        address_validated_data = validated_data.pop('address')
        member = Member.objects.create(**validated_data)
        Address.objects.create(member=member, **address_validated_data)
        return member
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        
        if address_data:
            address_serializer = self.fields['address']
            address_instance = instance.address
            address_serializer.update(address_instance, address_data)
        
        return instance