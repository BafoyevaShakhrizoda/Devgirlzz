from django.contrib import admin

from apps.common.models import Test, Question,Option,AssessmentResult,Vacancy,Company

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(AssessmentResult)
admin.site.register(Vacancy)
admin.site.register(Company)

