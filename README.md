# CIS4517 — Cloud Image Processing App (Django + S3)

A cloud-based image processing web app with online filters (Grayscale, Sepia, Posterize, Blur, Edge, Solarize). Users upload an image, choose filters, and download the processed result. Storage is on AWS S3. Hosted on AWS EC2 with Nginx + Gunicorn.

## Architecture
- **Web/App**: Django views + templates, Pillow for filters
- **Storage**: AWS S3 (private, presigned URLs)
- **Hosting**: EC2 (Ubuntu 22.04), Gunicorn, Nginx
- **Auth**: EC2 IAM Role (no access keys in code)

## Quick Start (local dev)
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env values (SECRET, BUCKET, REGION)
python manage.py migrate
python manage.py runserver 0.0.0.0:8000


## Start Up   load up EC2 and cd opt/imageapp/
Enter in Ubuntu
sudo systemctl start imageapp
sudo systemctl start nginx

Test system
systemctl status imageapp
systemctl status nginx

Test website
http://3.17.251.207


Encountered errors: EC2 public dns and ip address changed after stop and start.
- associated EC2 with Elastic IP

To demo:
Just start ec2
