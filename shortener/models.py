import uuid
import base64

from django.db import models

HOST_NAME = 'http://127.0.0.1:8000/'


class Url(models.Model):
    url = models.URLField()
    url_hash = models.CharField(max_length=10, unique=True, db_index=True)
    short_url = models.URLField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.url_hash = self.generate_hash()
        self.short_url = self.create_short_url()
        super(Url, self).save(*args, **kwargs)

    def generate_hash(self):
        hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:6]
        hash_exist = Url.objects.filter(url_hash=hash)
        while hash_exist:
            hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:6]
            hash_exist = Url.objects.filter(url_hash=hash)
            continue

        hash = hash.decode('utf-8')

        return hash

    def create_short_url(self):
        return HOST_NAME + self.url_hash


