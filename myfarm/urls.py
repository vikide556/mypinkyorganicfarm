from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("products/", views.product_view, name="product_list"),

    # path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
    path("product/<slug:slug>/", views.single_product_detail, name="single_product_detail"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("blog/", views.blog_view, name="blog"),
    path("gallery/", views.gallery_view, name="gallery"),
    path("faq/", views.faq_view, name="faq"),

]

