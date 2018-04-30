from django.forms import ModelForm, Textarea
from article.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': Textarea(attrs={'cols': 40, 'rows': 4}),
        }
    
