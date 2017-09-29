from django import template
register = template.Library()


@register.filter
def filter_model(queryset, model_id):
    return queryset.filter(model_id=model_id).all() if model_id else queryset.all()
