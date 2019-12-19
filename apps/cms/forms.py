from apps.forms import FormMixin
from django import forms
from apps.course.models import Course

from apps.news.models import News, Banner


# 编辑新闻分类表单
class EditNewsCategoryForm(forms.Form):
    pk = forms.IntegerField(error_messages={"required": "必须传入分类的id !!!"})
    name = forms.CharField(max_length=100)


# 发布新闻表单
class WriteNewsForm(forms.ModelForm, FormMixin):
    category = forms.IntegerField()

    class Meta:
        model = News
        exclude = ['category', 'author', 'pub_time']


# 添加轮播图表单
class AddBannerForm(forms.ModelForm, FormMixin):
    class Meta:
        model = Banner
        fields = ('priority', 'link_to', 'image_url')


# 修改轮播图表单
class EditBannerForm(forms.ModelForm, FormMixin):
    pk = forms.IntegerField()

    class Meta:
        model = Banner
        fields = ('priority', 'link_to', 'image_url')


# 新闻修改表单
class EditNewsForm(forms.ModelForm, FormMixin):
    category = forms.IntegerField()
    pk = forms.IntegerField()

    class Meta:
        model = News
        exclude = ['category', 'author', 'pub_time']


# 课程表单
class PubCourseForm(forms.ModelForm, FormMixin):
    category_id = forms.IntegerField()
    teacher_id = forms.IntegerField()

    class Meta:
        model = Course
        exclude = ("category", 'teacher')
