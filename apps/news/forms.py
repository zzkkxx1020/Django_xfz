# encoding: utf-8

from django import forms
from apps.forms import FormMixin


# 新闻详情评论表单
class PublicCommentForm(forms.Form, FormMixin):
    content = forms.CharField()
    news_id = forms.IntegerField()
