from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from random import *


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

def forgot(request):
    return render(request,'app/forgot.html')

def get_email(request):
    email = request.POST['em']
    
    try:
        abc = profile.objects.get(Email=email)
        
        if abc.Email == email:
            otp = randint(100000, 9999999)
            new = check.objects.create(
            Otp = otp
        )
            send_mail('OTP FOR RESET PASSWORD :' + str(otp) ,
            "Kindly notedown your otp " + str(otp) + " ", 
            email,
            [email], 
            fail_silently=True)
            return HttpResponseRedirect(reverse('get_otp'))

        else:
            er_msg = "You have entered unregistered email." #here is an error programe cant go in else part
            # return render(request,'app/forgot.html',{'er_msg':er_msg})
            return HttpResponseRedirect(reverse('forgot'))
    except:
        pass

def get_otp(request):
    return render(request,'app/get_otp.html')

def verify_otp(request):
    print("here")
    otp1 = request.POST['otp']
    verify_otp = check.objects.get(Otp = otp1)
    print(otp1)
    if verify_otp.Otp:
        return HttpResponseRedirect(reverse('reset_password'))
    else:
        print("no")
        err_msg = "you have entered wrong otp"
        return render(request,'app/get_otp.html',{'err_msg':err_msg})



def reset_password(request):
    return render(request,'app/reset_password.html')

def get_newpassword(request):

    try:
        email = request.POST['em']
        new_password = request.POST['nps']
        new_password1 = request.POST['cps']

        if new_password == new_password1:
            availuser = profile.objects.get(Email = email)

            availuser.PassWord = new_password
            availuser.save()

        
            # messages.info(request,"Password has changed successfully.")
            return HttpResponseRedirect(reverse('login'))
       
        # else:
        #     messages.info(request,"Password does not match.")
        #     return render(request,'app/reset_password.html')

    except:
        pass




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

def pro(request):
    all_products = products.objects.all()
    return render(request,'app/pro.html',{"keys":all_products})
