from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from django.core.files.base import ContentFile
from .forms import UploadForm
from .models import ImageJob
from .utils import apply_filter
from PIL import Image
from io import BytesIO

def upload_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_file = form.cleaned_data["image"]
            filter_name = form.cleaned_data["filter_name"]
            job = ImageJob.objects.create(original=img_file, filter_name=filter_name)
            # Process
            original = Image.open(job.original).convert("RGB")
            processed = apply_filter(original, filter_name)
            buf = BytesIO()
            processed.save(buf, format="JPEG", quality=92)
            job.processed.save(f"{job.id}.jpg", ContentFile(buf.getvalue()), save=True)
            return redirect("result", job_id=job.id)
    else:
        form = UploadForm()
    return render(request, "images/upload.html", {"form": form})

def result_view(request, job_id):
    job = ImageJob.objects.filter(id=job_id).first()
    if not job or not job.processed:
        raise Http404("Not ready")
    return render(request, "images/result.html", {"job": job})

def download_view(request, job_id):
    job = ImageJob.objects.filter(id=job_id).first()
    if not job or not job.processed:
        raise Http404("Not found")
    return FileResponse(job.processed.open("rb"), as_attachment=True, filename=f"{job.id}.jpg")