from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    # Заменяем нежелательные слова на '*'
    words_to_censor = ['нежелательное1', 'нежелательное2']  # Замените на реальные нежелательные слова
    for word in words_to_censor:
        value = value.replace(word, '*' * len(word))
    return value
