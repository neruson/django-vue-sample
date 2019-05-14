from django.db import models


class RiskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomField(models.Model):
    FIELD_TYPE_CHOICES = [
        ("text", "Text"),
        ("number", "Number"),
        ("date", "Date"),
        ("enum", "Enum"),
    ]

    name = models.CharField(max_length=100)
    risk_type = models.ForeignKey(
        RiskType, on_delete=models.CASCADE, related_name="fields"
    )
    field_type = models.CharField(max_length=25, choices=FIELD_TYPE_CHOICES)

    def __str__(self):
        return self.name


class CustomFieldOption(models.Model):
    value = models.CharField(max_length=500)
    field = models.ForeignKey(
        CustomField, on_delete=models.CASCADE, related_name="options"
    )

    def __str__(self):
        return self.value
