from rest_framework import serializers
from .models import User, MembersList, ActivityPeriod


# Serializer for serializing start and end dates
class ActivityPeriodSerializer(serializers.ModelSerializer):

    # Overrides superclass method for getting required datetime representation ex- Feb 1 2020  1:33PM
    def to_representation(self, instance):
        representation = super(ActivityPeriodSerializer, self).to_representation(instance)
        representation['start_time'] = instance.start_time.strftime('%b %d %Y  %I:%M%p')
        representation['end_time'] = instance.end_time.strftime('%b %d %Y  %I:%M%p')
        return representation

    class Meta:
        model = ActivityPeriod
        exclude = ['id']


# Serializes the User model and contains nested ActivityPeriodSerializer
class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')


# Serializes the MembersList model and gives the final data
class MemberListSerializer(serializers.ModelSerializer):
   members = MemberSerializer(many=True)

   class Meta:
       model = MembersList
       fields = ('ok', 'members')