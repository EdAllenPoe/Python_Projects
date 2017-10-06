from django.conf.urls import url
from views import *
# from django.contrib import admin

urlpatterns = [
    url(r'^home$', home, name = "home"),
    url(r'^add_book$', add_book, name="add_book"),
    url(r'^create_review/(?P<id>\d+)$', create_review, name="create_review"),
    url(r'^show/(?P<id>\d+)$', show, name="show"),
    url(r'^user/(?P<id>\d+)$', user, name="user"),
    url(r'^destroy/(?P<id>\d+)$', destroy, name="destroy"),
    # url(r'^admin/', admin.site.urls),
]
