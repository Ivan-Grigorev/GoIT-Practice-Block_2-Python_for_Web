from django.urls import include, path
from gymschedule.api.views import TrainingPlanView, TrainingPlanDetailView, TrainingPlanCreateView,\
    TrainingPlanUpdateView, TrainingPlanDeleteView


urlpatterns = [
    path("", TrainingPlanView.as_view(), name='list'),
    path("<slug:slug>", TrainingPlanDetailView.as_view(), name='detail'),
    path("create/", TrainingPlanCreateView.as_view(), name='create'),
    path("<slug:slug>/update/", TrainingPlanUpdateView.as_view(), name='update'),
    path("<slug:slug>/delete/", TrainingPlanDeleteView.as_view(), name='delete')
]
