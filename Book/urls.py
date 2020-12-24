from django.conf.urls import url
from Book import views


urlpatterns = [

    url(r'^booklist/$', views.booklist, name='booklist'),
    url(r'^get/$', views.get, name='get'),
    url(r'^get1/$', views.get1, name='get1'),
    url(r'^get2/$', views.get2, name='get2'),
    url(r'^posttest/$', views.post_test, name='posttest'),
    url(r'index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^mine/$', views.mine, name='mine'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^cookie/$', Book.views.cookie)

]