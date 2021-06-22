from django.urls import path
from . import views

app_name = 'postit'

urlpatterns = [
    path('', views.IndexListView.as_view(), name = 'index'),
    path('add_note', views.add_note, name = 'add_note'),
    path('del_all', views.del_all, name = "del_all"),
    path('mark_all', views.mark_all, name = "mark_all"),
    path('unmark_all', views.unmark_all, name = "unmark_all"),
    path('update_note', views.update_note, name = "update_note"),
    path('delete_note/<int:id>', views.delete_note, name = 'delete_note'),
    path('mark_note/<int:id>', views.mark_note, name = 'mark_note'),
]