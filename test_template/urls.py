from django.conf.urls import url, patterns
from test_template.views import (IndexView, TestCache)

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view()),
    url(r'^cache$', TestCache.as_view()),
)
