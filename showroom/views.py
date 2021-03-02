from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib import messages
from .models import CreateNewPost,CreateNewPostPhotos
from .forms import CreateNewPostForm,CreateNewPostPhotosForm
from django.core.paginator import Paginator
# Create your views here.

class CreateCarDetailsView(TemplateView):
    template_name = "showroom/index.html"

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        uname = "admin"
        pwd = "admin123"
        username = request.POST["Username"]
        password = request.POST["Password"]
        # print(username, password)
        if uname == username and pwd == password:
            # print("success")
            return redirect("homepage")
        else:
            messages.error(request, 'Invalid Username or Password.Please check your Username And Password.')
            return redirect('login')

class ShowRoomLogout(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")

class ShowRoomPosts(TemplateView):
    model=CreateNewPost
    template_name = "showroom/homepagedata.html"
    context={}

    def get_object(self):
        return self.model.objects.filter(status="active")
    def get(self, request, *args, **kwargs):
        purchases=self.get_object()
        paginator = Paginator(purchases,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})

class HomePageFinal(TemplateView):
    template_name = "showroom/homepage.html"
    context={}
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

class CreatePost(TemplateView):
    model=CreateNewPost
    template_name = "showroom/createpost.html"
    context={}

    def get(self, request, *args, **kwargs):
        postid = CreateNewPost.objects.all().last()
        if postid:
            getpostid = int(postid.post_id)
            getpostid += 1
            getpostid = str(getpostid)
        else:
            getpostid = "1000"
        # print(getpostid)
        form=CreateNewPostForm(initial={"post_id":getpostid})
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = CreateNewPostForm(request.POST)
        if form.is_valid():
            posti=form.cleaned_data.get("post_id")
            form.save()
            # print("save")
            return redirect("photos",pk=posti)
        else:
            # km = form.cleaned_data.get("km")
            # price = form.cleaned_data.get("price")
            # carname = form.cleaned_data.get("carname")
            # post_id = form.cleaned_data.get("post_id")
            # model = form.cleaned_data.get("model")
            # ownership = form.cleaned_data.get("ownership")
            # reg_number = form.cleaned_data.get("reg_number")
            # color = form.cleaned_data.get("color")
            # tyre_condition = form.cleaned_data.get("tyre_condition")
            # replacement = form.cleaned_data.get("replacement")
            # accident_history = form.cleaned_data.get("accident_history")
            # car_condition = form.cleaned_data.get("car_condition")
            # insurance = form.cleaned_data.get("insurance")
            # print(insurance,car_condition,accident_history,replacement,tyre_condition,color,reg_number,ownership,price,km,model,carname,post_id)
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class CreatePostPhotos(TemplateView):
    model=CreateNewPostPhotos
    template_name = "showroom/uploadphotos.html"
    context={}

    def get(self, request, *args, **kwargs):
        postid = kwargs.get("pk")
        self.context["postid"]=postid
        postidgetdetails=CreateNewPost.objects.get(post_id=postid)
        form = CreateNewPostPhotosForm(initial={"postid":postidgetdetails})
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        postid = kwargs.get("pk")
        self.context["postid"] = postid
        form=CreateNewPostPhotosForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # print(form)
            return redirect("homepage")
        else:
            print("bad")
            self.context["form"]=form
            return render(request, self.template_name, self.context)

class ViewPosts(TemplateView):
    model=CreateNewPost
    template_name = "showroom/viewpost.html"
    context={}

    def get_object(self,postid):
        return self.model.objects.get(post_id=postid)

    def get(self, request, *args, **kwargs):
        postid = self.get_object(kwargs.get("pk"))
        postidgetdetails=self.model.objects.filter(post_id=postid)
        self.context["postids"]=postidgetdetails
        form = CreateNewPostForm(instance=postid)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        postid=self.get_object(kwargs.get("pk"))
        form=CreateNewPostForm(instance=postid,data=request.POST)
        if form.is_valid():
            posti = form.cleaned_data.get("post_id")
            form.save()
            return redirect("editphoto",pk=posti)
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)

class Viewphotos(TemplateView):
    model = CreateNewPostPhotos
    template_name = "showroom/viewphotos.html"
    context = {}

    def get_object(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        purchases = self.get_object()
        paginator = Paginator(purchases, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})

class EditViewPhotos(TemplateView):
    model=CreateNewPost
    template_name = "showroom/editphotos.html"
    context={}

    def get_object(self,id):
        return self.model.objects.get(post_id=id)

    def get(self, request, *args, **kwargs):
        pstid=self.get_object(kwargs.get("pk"))
        print(pstid.id)
        obj=CreateNewPostPhotos.objects.get(id=pstid.id)
        self.context["postid"]=obj
        form=CreateNewPostPhotosForm(initial={"postid":obj.postid})
        self.context["form"]=form
        return render(request,self.template_name,self.context)

class HideCarDetails(TemplateView):
    model=CreateNewPost

    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        post=self.get_object(kwargs.get("pk"))
        postid=post.id
        # print(postid)
        obj=self.model.objects.get(post_id=post)
        obj.status="inactive"
        obj.save()
        print(obj)
        obj1=CreateNewPostPhotos.objects.get(id=postid)
        print(obj1)
        obj1.status="inactive"
        obj1.save()
        return redirect("homepage")

class InactivePost(TemplateView):
    model = CreateNewPost
    template_name = "showroom/hidepost.html"
    context = {}
    def get_objects(self):
        return self.model.objects.filter(status="inactive")

    def get(self, request, *args, **kwargs):
        hide = self.get_objects()
        paginator = Paginator(hide, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})

class ActivePost(TemplateView):
    model = CreateNewPost

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        post = self.get_object(kwargs.get("pk"))
        postid = post.id
        print(postid)
        obj = self.model.objects.get(post_id=post)
        obj.status = "active"
        obj.save()
        print(obj)
        obj1 = CreateNewPostPhotos.objects.get(id=postid)
        print(obj1)
        obj1.status = "active"
        obj1.save()
        return redirect("homepage")

class PhotoPageView(TemplateView):
    model = CreateNewPostPhotos
    template_name = "showroom/photopage.html"
    context={}

    def get_object(self,id):
        return self.model.objects.get(postid=id)

    def get(self, request, *args, **kwargs):
        postid=self.get_object(kwargs.get("pk"))
        ids=postid.id
        # print(ids)
        obj=self.model.objects.filter(postid=ids)
        paginator = Paginator(obj,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})



