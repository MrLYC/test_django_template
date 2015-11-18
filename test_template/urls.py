from django.conf.urls import url, patterns
from test_template.views import (
    IndexView, TestCache, TestSQL, TestExcel,
)

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view()),
    url(r'^cache$', TestCache.as_view()),
    url(r'^sql$', TestSQL.as_view()),
    url(r'^excel$', TestExcel.as_view()),
)
