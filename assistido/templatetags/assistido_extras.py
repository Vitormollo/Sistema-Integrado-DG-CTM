from django import template
import re
from datetime import date

register = template.Library()

# Filtro para calcular dias passados desde uma data
@register.filter
def dias_passados(value):
    if not value:
        return ''
    today = date.today()
    try:
        return (today - value).days
    except Exception:
        return ''

# Filtro para calcular idade
@register.filter
def age(value):
    if not value:
        return ''
    today = date.today()
    try:
        return today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    except Exception:
        return ''

@register.filter
def format_telefone(value):
    if not value:
        return ''
    num = re.sub(r'\D', '', value)
    # Remove o +55 se houver
    if num.startswith('55'):
        num = num[2:]
    # DDD + 9 dígitos (celular): 019999999999 ou 11999999999
    if len(num) == 11:
        return f'{num[0:2]} {num[2:7]}-{num[7:]}'
    # DDD + 8 dígitos (fixo): 01999999999 ou 1199999999
    elif len(num) == 10:
        return f'{num[0:2]} {num[2:6]}-{num[6:]}'
    # 9 dígitos sem DDD: 99999-9999
    elif len(num) == 9:
        return f'{num[0:5]}-{num[5:]}'
    # 8 dígitos sem DDD: 9999-9999
    elif len(num) == 8:
        return f'{num[0:4]}-{num[4:]}'
    return value
