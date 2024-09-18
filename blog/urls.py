from django.urls import path
from . import views

"""
https://tutorial.djangogirls.org/en/django_urls/

As you can see, we're now assigning a view called post_list to the root URL. 
This URL pattern will match an empty string and the Django URL resolver will ignore 
the domain name (i.e., http://127.0.0.1:8000/) that prefixes the full URL path. This 
pattern will tell Django that views.post_list is the right place to go if someone 
enters your website at the 'http://127.0.0.1:8000/' address.

The last part, name='post_list', is the name of the URL that will be used to identify 
the view. This can be the same as the name of the view but it can also be something 
completely different.
"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path ('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]

"""
This part post/<int:pk>/ specifies a URL pattern - we will explain it for you:

post/ means that the URL should begin with the word post followed by a /. So far so good.

<int:pk> - this part is trickier. It means that Django expects an integer value and will transfer it to a view as a variable called pk.

/ - then we need a / again before finishing the URL.

That means if you enter http://127.0.0.1:8000/post/5/ into your browser, Django will understand that you are looking for a view called post_detail and transfer the information that pk equals 5 to that view.
"""
