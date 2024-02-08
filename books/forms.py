from django.forms import ModelForm
from books.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'recommend']
