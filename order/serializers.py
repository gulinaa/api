from rest_framework import serializers
from .models import Order
from account.celery import send_order_info


class OrderSerializer(serializers.ModelSerializer):
    guest = serializers.ReadOnlyField(source='guest.email')
    hotel = serializers.ReadOnlyField(source='hotel.name')

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        guest = request.user
        guesthouse = validated_data.get('guesthouse')
        hotel = guesthouse.hotel
        validated_data['guest'] = guest
        validated_data['hotel'] = hotel
        message = []
        for i in validated_data:
            val = validated_data.get(i)
            message.extend([f'{i}: {val}'])
        message = '\n'.join(message)
        send_order_info.delay(validated_data['email'], message)
        return super().create(validated_data)