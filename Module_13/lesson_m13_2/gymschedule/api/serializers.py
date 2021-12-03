from rest_framework import serializers
from gymschedule.models import TrainingPlan


class TrainingPlanSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = TrainingPlan
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d %B %Y")
