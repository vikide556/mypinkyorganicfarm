from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .models import MyfarmProduct,ProductCategory
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Base pages
def base_view(request):
    return render(request, "myfarm/base.html")

def home_view(request):
    return render(request, "myfarm/home.html")

def about_view(request):
    return render(request, "myfarm/about.html")
    

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        messages.success(request, "✅ Your message has been sent successfully! We'll get back to you soon.")
        return redirect('contact')  # Redirect to avoid resubmission
    return render(request, 'myfarm/contact.html')

    clean_message = f'Name: {name}\nPhone : {phone}\nEmail : {email}\nMessage : {message}'
    print(clean_message)

    try:
            email_message = EmailMessage(
                subject=f"New Contact Form: {name}",
                body=clean_message,
                from_email="django@dtechnologys.com",  # must match your Gmail SMTP account
                to=["onyangoodiwuor@gmail.com", "danielnjama2015@gmail.com"],
                reply_to=[email],  # so you can hit "Reply" and email the visitor
            )
            email_message.send(fail_silently=False)

            messages.success(request, f"Thanks {name}, your message has been sent successfully!")
            print("OK")

    except Exception as e:
             print("AN ERROR OCCURRED:", e) 
        # Here you could save to DB or send email
        
    return redirect("contact")  # reload page with success message

    # default GET request
    return render(request, "myfarm/contact.html")


def blog_view(request):
    return render(request, "myfarm/blog.html")

def gallery_view(request):
    return render(request, "myfarm/gallery.html")

def faq_view(request): 
    return render(request, "myfarm/faq.html")

# Products
def product_view(request):
    products = ProductCategory.objects.all()
    return render(request, "myfarm/product_list.html", {"products": products})

# def product_detail(request, slug):
#     product = get_object_or_404(MyfarmProduct, slug=slug)
#     return render(request, "myfarm/product_detail.html", {"product": product})

# def product_list(request):
#     products = MyfarmProduct.objects.all()
#     return render(request, 'myfarm/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(ProductCategory, slug=slug)
    related_products = MyfarmProduct.objects.filter(category=product)
    return render(request, 'myfarm/product_detail.html', {
        'product': product,
        'related_products': related_products
    })

def single_product_detail(request, slug):
    product = get_object_or_404(MyfarmProduct, slug=slug)
    related_products = MyfarmProduct.objects.filter(category=product.category)
    return render(request, 'myfarm/product_detail.html', {
        'product': product,
        'related_products': related_products
    })