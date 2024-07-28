from django.urls import path
from .views import PeopleListView, PeopleDetailView, PeopleCreateView, PeopleUpdateView, PeopleDeleteView

urlpatterns = [
    path('', PeopleListView.as_view(), name='people_list'),
    path('<int:pk>/', PeopleDetailView.as_view(), name='people_detail'),
    path('create/', PeopleCreateView.as_view(), name='people_create'),
    path('<int:pk>/edit/', PeopleUpdateView.as_view(), name='people_edit'),
    path('<int:pk>/delete/', PeopleDeleteView.as_view(), name='people_delete'),
]
