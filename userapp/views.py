
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from requests import Response

from adminapp.models import CategoryDb, ProductDb
from django.core.paginator import Paginator

from userapp.models import ContactusDb, UserDb
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def FrontPage(request):
    Allproducts=ProductDb.objects.all().order_by('?')[:24]
    

    return render(request,'Userindex.html',{'obj':Allproducts})
def Shop(request):
    products=ProductDb.objects.order_by('?')

    paginator_product=Paginator(products,8)
    page_number=request.GET.get('page')

    page_obj=paginator_product.get_page(page_number)

    return render(request,'shop.html',{'obj':page_obj})
def ShopVegitables(request):
    products=ProductDb.objects.filter(productcategory='Vegitables')

    paginator_product=Paginator(products,8)
    page_number=request.GET.get('page')
    page_obj=paginator_product.get_page(page_number)

    c_catogory=CategoryDb.objects.get(CategoryName='Vegitables')
  
    return render(request,'ShopItems/shopVegitables.html',{'obj':page_obj,'category':c_catogory})
def ShopFruits(request):
    products=ProductDb.objects.filter(productcategory='Fruits')
    Paginator_products=Paginator(products,8)
    page_number=request.GET.get('page')
    page_obj=Paginator_products.get_page(page_number)

    c_catogory=CategoryDb.objects.get(CategoryName='Fruits')
   
    return render(request,'ShopItems/ShopFruits.html',{'obj':page_obj,'category':c_catogory})
def ShopDryFruits(request):
    products=ProductDb.objects.filter(productcategory='DryFruits')
    Paginator_products=Paginator(products,8)
    page_number=request.GET.get('page')
    page_obj=Paginator_products.get_page(page_number)

    c_catogory=CategoryDb.objects.get(CategoryName='DryFruits')
    return render(request,'ShopItems/shopDryfruits.html',{'obj':page_obj,'category':c_catogory})

def Shopjuices(request):
    products=ProductDb.objects.filter(productcategory='Juices')
    Paginator_products=Paginator(products,8)
    page_number=request.GET.get('page')
    page_obj=Paginator_products.get_page(page_number)

    c_catogory=CategoryDb.objects.get(CategoryName='Juices')
    return render(request,'ShopItems/shopjuices.html',{'obj':page_obj,'category':c_catogory})    
def SingleProduct(request,id):
    obj=ProductDb.objects.get(id=id)

    for i in CategoryDb.objects.all():
        if i.CategoryName==obj.productcategory:
            category_objects=ProductDb.objects.filter(productcategory=obj.productcategory).order_by('?')[:4]

    return render(request,'Product-single.html',{'obj':obj,'categoryporducts':category_objects})    
def LoginPage(request):
    return render(request,'Login.html')
def CreateAccountPage(request):
    return render(request,'CreateAccount.html')
def GetDataFromCreateAccount(request):
    if request.method=='POST':
        m_username=request.POST.get('username')
        m_password=request.POST.get('password')
        m_email=request.POST.get('email')
        data=UserDb(password=m_password,username=m_username,email=m_email)
        data.save()
    return redirect(LoginPage)
def GetLoginData(request):
    c_username=request.POST.get('username')
    c_password=request.POST.get('password')

    if UserDb.objects.filter(username=c_username,password=c_password).exists():
        c_data=UserDb.objects.filter(username=c_username,password=c_password).values('email','id').first()
        request.session['email']=c_data['email']
        request.session['userid']=c_data['id']
        request.session['password']=c_password
        request.session['username']=c_username
        return redirect(FrontPage)
    else:
        return redirect(CreateAccountPage)


def LogOut(request):
    del request.session['username']
    del request.session['password']

    return redirect(FrontPage)
    
@csrf_exempt
def Addtocart(request):

    if request.is_ajax():
        product_id=request.POST.get('id',None)
        print("productid=======================|",product_id)
        return JsonResponse(response)
        

def cartPage(request):
    return render(request,'cart.html')
def AboutPage(request):
    return render(request,'about.html')
def contactPage(request):
    return render(request,'contact.html')    
def GetontactData(request):
    if request.method=='POST':
        m_name=request.POST.get('name')
        m_email=request.POST.get('email')
        m_message=request.POST.get('messege')
        m_subject=request.POST.get('subject')    

        m_Data=ContactusDb(name=m_name,email=m_email,messege=m_message,subject=m_subject)
        m_Data.save()
    return redirect(Shop)    