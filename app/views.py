from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def login(request):
    return render(request,'app/login.html')

def karma_login(request):
    
    email = request.POST['em']
    password = request.POST['ps']

    user = profile.objects.get(Email = email)
    if user.Password == password:
        messages.info(request, "successfully register")
        request.session['user'] = user.id
        print(request.session['user'])
        
        return redirect('/userapp/')
    else:
        messages.info(request, "Your password is incorrect or user doesn't exist")
        return HttpResponseRedirect(reverse('login'))
   


def signup(request):
    return render(request,'app/signup.html')

def register(request):
    firstname = request.POST['fn']
    lastname = request.POST['ln']
    email = request.POST['em']
    password = request.POST['ps']
    confirm_password = request.POST['cps']
    mobile = request.POST['mb1']
    alternatemobile = request.POST['mb2']
    address1 = request.POST['ad1']
    address2 = request.POST['ad2']
    city = request.POST['ct']
    state = request.POST['st']
    zipcode = request.POST['zp']
    country = request.POST['ctry']

    old_user = profile.objects.filter(Email=email)

    if old_user:
        messages.info(request, 'Email is already registered.')
        return HttpResponseRedirect(reverse('login'))

    else:
        if  password != confirm_password:
            messages.warning(request, 'Password did not match')
            return HttpResponseRedirect(reverse('signup'))
    
    new_user = profile.objects.create(
        Firstname = firstname,
        Lastname=lastname,
        Email=email,
        Password=password,
        Mobile=mobile,
        AlternateMobileno=alternatemobile,
        Address1=address1,
        Address2=address2,
        City = city,
        State=state,
        Zipcode=zipcode,
        Country=country
    )
    new_user_shipping = shippingaddress.objects.create(
        UserId=new_user,
        Address1=address1,
        Address2=address2,
        City = city,
        State=state,
        Zipcode=zipcode,
        Country=country
    )
    new_user_id = user.objects.create(
        UserId = new_user,
        Email=email,
        Firstname = firstname,
    )
    messages.success(request, 'registration successfull.')
    return HttpResponseRedirect(reverse('login'))


def product_upload(request):
    return render(request,'app/product_upload_form.html')

def add_product(request):
    pname = request.POST.get('pn')
    pcategory = request.POST.get('cate')
    psize = request.POST.get('size')
    ptype = request.POST.get('type')
    pprize = request.POST.get('pp')
    pcolor = request.POST.get('pc')
    pimage = request.FILES.get('pimg')

    add_new_product = products.objects.create(
        Pname = pname,
        Pcategory = pcategory,
        Psize = psize,
        Ptype = ptype,
        Pprice = pprize,
        Pcolor = pcolor,
        Pimage = pimage
    )
    return render(request,'app/product_upload_form.html')
    # return HttpResponseRedirect(reverse('product_upload_form'))

# def show_product(request):
#     all_products = products.objects.all()
#     return render(request,'app/show_product.html',{"keys":all_products})


def contact(request):
    return render(request,'app/contact.html')

def blog(request):
    return render(request,'app/blog.html')

def cart(request):
    return render(request,'app/cart.html')

def category(request):
    return render(request,'app/category.html')

def checkout(request):
    return render(request,'app/checkout.html')

def confirmation(request):
    return render(request,'app/confirmation.html')

def elements(request):
    return render(request,'app/elements.html')

def single_blog(request):
    return render(request,'app/single_blog.html')

def single_product(request):
    return render(request,'app/single_product.html')

def tracking(request):
    return render(request,'app/pro.html')

# def pro(request):
#     all_products = products.objects.all()
#     return render(request,'app/pro.html',{"keys":all_products})
