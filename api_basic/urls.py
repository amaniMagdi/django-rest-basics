
from django.urls import path, include
#from .views import article_list, article_detail, ArticleAPIView, ArticleDetails
#from .views import ArticleAPIView, ArticleDetails
#from .views import GenericAPIView
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

########
# REST Framework Routers 
########
router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')


urlpatterns = [
    
    #######
    # REST Function Based API Views &  api_view() Decorator 
    #######
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail)

    #########
    # REST Class Based API Views
    #########
    #path('article/', ArticleAPIView.as_view()),
    #path('detail/<int:id>/', ArticleDetails.as_view())

    #########
    # REST Generic Views & Mixins
    #########
    # path('generic/article/<int:id>/', GenericAPIView.as_view()),
    # path('generic/article/', GenericAPIView.as_view()),

    ########
    #  REST Framework Viewsets & Routers 
    ########
    path('viewset/', include(router.urls))
]
