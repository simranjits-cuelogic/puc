from django import template

register = template.Library()
# load following line into template
# {% load tag_filter %}

@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})

# {{ form.subject|addcss:'MyClass' }}
@register.filter(name = 'addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})

# {{ form.field|with_value:'value' }}
@register.filter(name = 'with_value')
def with_value(value, arg):
    return value.as_widget(attrs={'value': arg})

# {{ object|published_articles_count:'value' }}
@register.filter(name = 'published_articles_count')
def published_articles_count(value):
    return value.published_articles().count()

# {{ object|total_articles_count:'value' }}
@register.filter(name = 'total_articles_count')
def total_articles_count(value):
    return value.total_articles().count()

# {{ object|draft_articles_count:'value' }}
@register.filter(name = 'draft_articles_count')
def draft_articles_count(value):
    return value.draft_articles().count()
