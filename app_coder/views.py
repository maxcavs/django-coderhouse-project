from django.shortcuts import render
from django.db.models import Q

from app_coder.models import *
from app_coder.forms import CategoryForm, ProfesorForm, HomeworkForm


def index(request):
    return render(request, "app_coder/home.html")


def profesors(request):
    profesors = Profesor.objects.all()

    context_dict = {
        'profesors': profesors
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/profesors.html"
    )


def categories(request):
    categories = Categoria.objects.all()

    context_dict = {
        'categories': categories
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/categories.html"
    )


def students(request):
    students = Student.objects.all()

    context_dict = {
        'students': students
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/students.html"
    )


def homeworks(request):
    homeworks = Homework.objects.all()

    context_dict = {
        'homeworks': homeworks
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/homeworks.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        category = Categoria(name=request.POST['name'], code=request.POST['code'])
        category.save()

        categories = Categoria.objects.all()
        context_dict = {
            'categories': categories
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/categories.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def category_forms_django(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            data = category_form.cleaned_data
            category = Categoria(name=data['name'], code=data['code'])
            category.save()

            categories = Categoria.objects.all()
            context_dict = {
                'categories': categories
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/categories.html"
            )

    category_form = CategoryForm(request.POST)
    context_dict = {
        'category_form': category_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/category_django_forms.html'
    )


def profesor_forms_django(request):
    if request.method == 'POST':
        profesor_form = ProfesorForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data
            profesor = Profesor(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                profession=data['profession'],
            )
            profesor.save()

            profesors = Profesor.objects.all()
            context_dict = {
                'profesors': profesors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/profesors.html"
            )

    profesor_form = ProfesorForm(request.POST)
    context_dict = {
        'profesor_form': profesor_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/profesor_django_forms.html'
    )


def homework_forms_django(request):
    if request.method == 'POST':
        homework_form = HomeworkForm(request.POST)
        if homework_form.is_valid():
            data = homework_form.cleaned_data
            homework = Homework(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            homework.save()

            homeworks = Homework.objects.all()
            context_dict = {
                'homeworks': homeworks
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/homeworks.html"
            )

    homework_form = HomeworkForm(request.POST)
    context_dict = {
        'homework_form': homework_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/homework_django_forms.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        categories = Categoria.objects.filter(name__contains=search_param)
        context_dict = {
            'categories': categories
        }
    elif request.GET['code_search']:
        search_param = request.GET['code_search']
        categories = Categoria.objects.filter(code__contains=search_param)
        context_dict = {
            'categories': categories
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        categories = Category.objects.filter(query)
        context_dict = {
            'categories': categories
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )
