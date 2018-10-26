from articles.views import ArticleList, ArticleDetail

from django.conf.urls import url

urlpatterns = [
    url(r'^$', ArticleList.as_view(), name='article_index'),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', ArticleDetail.as_view(), name='article_detail')
]

