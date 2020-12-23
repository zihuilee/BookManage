from django.conf.urls import url
from Book import views


urlpatterns = [

    url(r'^booklist/$', views.booklist, name='booklist'),
    url(r'^get/$', views.get, name='get'),
    url(r'^get1/$', views.get1, name='get1'),
    url(r'^get2/$', views.get2, name='get2'),
    url(r'^posttest/$', views.post_test, name='posttest'),
    # url(r'^cookie/$', Book.views.cookie)

]