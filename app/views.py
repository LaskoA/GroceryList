from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from app.models import Purchase, Product, Category
from app.forms import PurchaseForm, ProductForm, CategoryForm, PurchaseSearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, template_name="app/index.html")


class PurchaseListView(LoginRequiredMixin, generic.ListView):
    model = Purchase
    queryset = Purchase.objects.all()
    template_name = "app/purchase_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PurchaseListView, self).get_context_data(**kwargs)
        context["search_form"] = PurchaseSearchForm()

        return context

    def get_queryset(self):
        title = self.request.GET.get("title")

        if title:
            return self.queryset.filter(products__purchase__categories_id=title)
        return self.queryset


class PurchaseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Purchase


class PurchaseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = "http://127.0.0.1:8000/purchases/?title=1"
    template_name = "app/purchase_form.html"


class PurchaseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = "http://127.0.0.1:8000/purchases/?title=1"
    template_name = "app/purchase_form.html"


class PurchaseDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Purchase
    success_url = reverse_lazy("app:purchase-list")
    template_name = "app/purchase_delete.html"


@login_required
def purchase_status_change(request, pk):
    purchase = Purchase.objects.get(id=pk)
    if purchase.status:
        purchase.status = False
    else:
        purchase.status = True
    purchase.save()

    redirect_to = request.META.get('HTTP_REFERER', reverse_lazy('default-redirect-page'))
    return HttpResponseRedirect(redirect_to)


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("app:product-list")
    template_name = "app/product_form.html"


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "app/product_list.html"


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("app:product-list")
    template_name = "app/product_form.html"


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy("app:product-list")
    template_name = "app/product_delete.html"


class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "app/category_list.html"


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("app:category-list")
    template_name = "app/category_form.html"


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy("app:category-list")
    template_name = "app/category_delete.html"
