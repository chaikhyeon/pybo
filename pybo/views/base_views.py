from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question, Answer

# Create your views here.
def index(request):
    """
        리스트
    """
    page = request.GET.get('page', '1') # page
    kw = request.GET.get('kw', '')      # search
    question_list = Question.objects.order_by('-create_date')
    # if kw:
    #     question_list = question_list.filter(
    #         Q(subject__icontains=kw) | # 제목 검색
    #         Q(content__icontains=kw) | # 내용 검색
    #         Q(answer__content__icontains=kw) | # 답변 내용 검색
    #         Q(author__username__icontains=kw) | # 질문 글쓴이 검색
    #         Q(answer__author__username__icontains=kw) # 답변 글쓴이 검색
    #         ).distinct()
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(author__username__icontains=kw) # 질문 글쓴이 검색
            ).distinct()
        
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    # print(page_obj.next_page_number())
    context = {'question_list':page_obj, 'page':page, 'kw':kw}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
        상세 내용
    """
    
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)