from django.urls import include, path
from rest_framework import routers

from .views.api.word import BatchViewSet, WordViewSet
from .views.auth import SettingsView, LoginView, LogoutView
from .views.batch import (
    AddContributorBatchView,
    EditBatchView,
    IndexBatchView,
    NewBatchView,
    OvenBatchView,
    PromoteBatchView,
    ShowBatchView,
    SubmitBatchView,
    UnsubmitBatchView,
)
from .views.dictionary import IndexDictionaryView, ShowDictionaryView
from .views.discussion import (
    IndexDiscussionView,
    NewDiscussionView,
    ResolveDiscussionView,
)
from .views.static import DashboardView
from .views.word import DeleteWordView, EditWordView, NewWordView, ShowWordView


router = routers.DefaultRouter()
router.register(r"batches", BatchViewSet)
router.register(r"words", WordViewSet)


urlpatterns = [
    path("batch", IndexBatchView.as_view(), name="batch.index"),
    path("batch/new", NewBatchView.as_view(), name="batch.new"),
    path("batch/<int:batch>/word/new", NewWordView.as_view(), name="word.new"),
    path("batch/<int:batch>/word/<int:word>", ShowWordView.as_view(), name="word.show"),
    path(
        "batch/<int:batch>/word/<int:word>/edit",
        EditWordView.as_view(),
        name="word.edit",
    ),
    path(
        "batch/<int:batch>/word/<int:word>/delete",
        DeleteWordView.as_view(),
        name="word.delete",
    ),
    path(
        "batch/<int:batch>/contributor",
        AddContributorBatchView.as_view(),
        name="batch.add_contributor",
    ),
    path("batch/<int:batch>/edit", EditBatchView.as_view(), name="batch.edit"),
    path("batch/<int:batch>/submit", SubmitBatchView.as_view(), name="batch.submit"),
    path(
        "batch/<int:batch>/unsubmit", UnsubmitBatchView.as_view(), name="batch.unsubmit"
    ),
    path(
        "batch/<int:batch>/discuss", NewDiscussionView.as_view(), name="discussion.new"
    ),
    path("batch/<int:batch>/promote", PromoteBatchView.as_view(), name="batch.promote"),
    path("batch/<int:batch>", ShowBatchView.as_view(), name="batch.show"),
    path("oven", OvenBatchView.as_view(), name="batch.oven"),
    path("discussion", IndexDiscussionView.as_view(), name="discussion.index"),
    path(
        "discussion/<int:discussion>/resolve",
        ResolveDiscussionView.as_view(),
        name="discussion.resolve",
    ),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("dictionary", IndexDictionaryView.as_view(), name="dictionary.index"),
    path("dictionary/<str:slug>", ShowDictionaryView.as_view(), name="dictionary.show"),
    path("settings", SettingsView.as_view(), name="settings"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("api/", include(router.urls)),
    path("", LoginView.as_view(), name="login"),
]
