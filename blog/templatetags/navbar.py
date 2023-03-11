from django import template
from blog import models

register = template.Library()


@register.inclusion_tag('blog/include/navbar_tpl.html')
def show_navbar():
    contex = {
        'categories': models.Category.objects.all()
    }

    return contex


@register.inclusion_tag('blog/include/footer_tpl.html')
def show_footer():
    contex = {
        'categories': models.Category.objects.all(),
        'tags': models.Tag.objects.all(),
        'popular': models.Post.objects.filter(is_published=True).order_by('-views')[:6]
    }

    return contex