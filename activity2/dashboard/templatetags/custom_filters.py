from django import template

register = template.Library()


@register.filter
def currency(value):
    """Formats a number as currency (e.g., $12,450.00)"""
    try:
        value = float(value)
        return "${:,.2f}".format(value)
    except (ValueError, TypeError):
        return value
