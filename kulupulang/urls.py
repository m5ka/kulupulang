from django.urls import path

from .views.auth import LoginView, LogoutView
from .views.batch import NewBatchView, ShowBatchView
from .views.dictionary import IndexDictionaryView
from.views.static import DashboardView


urlpatterns = [
    path('batch/new', NewBatchView.as_view(), name='batch.new'),
    path('batch/<int:batch>', ShowBatchView.as_view(), name='batch.show'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('dictionary', IndexDictionaryView.as_view(), name='dictionary.index'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('', LoginView.as_view(), name='login'),
]
