from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if len(cleaned_data) < 3:
            raise forms.ValidationError('Название продукта должно быть больше 3 символов')
        elif cleaned_data in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            raise forms.ValidationError('Название продукта с таким названием недопустимо')

        return cleaned_data
