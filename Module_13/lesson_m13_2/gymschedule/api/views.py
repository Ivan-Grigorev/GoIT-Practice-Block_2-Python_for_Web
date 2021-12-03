from rest_framework import viewsets
from gymschedule.models import TrainingPlan
from gymschedule.api.serializers import TrainingPlanSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class TrainingPlanView(ListAPIView):
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
    permission_classes = [IsAuthenticated]


class TrainingPlanDetailView(RetrieveAPIView):
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'


class TrainingPlanCreateView(CreateAPIView):
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class TrainingPlanUpdateView(RetrieveUpdateAPIView):
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser]


class TrainingPlanDeleteView(RetrieveDestroyAPIView):
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser]
