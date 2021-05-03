from django.db import models


class Artist(models.Model):
    name = models.CharField('Nom', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "artiste"


class Contact(models.Model):
    email = models.EmailField('E-mail', max_length=100)
    name = models.CharField('Nom', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "prospect"


class Album(models.Model):
    reference = models.IntegerField('Référence', null=True)
    created_at = models.DateTimeField('Date de création', auto_now_add=True)
    available = models.BooleanField('Disponible', default=True)
    title = models.CharField('Titre', max_length=200)
    picture = models.URLField('Photo',)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "disque"


class Booking(models.Model):
    created_at = models.DateTimeField('Date d\'envoi', auto_now_add=True)
    contacted = models.BooleanField('Demande traitée', default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name

    class Meta:
        verbose_name = "réservation"
