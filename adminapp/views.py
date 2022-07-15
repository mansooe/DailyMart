

from unicodedata import category
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from adminapp.models import CategoryDb, ProductDb

# Create your views here.
def adminpage(request):
   
    return render(request,'index.html')

def CategoryTable(request):
    obj=CategoryDb.objects.all()
    return render(request,'CategoryTable.html',{'obj':obj})
def Addcategory(request):
    return render(request,'AddCategory.html')
def Addcategorydata(request):
    if request.method=='POST':
        m_CategorytyName=request.POST.get('CategoryName')
        m_CategoryImg=request.FILES['CategoryImg']

        m_data=CategoryDb(CategoryName=m_CategorytyName,CategoryImg=m_CategoryImg)
        m_data.save()
    return redirect(CategoryTable)      
            
def Tableslist(request):
   
    return render(request,'Tables.html')
def Deletecategory(request,id):
    CategoryDb.objects.get(id=id).delete()
    return redirect(CategoryTable)

def Addproduct(request):
    obj=CategoryDb.objects.all()
    return render(request,'AddProduct.html',{'obj':obj})    
def AddnewProduct(request):
    if request.method=='POST':
        m_productname=request.POST.get('productname')
        m_productprice=request.POST.get('productprice')
        m_productcategory=request.POST.get('productcategory')
        m_Productimg=request.FILES['productimg']

        m_data=ProductDb(productname=m_productname,productcategory=m_productcategory,productprice=m_productprice,productimg=m_Productimg)
        m_data.save()
    return redirect(ProductTable)          

def ProductTable(request):
   
    obj=ProductDb.objects.all()

    VegitableCount=obj.filter(productcategory='Vegitables').count()
    fruitCount=obj.filter(productcategory='Fruits').count()
    DryFruitsCount=obj.filter(productcategory='DryFruits').count()
    JuicesCount=obj.filter(productcategory='Juices').count()

    category=CategoryDb.objects.all()

    contex={
        'obj':obj,
        'vegitableCount':VegitableCount,
        'FruitCount':fruitCount,
        'DryFruitCount':DryFruitsCount,
        'JuicesCount':JuicesCount,
        'Categorys':category
    }
    return render(request,'ProductTable.html',contex)            

    
def UpdateProductDetail(request,id):
    
    if 'Delete' in request.POST:
        ProductDb.objects.get(id=id).delete()
        return redirect(ProductTable)
    if 'Update' in request.POST:

        if request.method=='POST':
       
            c_productname=request.POST.get('productname')
            c_productprice=request.POST.get('productprice')
            c_productcategory=request.POST.get('productcategory')
            
            try:
                c_img=request.FILES['productimg']
                fs=FileSystemStorage()
                file=fs.save(c_img.name,c_img)
            except:
                file=ProductDb.objects.get(id=id).productimg


    ProductDb.objects.filter(id=id).update(productname=c_productname,productcategory=c_productcategory,productprice=c_productprice,productimg=file)  
    return redirect(ProductTable)       

