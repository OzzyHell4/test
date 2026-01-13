from django.shortcuts import render, get_object_or_404
from .models import Course, ProgLang


def product_list(request, progLang_slug=None):
    progLangs = ProgLang.objects.all()
    courses = Course.objects.all()

    progLang = None
    if progLang_slug:
        progLang = get_object_or_404(ProgLang, progLang_slug=progLang_slug)
        courses = courses.filter(progLang=progLang)

    return render(request, 'main/course/list.html', {'progLang':progLang, 
                                                     'progLangs':progLangs, 
                                                     'courses':courses})

def product_detail(request, id, slug):
    product = get_object_or_404(Course, id=id, slug=slug)
    related_products = Course.objects.filter(progLang=product.progLang).exclude(id=product.id)[:4]

    return render(request, 'main/course/detail.html', {'product': product,
                                                       'related_products':related_products})