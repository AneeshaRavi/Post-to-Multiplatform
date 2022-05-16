from django.urls import URLPattern, path
from . import views



urlpatterns =[
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('userhome',views.userhome,name='userhome'),
    path('addpost/<int:id>',views.addpost,name='addpost'),
    path('editprofile/<int:id>',views.editprofile,name="editprofile"),
    path('update/<int:id>',views.update,name='update'),
    path('doc',views.doc,name='doc'),
]
