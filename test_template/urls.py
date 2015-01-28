from django.conf.urls import url, patterns
from test_template.views import IndexView

urlpatterns = patterns(
    '',
    url(r'', IndexView.as_view()),
)
