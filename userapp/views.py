from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from app.models import *
from django.contrib import messages


# Create your views here.
def user_home(request):
    all_products = products.objects.all()
    # return render(request,'app/pro.html',{"keys":all_products})
    return render(request,'userapp/home.html',{"keys":all_products})

def profile_show(request):
    ids = request.session.get('user')
    # print(ids)
    Profile = profile.objects.filter(id = ids)
    # print(Profile)
    return render(request,'userapp/profile_show.html',{'user':Profile})

def single_product(request):
    # ids = request.session.get('user')
    # print(ids)
    product_image = products.objects.filter(id = ids)
    print(product_image)
    return render(request,'userapp/single_product.html',{"product":product_image})




def editdetails(request,pk):
    edituser = profile.objects.get(pk=pk)
    print("edituser is here",edituser)
    return render(request,"userapp/profile_edit.html",{"users":edituser})


def edituser(request,pk):
    existuser = profile.objects.get(id = pk)
    existuser.firstname = request.POST.get('fn')
    existuser.lastname = request.POST.get('ls')
    # existuser.email = request.POST.get('em')
    existuser.password = request.POST.get('ps')
    existuser.mobile = request.POST.get('mb1')
    existuser.alternatemobile = request.POST.get('mb2')
    existuser.address1 = request.POST.get('ad1')
    existuser.address2 = request.POST.get('ad2')
    existuser.city = request.POST.get('ct')
    existuser.state = request.POST.get('st')
    existuser.zipcode = request.POST.get('zp')
    existuser.country = request.POST.get('ctry')
   
    existuser.save()

    return HttpResponseRedirect(reverse('profile_show'))



def show_product(request):
    all_products = products.objects.all()
    return render(request,'app/show_product.html',{"keys":all_products})


def pro(request):
    all_products = products.objects.all()
    return render(request,'app/pro.html',{"keys":all_products})





# def userapp_logout(request):
#     del request.session['Email']
#     del request.session['Role']
#     del request.session['Firstname']
#     return HttpResponseRedirect(reverse('index'))

