from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductListView, ProductCreateView, home, test, product_list, product_detail, product_create, product_update, product_delete, products

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', home, name='home'),  # Página principal
    path('test/', test, name='test'),
    path('product-list/', product_list, name='product_list'),
    path('product-detail/<int:pk>/', product_detail, name='product_detail'),
    path('product-create/', product_create, name='product_create'),
    path('product-update/<int:pk>/', product_update, name='product_update'),
    path('product-delete/<int:pk>/', product_delete, name='product_delete'),
    path('products-api/', include(router.urls)),  # API de productos
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/add/', ProductCreateView.as_view(), name='product-add'),
    path('home/', home, name='home'),
    path('products-list/', products, name='products'),
]
