from django import template
from num2words import num2words
import re

register = template.Library()

@register.filter
def number_to_text(value):
    num = re.findall(r'\d+', value)
    for i in num:
        value = value.replace(i, num2words(int(i), lang='ru'))
    return value

@register.filter
def red2(value):
    cnt = 0
    while '<p>' in value:
        cnt += 1
        if cnt % 2 != 0:
            value = value.replace('<p>', '<p style="color:#000000">', 1)
        if cnt % 2 == 0:
            value = value.replace('<p>', '<p style="color:#FF0000">', 1)
    return value



