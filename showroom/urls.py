
from django.contrib import admin
from django.urls import path
from .views import CreateCarDetailsView,ShowRoomLogout,ShowRoomPosts,\
    CreatePost,ViewPosts,CreatePostPhotos,EditViewPhotos,\
    Viewphotos,HideCarDetails,InactivePost,ActivePost,PhotoPageView

urlpatterns = [
    path("login",CreateCarDetailsView.as_view(),name="login"),
    path("homepage",ShowRoomPosts.as_view(),name="homepage"),
    path("logout",ShowRoomLogout.as_view(),name="logout"),
    path("create",CreatePost.as_view(),name="create"),
    path("view/<int:pk>",ViewPosts.as_view(),name="view"),
    path("photos<int:pk>",CreatePostPhotos.as_view(),name="photos"),
    path("viewphoto",Viewphotos.as_view(),name="viewphoto"),
    path("editphoto/<int:pk>",EditViewPhotos.as_view(),name="editphoto"),
    path("hidedetails/<int:pk>",HideCarDetails.as_view(),name="hidedetails"),
    path("hidepost",InactivePost.as_view(),name="hidepost"),
    path("activepost/<int:pk>",ActivePost.as_view(),name="activepost"),
    path("photopage/<int:pk>",PhotoPageView.as_view(),name="photopage"),
]
