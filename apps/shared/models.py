from pathlib import Path
from uuid import uuid4

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as lazy
from rest_framework.exceptions import ValidationError


class CustomFileExtensionValidator(FileExtensionValidator):
    message = lazy(
        "File extension “{extension}(s)” is not allowed. "
        "Allowed extensions are: {allowed_extensions}s."
    )

    def __call__(self, values):
        for value in values:
            extension = Path(value.name).suffix[1:].lower()
            if (
                self.allowed_extensions is not None
                and extension not in self.allowed_extensions
            ):
                raise ValidationError(
                    self.message.format(**{
                        "extension": extension,
                        "allowed_extensions": ", ".join(self.allowed_extensions),
                        "value": value,
                    }),
                    code=self.code
                )


def unique_id():
    return str(uuid4()).split('-')[-1]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True