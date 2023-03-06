from django.db import models


class ServicesData(models.Model):
    class Meta:
        verbose_name_plural = 'Services Data'

    service_type = models.CharField(max_length=30)

    short_text = models.CharField(max_length=300)

    long_text = models.TextField()

    contact_person = models.CharField(max_length=200)

    general_email = models.EmailField(verbose_name="Email")

    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.service_type}"


class NetworkData(models.Model):
    class Meta:
        verbose_name_plural = 'Network Data'

    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.country}: {self.city}'


class AboutData(models.Model):
    class Meta:
        verbose_name_plural = 'About Data'

    history = models.TextField()
    exchange_introduction = models.TextField()
