
from django.urls import path
from .import views
import adminapp

urlpatterns = [
    path('dailyadmin',views.adminpage,name='dailyadmin'),
    path('CatergoryTable',views.CategoryTable,name='CatergoryTable'),
    path('Addcategory',views.Addcategory,name='Addcategory'),
    path('Addcategorydata',views.Addcategorydata,name='Addcategorydata'),
    path('Tableslist',views.Tableslist,name='Tableslist'),
    path('Deletecategory/<int:id>',views.Deletecategory,name='Deletecategory'),
    path('Addproduct',views.Addproduct,name='Addproduct'),
    path('AddnewProduct',views.AddnewProduct,name='AddnewProduct'),
    path('ProductTable',views.ProductTable,name='ProductTable'),

    path('UpdateProductDetail/<int:id>',views.UpdateProductDetail,name='UpdateProductDetail')
    
]
