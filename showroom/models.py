from django.db import models

# Create your models here.


class CreateNewPost(models.Model):
    type=(
        ("First Owner","First Owner"),
        ("Second Owner","Second Owner"),
        ("Third Owner","Third Owner"),
    )
    car_condition = (
        ("Excellent Condition", "Excellent Condition"),
        ("Hale And Hearty", "Hale And Hearty"),
        ("ShowRoom Condition", "ShowRoom Condition"),
    )

    conditions=(
        ("Yes","Yes"),
        ("No","No"),
    )

    insurancetype=(
        ("New Insurance","New Insurance"),
        ("Valid Insurance","Valid Insurance"),
    )
    post_id=models.CharField(max_length=140,unique=True,null=False)
    carname=models.CharField(max_length=140,null=False)
    model=models.IntegerField(null=False)
    km=models.IntegerField(null=False)
    price=models.IntegerField(null=False)
    ownership=models.CharField(max_length=12,choices=type,default=1)
    reg_number=models.CharField(max_length=140,null=False)
    color=models.CharField(max_length=140,null=False)
    tyre_condition=models.CharField(max_length=140,null=False)
    replacement=models.CharField(max_length=20,choices=conditions,default=1)
    accident_history=models.CharField(max_length=20,choices=conditions,default=1)
    car_condition=models.CharField(max_length=120,choices=car_condition,default=1)
    insurance=models.CharField(max_length=20,choices=insurancetype,default=1)
    date=models.DateField(auto_now=True)
    status=models.CharField(max_length=10,null=False)

    def __str__(self):
        return self.post_id

class CreateNewPostPhotos(models.Model):
    postid=models.ForeignKey(CreateNewPost,on_delete=models.CASCADE)
    Front_Side_Image=models.ImageField(upload_to="Images",blank=False)
    Back_Side_Image=models.ImageField(upload_to="Images",blank=False)
    Left_Side_Image=models.ImageField(upload_to="Images",blank=False)
    Right_Side_Image=models.ImageField(upload_to="Images")
    Car_Interior_Image=models.ImageField(upload_to="Images")
    Car_Stereo_And_Camera=models.ImageField(upload_to="Images")
    Car_Seat_Image=models.ImageField(upload_to="Images")
    date=models.DateField(auto_now=True)
    status=models.CharField(max_length=10,null=False)

    def __str__(self):
        return str(self.postid)


