from .models import Purchase, Product, Category
from django import forms


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = ["products", "status", "quantity", "scale", "comment", "categories"]
        labels = {
            "products": "Назва",
            "status": "Статус",
            "quantity": "Кількість",
            "scale": "Шкала",
            "comment": "Коментар",
            "categories": "Категорії",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["products"].widget.attrs.update({"class": "form-control", "style": "width:200px"})
        self.fields["quantity"].widget.attrs.update({"class": "form-control", "style": "width:100px"})
        self.fields["scale"].widget.attrs.update({"class": "form-control", "style": "width:100px"})
        self.fields["comment"].widget.attrs.update({"class": "form-control", "style": "width:200px"})
        self.fields["categories"].widget.attrs.update({"class": "form-control", "style": "width:200px"})


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name"]
        labels = {
            "name": "Назва"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "style": "width:200px"})


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["title"]
        labels = {
            "title": "Назва"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control", "style": "width:200px"})


class PurchaseSearchForm(forms.Form):
    title = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.RadioSelect(), initial=1,
                                   label="Категорії")
