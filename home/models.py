# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Nationality(models.Model):

    #__Nationality_FIELDS__
    nationalityid = models.CharField(max_length=255, null=True, blank=True)
    nationalityname = models.CharField(max_length=255, null=True, blank=True)
    state = models.BooleanField()

    #__Nationality_FIELDS__END

    class Meta:
        verbose_name        = _("Nationality")
        verbose_name_plural = _("Nationality")


class Insured_Person(models.Model):

    #__Insured_Person_FIELDS__
    uid = models.IntegerField(null=True, blank=True)
    idnumber = models.IntegerField(null=True, blank=True)
    nationalityid = models.ForeignKey(nationality, on_delete=models.CASCADE)
    taxnumber = models.CharField(max_length=255, null=True, blank=True)
    passportnumber = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    genderid = models.CharField(max_length=255, null=True, blank=True)
    relationtypeid = models.CharField(max_length=255, null=True, blank=True)
    mothername = models.CharField(max_length=255, null=True, blank=True)
    fathername = models.CharField(max_length=255, null=True, blank=True)
    birthplace = models.CharField(max_length=255, null=True, blank=True)
    professionid = models.ForeignKey(Professions, on_delete=models.CASCADE)

    #__Insured_Person_FIELDS__END

    class Meta:
        verbose_name        = _("Insured_Person")
        verbose_name_plural = _("Insured_Person")


class Professions(models.Model):

    #__Professions_FIELDS__
    professioncode = models.IntegerField(null=True, blank=True)
    professionname = models.CharField(max_length=255, null=True, blank=True)

    #__Professions_FIELDS__END

    class Meta:
        verbose_name        = _("Professions")
        verbose_name_plural = _("Professions")



#__MODELS__END
