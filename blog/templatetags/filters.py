from django import template
from num2words import num2words
from django.utils.safestring import SafeString

register = template.Library()

# после цифры обязательно должен идти пробел, иначе не сконвертирует
@register.filter
def number_to_text(value):
    words = value.split()
    for i in range(len(words)):
        if words[i].isdigit():
            words[i] = num2words(int(words[i]), lang='ru')
    return SafeString(' '.join(words))


