from django.conf.urls.defaults import *
from pyladies.jobs.views import JobList,JobDetail

urlpatterns = patterns('',
    (r'(?P<company_slug>[-\w]+)/(?P<slug>[-\w]+)', JobDetail.as_view()),
    (r'(?P<company_slug>[-\w]+)/$', JobList.as_view()),
    (r'$', JobList.as_view()),

)