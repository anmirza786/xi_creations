from django.urls import path, include
from core.models.ourclients_model import OurClient
from core.views import *

urlpatterns = [
    path('blogs/', BlogsListView.as_view()),
    path('blog/<int:pk>/', SingleBlogView.as_view()),
    path('works/', WorkListApiView.as_view()),
    path('work/<int:pk>/', SingleWorkApiView.as_view()),
    path('testimonials/', TestimonialListApiView.as_view()),
    path('staff/', StaffListView.as_view()),
    path('clients/', OurClientView.as_view()),
    path('contact/', ContactApiView.as_view()),
]
