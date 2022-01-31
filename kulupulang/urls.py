from django.urls import path

from .views.auth import LoginView, LogoutView
from .views.batch import NewBatchView, ShowBatchView
from .views.dictionary import IndexDictionaryView
from .views.root import NewRootView
from .views.static import DashboardView
from .views.word import NewWordView


urlpatterns = [
    path('batch/new', NewBatchView.as_view(), name='batch.new'),
    path('batch/<int:batch>/root/new', NewRootView.as_view(), name='root.new'),
    path('batch/<int:batch>/word/new', NewWordView.as_view(), name='word.new'),
    path('batch/<int:batch>', ShowBatchView.as_view(), name='batch.show'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('dictionary', IndexDictionaryView.as_view(), name='dictionary.index'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('', LoginView.as_view(), name='login'),
]
