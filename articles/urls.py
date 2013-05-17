from articles.views import ArticleList, ArticleDetail
from django.conf.urls.defaults import patterns, url
#urlpatterns = Article.get_urls()
urlpatterns = patterns('',
            url(r'^$', ArticleList.as_view(), name='article_index'),
            url(r'^(?P<slug>[a-z0-9_-]+)/$', ArticleDetail.as_view(), name='article_detail'),
        )
