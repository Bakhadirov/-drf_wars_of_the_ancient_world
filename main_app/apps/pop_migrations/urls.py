from django.urls import path

from main_app.apps.pop_migrations.api.views.pop_migrations import MainTableView

urlpatterns = [
    path('main_table/', MainTableView.as_view()),

               ]


