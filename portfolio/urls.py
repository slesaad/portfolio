from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import static

from django.views.generic import TemplateView

from resume.views import ResumeView
from projects.views import ProjectsView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('admin/', admin.site.urls),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
