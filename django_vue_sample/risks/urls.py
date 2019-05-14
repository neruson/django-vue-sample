from django.urls import path

from . import views

urlpatterns = [
    path("", views.RiskTypeListView.as_view(), name="risk_type_list"),
    path("<int:pk>/", views.RiskTypeDetailView.as_view(), name="risk_type_detail"),
]
