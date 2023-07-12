from django.contrib import admin
from .models import Question, Answer
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['question_id']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
