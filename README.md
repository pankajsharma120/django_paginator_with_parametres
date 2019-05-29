# django_paginator_with_parametres
Django pagination  with proper url parameters.
Django simple pagination doesn't include extra url parameters in afterward pages ex - `?q=shirt&brand=Mangoon&category=men&page=1` pagination will remove brand and category for next page i.e - `?q=shirt&page=2`, to get rid out of this problem you can use this code.

# How to use -

1. Add `url_replace` in your custom tags file.

2. Use code of paginate.html for pagination.
