
from django.urls import path
#from .views import article_list, article_detail, ArticleAPIView, ArticleDetails
from .views import ArticleAPIView, ArticleDetails

urlpatterns = [
    #######
    # REST Function Based API Views &  api_view() Decorator 
    #######
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail)

    #########
    # REST Class Based API Views
    #########
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view())
]
