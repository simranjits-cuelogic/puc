from django import template

register = template.Library()

@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})

# {{ form.subject|addcss:'MyClass' }}
@register.filter(name = 'addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})
