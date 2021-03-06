from django import forms
from .models import Post, Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
        max_length=4000,
        help_text='The max length of the text is 4000.',
        #error_messages={'required': 'field is required.....'}
        #required=False
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class NewPostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
        max_length=4000,
        help_text='The max length of the text is 4000.',
        # error_messages={'required': 'field is required.....'}
        # required=False
    )

    class Meta:
        model = Post
        fields = ['message']
