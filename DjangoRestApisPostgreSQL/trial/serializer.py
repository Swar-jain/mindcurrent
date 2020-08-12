from rest_framework import serializers 
from trial.models import Trial
 
 
class TrialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Trial
        fields = ('id_pk',
                  'user_email',
                  'event_id',
                  'summary',
                  'start_dateTime',
                  'end_dateTime',
                  'attendee_email',
                  'location',
                  'creator_email',
                  'organizer_email',
                  'recurrence',
                  'published'
                  )
