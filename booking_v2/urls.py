from django.urls import path
from booking_v2.views import SignUpRegisterView
from booking_v2.views import TurfBookingListCreateView,TurfBokingRetrieveUpdateDeleteView

urlpatterns = [

    path('signup/',SignUpRegisterView.as_view()),

    path('turf/booking/',TurfBookingListCreateView.as_view()),
    path('turf/booking/<int:pk>/',TurfBokingRetrieveUpdateDeleteView.as_view()),
]