# django_paginator_with_parametres
Django pagination  with proper url parameters.
#How to use -

{% if is_paginated %}
      <br>
      <div class="row">
        <div class="col-12">
        <ul class="pagination float-right">
          {% if page_obj.has_previous %}
            <li class="page-item"><a class="page-link" href="?{% url_replace request 'page' page_obj.previous_page_number %}">&laquo;</a></li>
          {% else %}
            <li class="page-item disabled"><span class="page-link">&laquo;</span></li>
          {% endif %}
          {% for i in paginator.page_range %}
            {% if page_obj.number == i %}
              <li class="active page-item"><span class="page-link">{{ i }} <span class="sr-only">(current)</span></span></li>
            {% else %}
              <li class="page-item"><a class="page-link" href="?{% url_replace request 'page' i %}">{{ i }}</a></li>
            {% endif %}
          {% endfor %}
          {% if page_obj.has_next %}
            <li class="page-item"><a class="page-link" href="?{% url_replace request 'page' page_obj.next_page_number %}">&raquo;</a></li>
          {% else %}
            <li class="page-item disabled"><span class="page-link">&raquo;</span></li>
          {% endif %}
        </ul>
      </div>
    </div>
 {% endif %}
