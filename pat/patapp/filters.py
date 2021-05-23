import django_filters

from django import forms
from .models import *
from django_filters import CharFilter,ModelChoiceFilter

class CatFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='宠物名称')
    SELVALUE = (
        ('','任意'),
        ('大型', '大型猫'),
        ('中型', '中型猫'),
        ('小型', '小型猫')
    )
    mc = (
        ('', '任意'),
        ('无毛', '无毛猫'),
        ('短毛', '短毛猫'),
        ('长毛', '长毛猫')
    )
    class Meta:
        model=Cat
        fields=['shape','hair']

    shape=CharFilter(field_name='shape',widget=forms.widgets.Select(choices=SELVALUE),label='宠物大小')
    hair=CharFilter(field_name='hair',widget=forms.widgets.Select(choices=mc),label='宠物毛长')


class DogFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='宠物名称')
    SELVALUE = (
        ('','任意'),
        ('大型犬', '大型犬'),
        ('中型犬', '中型犬'),
        ('小型犬', '小型犬')
    )
    mc = (
        ('', '任意'),
        ('中长毛', '中长毛'),
        ('短毛', '短毛'),
        ('长毛', '长毛'),
        ('无毛', '无毛'),
        ('无毛', '中短毛'),

    )
    class Meta:
        model=Dog
        fields=['shape','hair']

    shape=CharFilter(field_name='shape',widget=forms.widgets.Select(choices=SELVALUE),label='宠物大小')
    hair=CharFilter(field_name='hair',widget=forms.widgets.Select(choices=mc),label='宠物毛长')

