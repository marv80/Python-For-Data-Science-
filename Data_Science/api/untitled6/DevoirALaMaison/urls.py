from . import views
from django.urls import path

urlpatterns =[
    path('subject/<int:subject_id>/', views.subject_detail, name='detail'),
    path('subject/', views.i_want_a_list, name='list_of_subject'),
    path('predict/', views.predict, name='to_predict')
]
