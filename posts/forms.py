from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=128, label='Заголовок')
    text = forms.CharField(widget=forms.Textarea, max_length=512, label='Текст')