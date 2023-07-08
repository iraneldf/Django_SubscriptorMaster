from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


# Create your models here.


class Config(SingletonModel):
    business_name = models.CharField(
        _("Nombre de negocio"), max_length=50, blank=True, null=True)
    business_name_active = models.BooleanField(
        _("Nombre de negocio activo"), default=False)
    logo = models.ImageField(
        _("Logo"), upload_to='config/', blank=True, null=True)
    facebook = models.URLField(
        _("facebook"), max_length=240, blank=True, null=True)
    twitter = models.URLField(
        _("twitter"), max_length=240, blank=True, null=True)
    telegram = models.URLField(
        _("telegram"), max_length=240, blank=True, null=True)
    pinterest = models.URLField(
        _("pinterest"), max_length=240, blank=True, null=True)
    flirk = models.URLField(_("flirk"), max_length=240, blank=True, null=True)
    suscribe_title = models.CharField(
        _("Titulo suscripción"), max_length=150, blank=True, null=True)
    suscribe_text = models.TextField(
        _("Texto suscripción"), blank=True, null=True)

    class Meta:
        verbose_name = _("Configuración")


class Suscriptor(models.Model):
    email = models.EmailField(
        _("Email"), max_length=254, unique=True, null=True, blank=True)
    phone = models.CharField(
        _("Telefono"), max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = _("Subscriptor")
        verbose_name_plural = _("Subscriptores")

    def __str__(self):
        return self.email or self.phone

    def get_absolute_url(self):
        return reverse("suscriptor_detail", kwargs={"pk": self.pk})


class New(models.Model):
    title = models.CharField(_("Titulo"), max_length=100)
    news = RichTextField('Noticias')

    class Meta:
        verbose_name = _("Noticia")
        verbose_name_plural = _("Noticias")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("new_detail", kwargs={"pk": self.pk})


class SMS(models.Model):
    sms = models.TextField(_("sms"), max_length=160)

    @property
    def longitud(self):
        return len(self.sms)

    class Meta:
        verbose_name = _("SMS")
        verbose_name_plural = _("SMSs")

    def __str__(self):
        return self.sms[:20]

    def get_absolute_url(self):
        return reverse("SMS_detail", kwargs={"pk": self.pk})


class EmailImg(models.Model):
    imagen = models.ImageField(
        _("imagen"), upload_to='noticias/imagenes', blank=True, null=True)
    noticia = models.ForeignKey(New, on_delete=models.CASCADE)
