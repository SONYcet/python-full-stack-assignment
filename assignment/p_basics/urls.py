from django.urls import path
from . import views
urlpatterns=[
    path('name/', views.print_name, name='print_name'),
    path('operators/', views.operators, name='operators'),
    path('loops/', views.loops, name='loops'),
    path('strings/', views.string1, name='strings'),
    path('strings/', views.string1, name='strings'),
    path('arrays/', views.arrays, name='arrays'),
    path('arrays/', views.arrays, name='arrays'),
    path('sta_variable/', views.static_variable, name='sta_variable'),
    path('inheritance/', views.main_view, name='inheritance'),
    path('access/', views.access_modifiers, name='access'),
    path('abstract/', views.abstract1, name='abstract'),
    path('dictionary/', views.studentmanager, name='dictionary'),
    path('method_overloading/', views.student_view, name='method_overloading'),
    path('packages/', views.testcalsses, name='packages'),
    path('read_file/', views.read_text_file, name='read_file'),
    path('exceptions/', views.exceptions, name='read_file'),
    path('constructors/', views.constructors, name='constructors'),

]
