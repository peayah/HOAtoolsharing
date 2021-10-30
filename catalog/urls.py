from django.urls import path
from . import views

# define the (empty) imported urlpatterns
urlpatterns = [
    path('', views.index, name='index'),

    path('tools/', views.ToolListView.as_view(), name='tools'),
    path('tool/<int:pk>', views.ToolDetailView.as_view(), name='tool-detail'),

    path('hosts/', views.HostListView.as_view(), name='hosts'),
    path('host/<int:pk>', views.HostDetailView.as_view(), name='host-detail'),

    path('mytools/',
         views.LoanedToolsByUserListView.as_view(),
         name='my-borrowed'),

    path('tool/<uuid:pk>/renew/',
         views.renew_tool_toolshed_admin,
         name='renew-tool-toolshed-admin'),

    path('borrowedtools/',
         views.LoanedToolsListView.as_view(),
         name='all-borrowed'),
]
