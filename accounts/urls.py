
from django.conf.urls import url
from.import views


app_name= 'accounts'

urlpatterns = [
    url(r'^signup/$',views.signup_view,name="signup"),
    url(r'^login/$',views.login_view,name="login"),
    url(r'^logout/$',views.logout_view,name="logout"),
    url(r'^password_change/$',views.password_change_view,name='password_change'),
#    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

]
