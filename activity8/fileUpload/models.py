from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from PIL import Image
import os


def validate_file_size(value):
    filesize = value.size
    if filesize > 2 * 1024 * 1024:  # 2MB
        raise ValidationError("The maximum file size that can be uploaded is 2MB")


def validate_image_file(value):
    valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError("Only JPEG, PNG, and WebP files are allowed.")


class CustomUser(AbstractUser):
    photo = models.ImageField(
        upload_to="profile_photos/",
        validators=[validate_file_size, validate_image_file],
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            img = Image.open(self.photo.path)

            # Convert to square format (1:1 aspect ratio)
            if img.height != img.width:
                size = min(img.height, img.width)
                # Calculate coordinates for center crop
                left = (img.width - size) // 2
                top = (img.height - size) // 2
                right = left + size
                bottom = top + size

                # Crop and save
                img = img.crop((left, top, right, bottom))
                img.save(self.photo.path)
