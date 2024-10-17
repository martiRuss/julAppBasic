from django.shortcuts import render
from .models import Post
from .forms import DomCalculatorForm
import random

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


# def Post(request, pk):
#     posts = Post.objects.get(id=pk)
#     return render(request, 'posts.html', )


def calculate_dom(request):
    if request.method == "POST":
        form = DomCalculatorForm(request.POST)
        if form.is_valid():
            suburb = form.cleaned_data["suburb"]
            property_type = form.cleaned_data["property_type"]
            price = form.cleaned_data["price"]

            # Placeholder prediction logic (replace with actual model later)
            predicted_dom = random.randint(20, 90)

            return render(request, "result.html", {"predicted_dom": predicted_dom})

    else:
        form = DomCalculatorForm()

    return render(request, "form.html", {"form": form})
