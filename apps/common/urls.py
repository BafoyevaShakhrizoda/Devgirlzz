from django.urls import path
from .views import (
    home_view,
    CategoryListView,
    CategoryDetailView,
    TestView,
    AssessmentResultView,
    VacancyListView,
    VacancyDetailView,
    generate_cv_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('tests/<int:pk>/', TestView.as_view(), name='test_detail'),
    path('results/<int:pk>/', AssessmentResultView.as_view(), name='assessment_result'),
    path('results/<int:result_id>/cv/', generate_cv_view, name='generate_cv'),
    path('vacancies/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
]