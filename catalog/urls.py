from django.urls import path
from . import views

# define the (empty) imported urlpatterns
urlpatterns = [
    path('', views.index, name='index'),

    path('tools/', views.ToolListView.as_view(), name='tools'),
    path('tool/<int:pk>', views.ToolDetailView.as_view(), name='tool-detail'),

    path('hosts/', views.HostListView.as_view(), name='hosts'),
    path('host/<int:pk>', views.HostDetailView.as_view(), name='host-detail'),

    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),


    path('mytools/',
         views.LoanedToolsByUserListView.as_view(),
         name='my-borrowed'),

    path('tool/<uuid:pk>/renew/',
         views.renew_tool_toolshed_admin,
         name='renew-tool-toolshed-admin'),


    path('borrowedtools/',
         views.LoanedToolsListView.as_view(),
         name='all-borrowed'),

    path('host/create/', views.HostCreate.as_view(), name='host-create'),

    path('host/<int:pk>/update/', views.HostUpdate.as_view(), name='host-update'),

    path('host/<int:pk>/delete/', views.HostDelete.as_view(), name='host-delete'),

    path('tool/create/', views.ToolCreate.as_view(), name='tool-create'),

    path('tool/<int:pk>/update/', views.ToolUpdate.as_view(), name='tool-update'),

    path('tool/<int:pk>/delete/', views.ToolDelete.as_view(), name='tool-delete'),


]
