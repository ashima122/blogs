from django import forms
 
# creating a form
class BlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)