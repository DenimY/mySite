# from django.shortcuts import render

# Create your views here.
# 단축함수
from django.views.generic import ListView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, \
    TodayArchiveView, DetailView, TemplateView
from tagging.views import TaggedObjectList

from blog.models import Post

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render


# --- TemplateView
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


# --- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


# --- DetailView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


# --- FormView
# FormView 제네릭 부를 상속받아 SearchFormView 클래스형 뷰를 정의.
# 이는 GET 요청인 경우 폼을 화면에 보여주고 사용자의 입력을 기다린다.
# 사용자가 폼에 데이터를 입력한 후 제출하면 이는 POST 요청으로 접수되어, FormView 클래스는 데이터에 대한 유효성을 검사한다.
# 데티어가 유효화면 form_valid() 함수를 실행한 후에 적절한 URL로 리다이렉트 시키는 기능을 갖고 있따.
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)  # No Redirection
