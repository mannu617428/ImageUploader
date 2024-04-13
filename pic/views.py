# from django.shortcuts import render
# from .forms import Imageform
# from .models import Image

# # Create your views here.
# def home(request):
#     form = Imageform()
#     return render(request, 'pic/home.html', {form:'form'})


from django.shortcuts import render
from .forms import Imageform
from .models import Image

def home(request):
    img = Image.objects.all()  # Move this line outside of the if-else block
    if request.method == 'POST':
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or render success page
    else:
        form = Imageform()
    return render(request, 'pic/home.html', {'img': img, 'form': form})
