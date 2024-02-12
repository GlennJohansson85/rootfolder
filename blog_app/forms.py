# ======================================
#                              FORMS.PY
# ======================================
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'categories']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['categories'].widget.attrs.update(
            {'class': 'form-control'}
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def save(self, user, post, commit=True):
        comment = super().save(commit=False)
        comment.user = user
        comment.post = post

        if commit:
            comment.save()
        return comment
