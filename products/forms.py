from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Brand, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_brand = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0 form-fields'

        self.fields['brand'].choices = friendly_names_brand
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0 form-fields'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        exclude = ('product', 'user', 'date_added')
