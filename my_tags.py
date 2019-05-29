@register.simple_tag(name='url_replace')
def url_replace(request, field, value):
    d = request.GET.copy()
    d[field] = value
    return d.urlencode()
