from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    def clean_description(self):
        for i in [self.cleaned_data['name'], self.cleaned_data['description']]:
            cleaned_data = i
            print(self.cleaned_data)
            if len(cleaned_data) < 3:
                raise forms.ValidationError('Название и описание продукта должно быть больше 3 символов')
            elif cleaned_data in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
                raise forms.ValidationError('Название или описание продукта имеет недопустимые слова')
        return cleaned_data

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')


class ProductFormForModerator(ProductForm):
    class Meta:
        model = Product
        fields = ('is_published', 'description', 'category')


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

