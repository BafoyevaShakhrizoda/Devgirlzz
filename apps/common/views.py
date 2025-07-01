from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Test, Vacancy, AssessmentResult
from django.contrib.auth.mixins import LoginRequiredMixin

def home_view(request):
    categories = Category.objects.all()[:6]
    featured_vacancies = Vacancy.objects.filter(is_featured=True)[:3]
    
    context = {
        'categories': categories,
        'featured_vacancies': featured_vacancies
    }
    return render(request, 'home.html', context)

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'categories/category_tests.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = self.object.tests.all()
        return context

class TestView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = 'categories/test_detail.html'

class AssessmentResultView(LoginRequiredMixin, DetailView):
    model = AssessmentResult
    template_name = 'results/assessment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VacancyListView(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies_list.html'
    context_object_name = 'vacancies'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class VacancyDetailView(LoginRequiredMixin, DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['similar_vacancies'] = Vacancy.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:3]
        return context

def generate_cv_view(request, result_id):
    return render(request, 'results/cv.html')
