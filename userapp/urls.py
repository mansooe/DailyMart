
from django.urls import path
from.import views

urlpatterns = [
    path('',views.FrontPage,name='FrontPage'),
    path('AllShop',views.Shop,name='AllShop'),
    path('shop/vegitables',views.ShopVegitables,name='vegitables'),
    path('shop/Fruits',views.ShopFruits,name='Fruits'),
    path('shop/Dryfruits',views.ShopDryFruits,name='DryFruits'),
    path('shop/Juices',views.Shopjuices,name='Juices'),
    path('Shop/Product/<int:id>',views.SingleProduct,name='ProductView'),
    path('Login',views.LoginPage,name='Loginpage'),
    path('CreatAccount',views.CreateAccountPage,name="CreateAccountPage"),
    path('GetDataFromCreateAccount',views.GetDataFromCreateAccount,name='GetDataFromCreateAccount'),
    path('login',views.GetLoginData,name='logindata'),
    path('Logout',views.LogOut,name='LogOut'),
    path('shop/Cart',views.cartPage,name='cartpage'),
    path('About',views.AboutPage,name='aboutpage'),
    path('Contactus',views.contactPage,name='contact'),
    path('Contactus/submit',views.GetontactData,name="GetontactData"),
    path('addtocart/',views.Addtocart,name='addtocart')
    
]
