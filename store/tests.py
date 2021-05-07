from django.test import TestCase
from django.urls import reverse

from .models import Album, Artist, Booking, Contact


class HomePageTestCase(TestCase):

    # test that index page returns a status code 200
    def test_home_page_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class DetailPageTestCase(TestCase):

    # ran before each test.
    def setUp(self):
        Album.objects.create(title="Grateful")
        self.album = Album.objects.get(title="Grateful")

    # test that detail page returns a 200 if the item exists
    def test_detail_page_returns_200(self):
        album_id = self.album.id
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist
    def test_detail_page_returns_404(self):
        album_id = self.album.id + 1
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)


class BookingPageTestCase(TestCase):

    # ran before each test.
    def setUp(self):
        Contact.objects.create(name="Kezimana Aimé Angelo",
                               email="kezangelo@gmail.com")
        grateful = Album.objects.create(title="Grateful")
        dj_khaled = Artist.objects.create(name="Dj Khaled")
        dj_khaled.albums.add(grateful)
        self.album = Album.objects.get(title="Grateful")
        self.contact = Contact.objects.get(email="kezangelo@gmail.com")

    # test that a new booking is made
    def test_new_booking_is_made(self):
        old_bookings = Booking.objects.count()
        album_id = self.album.id
        contact_name = self.contact.name
        contact_email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': contact_name,
            'email': contact_email,
        })
        new_bookings = Booking.objects.count()
        self.assertEqual(old_bookings + 1, new_bookings)

    # test that a booking belongs to a contact
    def test_booking_belongs_to_a_contact(self):
        album_id = self.album.id
        contact_name = self.contact.name
        contact_email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': contact_name,
            'email': contact_email,
        })

        booking = Booking.objects.filter(contact=self.contact.id).first()
        self.assertEqual(self.contact, booking.contact)

    # test that a booking belongs to an album
    def test_booking_belongs_to_an_album(self):
        album_id = self.album.id
        contact_name = self.contact.name
        contact_email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': contact_name,
            'email': contact_email,
        })

        booking = Booking.objects.filter(album=album_id).first()
        self.assertEqual(self.album, booking.album)

    # test that an album is not available after a booking is made
    def test_album_is_unavailable_after_a_booking_is_made(self):
        album_id = self.album.id
        contact_name = self.contact.name
        contact_email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': contact_name,
            'email': contact_email,
        })
        # Make the query again, otherwise `available` will still be set at `True`
        self.album.refresh_from_db()
        self.assertFalse(self.album.available)
