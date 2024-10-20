from django.urls import path
from.import views
urlpatterns = [
    path('',views.dictionary),
    path('std',views.std),
    path('fun2',views.fun2),
    path('fun3',views.fun3),
    path('fun4',views.fun4),
    path('fun5',views.fun5),
    path('fun6/<int:d>',views.fun6),
    path('fun7',views.fun7.as_view()),
    path('fun8/<int:id>',views.fun8.as_view()),
    path('fun9',views.genericapiview.as_view()),
    path('fun10/<int:id>',views.update.as_view()),




]