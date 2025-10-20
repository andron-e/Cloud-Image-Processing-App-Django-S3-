from django.contrib import admin
from django.urls import path
from images.views import upload_view, result_view, download_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", upload_view, name="upload"),
    path("result/<uuid:job_id>/", result_view, name="result"),
    path("download/<uuid:job_id>/", download_view, name="download"),
]