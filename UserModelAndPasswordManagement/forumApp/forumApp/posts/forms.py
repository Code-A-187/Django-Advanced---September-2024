from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        error_messages = {
            'title': {
                'required': 'Please enter the title of your post',
                'max_length': f'The title is too long. Please keep it under {Post.TITLE_MAX_LENGTH} characters'
            },
            'author': {
                'required': 'Please enter an author'
            }
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author[0].isupper():
            raise ValidationError('Author name should start with capital letter!')

        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title in content:
            raise ValidationError('The post title name could not be included in the post content')

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)
        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


class PostCreateForm(PostBaseForm):
        pass


class PostEditForm(PostBaseForm):
        pass


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...'
            }
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required. Write it!'
            },
            'content': {
                'required': 'Content is required. Write it!'
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add message...',
        })


CommentFormSet = formset_factory(CommentForm, extra=1)





        # widgets = {
        #     "title": forms.NumberInput,
        # }
        #
        # labels = {
        #     "title": "That's a title label"
        # }
        #
        # help_texts = {
        #     'title': 'This is the title'
        # }


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#
#     content = forms .CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=30,
#     )
#
#     created_at = forms.DateTimeField(
#         auto_now_add=True
#     )
#
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices
#
#     )