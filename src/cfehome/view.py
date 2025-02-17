from django.http import HttpResponse
from django.shortcuts import render
import pathlib

from visits.models import PageVisit
# access the path to the parent directory
this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "Home page"
    html_ = ""
    html_ = "home.html"
    my_context = {
        "title": my_title,
        "current_page_count": page_qs.count(),
        "total": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_, my_context)


def old_home_page_view(request, *args, **kwargs):
    my_title = "old Home page"
    my_context = {
        "title": my_title
    }
    html_ = """<!DOCTYPE html>
<html>
  <body>
    <h1>{title} is hi</h1>
  </body>
</html>
""".format(**my_context)
    # html_file_path = this_dir/"home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)
