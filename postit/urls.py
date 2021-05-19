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
]


"""
    
    path('edit_note', views.xxx, name = 'edit_note'),
    path('del_note', views.xxx, name = 'del_note'),
    path('add_fav', views.xxx, name = 'add_fav'),
    path('favs', views.xxx, name = 'favs')
"""