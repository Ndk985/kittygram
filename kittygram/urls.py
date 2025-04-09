from django.urls import path

from cats.views import CatList, CatDetail

urlpatterns = [
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
]


# from django.urls import path
# from cats.views import APICat

# # from cats.views import cat_list

# urlpatterns = [
#    # path('cats/', cat_list),
#    path('cats/', APICat.as_view()),
# ]
