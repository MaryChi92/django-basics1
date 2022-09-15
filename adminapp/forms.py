from django import forms

from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import Product, Category


class UserAdminEditForm(ShopUserEditForm):

    class Meta:
        model = ShopUser
        fields = '__all__'


# class CategoryEditForm(forms.ModelForm):
#
#     class Meta:
#         model = Category
#         exclude = ('is_active',)
#
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     for field_name, field in self.fields.items():
#     #         field.widget.attrs['class'] = 'form-control'
#     #         field.help_text = ''


class ProductEditForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('is_active',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
    #         field.help_text = ''
