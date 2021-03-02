from django.forms import ModelForm
from .models import CreateNewPost,CreateNewPostPhotos

class CreateNewPostForm(ModelForm):
    class Meta:
        model=CreateNewPost
        fields=["post_id","carname","model","km","price","ownership","reg_number","color","tyre_condition","replacement","accident_history","car_condition","insurance","status"]

class CreateNewPostPhotosForm(ModelForm):
    class Meta:
        model=CreateNewPostPhotos
        fields=["postid","Front_Side_Image","Back_Side_Image","Left_Side_Image","Right_Side_Image","Car_Interior_Image","Car_Stereo_And_Camera","Car_Seat_Image","status"]
