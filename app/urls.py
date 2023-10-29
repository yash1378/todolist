from django.urls import path
from . import views




'''In the urlpatterns list, you define URL patterns. Each URL pattern is defined using the path function, which takes three arguments:
The first argument is the URL pattern as a string. In this case, it's 'members/', so this pattern matches the URL /members/. This means
when a user's web browser requests the URL /members/, the associated view function will be called.
The second argument is the view function that should be called when this URL pattern is matched. In this case, it's views.members, which 
references the members function defined in your views module.
The name argument assigns a name to this URL pattern. This name can be used in other parts of your Django application to refer to this 
specific URL pattern, making it easier to reverse URL patterns and generate links.
'''
app_name = "app"
urlpatterns = [
    
    path("", views.main, name="main"),
    path('add/', views.receive_data, name='receive_data'),

]

#Using Generic Views
# app_name = "app"

# urlpatterns = [
#     path("", views.MainView.as_view(), name="main"),
#     path('add/', views.ReceiveDataView.as_view(), name='receive_data'),
# ]