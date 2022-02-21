from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register' ) ,
    path('login/', views.loginPg, name='login' ) ,
    path('signout', views.signoutPg, name='signout'),
    path('home/', views.home, name='home' ) ,
    path('subscribe/<int:id>',views.subscribe,name='subscribe-to-category'),
    path('unsubscribe/<int:id>',views.unsubscribe,name='unsubscribe-to-category'),
    path('like/<int:id>',views.like,name='like'),
    path('unlike/<int:id>',views.unlike,name='unlike'),
    path('dislike/<int:id>',views.dislike,name='dislike'),
    path('undislike/<int:id>',views.undislike,name='undislike'),
    path('u_add', views.addUser,name='uadd'),    
    path('del/<u_id>', views.delUser,name='udel'),
    path('edit/<u_id>', views.editUser,name='uedit'),
    path('p_add', views.addPost,name='padd'),
    path('pedit/<p_id>', views.editPost,name='pedit'),
    path('blog/', views.manageBlog, name='blog' ) ,
    path('pdelete/<p_id>', views.delPost,name='pdelete'),
    path('post/<p_id>', views.showPost, name='p_show' ) ,
    path('search', views.search, name='search' ) ,
    path('w_add', views.addWord,name='Wadd'),
    path('w_edit/<w_id>', views.editWord,name='Wedit'),
    path('w_del/<w_id>', views.delWord,name='Wdelete'),
    path('cat_add', views.addCatagory,name='Cadd'),
    path('cat_edit/<cat_id>', views.editCatagory,name='Cedit'),
    path('cat_del/<cat_id>', views.delCatagory,name='Cdelete'), 
    path('categoryposts/<c_id>', views.categoryposts,name='categoryposts'), 
]