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




def editdetails(request,pk):
    edituser = profile.objects.get(pk=pk)
    print("edituser is here",edituser)
    return render(request,"userapp/profile_edit.html",{"keys":edituser})


def edituser(request,pk):
    existuser = profile.objects.get(id = pk)
    existuser.Firstname = request.POST.get('fn')
    existuser.Lastname = request.POST.get('ls')
    # existuser.email = request.POST.get('em')
    existuser.Password = request.POST.get('ps')
    existuser.Mobile = request.POST.get('mb1')
    existuser.Alternatemobile = request.POST.get('mb2')
    existuser.Address1 = request.POST.get('ad1')
    existuser.Address2 = request.POST.get('ad2')
    existuser.City = request.POST.get('ct')
    existuser.State = request.POST.get('st')
    existuser.Zipcode = request.POST.get('zp')
    existuser.Country = request.POST.get('ctry')
   
    existuser.save()

    return HttpResponseRedirect(reverse('profile_show'))



def show_product(request):
    all_products = products.objects.all()
    return render(request,'app/show_product.html',{"keys":all_products})


def single_product(request):
    ids = request.session.get('user')
    print(ids)
    product_image = products.objects.filter(id = ids)
    print(product_image)
    return render(request,'userapp/single_product.html',{"user":product_image})




def pro(request):
    all_products = products.objects.all()
    return render(request,'app/pro.html',{"keys":all_products})





# def userapp_logout(request):
#     del request.session['Email']
#     del request.session['Role']
#     del request.session['Firstname']
#     return HttpResponseRedirect(reverse('index'))

