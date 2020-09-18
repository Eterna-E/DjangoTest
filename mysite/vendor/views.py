from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm,RawVendorForm,VendorModelForm # 要記得 import 相對應的 Model Form 唷!
# 額外 import Http404
# from django.http import Http404
from django.shortcuts import get_object_or_404 # 新增
from django.views.generic import ListView, DetailView, CreateView, UpdateView # 新增

# Create your views here.
def vendor_index(request):
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendors/vendor_detail.html', context)

# 針對 vendor_create.html
def vendor_create_view(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        # Vendor.objects.create(**form.cleaned_data) # 新增
        form.save()
        print(form.cleaned_data)
        form = VendorForm() # 清空 form
        # form = RawVendorForm()

    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)

def singleVendor(request, id):
    vendor_list = get_object_or_404(Vendor, id=id)
    # try:
    #     vendor_list = Vendor.objects.get(id=id)
    # except Vendor.DoesNotExist:
    #     raise Http404
    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendors/vendor_detail_single.html', context)

# 繼承 ListView
class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_list.html'

# 繼承 DetailView
class VendorDetailView(DetailView):
    model = Vendor
    # queryset = Vendor.objects.all()
    template_name = 'vendors/vendor_detail_new.html'

class VendorCreateView(CreateView):
    form_class = VendorModelForm
    # model = Vendor
    # fields='__all__'
    template_name = 'vendors/vendor_create.html'

class VendorUpdateView(UpdateView):
    form_class = VendorModelForm
    template_name = 'vendors/vendor_create.html'
    queryset = Vendor.objects.all() # 這很重要