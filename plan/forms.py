from django import forms

from .models import Post, Participant

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text']

class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = '__all__'
    def process(self):
        cd=self.cleaned_data
