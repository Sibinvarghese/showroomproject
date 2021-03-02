from django.shortcuts import render
from django.views.generic import TemplateView
from showroom.models import CreateNewPostPhotos,CreateNewPost


# Create your views here.
class UserHomePage(TemplateView):
    model=CreateNewPostPhotos
    template_name = "user/photopage.html"
    context={}

    def get(self, request, *args, **kwargs):
        # print("helloooo")
        self.context={
            "getphoto":CreateNewPostPhotos.objects.filter(status="active"),
            "getpost":CreateNewPost.objects.filter(status="active")
        }
        print(self.context["getphoto"])
        print(self.context["getpost"])
        # obj1=self.model.objects.filter(status="active")
        # self.context["obj1"]=obj1
        # obj=CreateNewPost.objects.filter(status="active")
        # self.context["obj"] = obj
        return render(request,self.template_name,self.context)
