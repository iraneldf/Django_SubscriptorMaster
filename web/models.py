from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Config(models.Model):

    business_name = models.CharField(_("business name"), max_length=50)
    logo = models.ImageField(_("logo"), upload_to='config/')
    facebook = models.URLField(_("facebook"), max_length=240)
    twitter = models.URLField(_("twitter"), max_length=240)
    telegram = models.URLField(_("telegram"), max_length=240)
    pinterest = models.URLField(_("pinterest"), max_length=240)
    flirk = models.URLField(_("flirk"), max_length=240)

    class Meta:
        verbose_name = _("configuration")

class Suscriptor(models.Model):

    email = models.EmailField(_("email"), max_length=254, unique=True)

    class Meta:
        verbose_name = _("Suscriptor")
        verbose_name_plural = _("Suscriptors")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("suscriptor_detail", kwargs={"pk": self.pk})

class New(models.Model):

    title = models.CharField(_("title"), max_length=100)
    news = models.TextField(_("news"))

    class Meta:
        verbose_name = _("new")
        verbose_name_plural = _("news")

    def __str__(self):
        return self.news

    def get_absolute_url(self):
        return reverse("new_detail", kwargs={"pk": self.pk})
