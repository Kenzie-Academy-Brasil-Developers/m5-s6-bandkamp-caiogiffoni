from albums.models import Album
from django.urls import reverse
from model_bakery import baker
from musicians.models import Musician
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from songs.models import Song


class ProductViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        # cls.musicician_1_data = {
        #     "first_name": "Jhon",
        #     "last_name": "Fruciant",
        #     "instrument": "Guitarrr",
        # }

        # cls.musician_2_data = {
        #     "first_name": "Sufjan",
        #     "last_name": "Stevens",
        #     "instrument": "Keyboard",
        # }

        # cls.album_1_data = {"name": "The Empyrean"}

        # cls.album_2_data = {"name": "Curtains"}

        # cls.musician_1 = Musician.objects.create(**cls.musicician_1_data)

        # cls.musician_2 = Musician.objects.create(**cls.musician_2_data)

        # cls.album_1 = Album.objects.create(
        #     **cls.album_1_data, musician=cls.musician_1
        # )

        # cls.album_2 = Album.objects.create(
        #     **cls.album_2_data, musician=cls.musician_2
        # )

        cls.song_1_data = {"name": "Before the Beginning", "duration": 548}

        # cls.song_2_data = {"name": "Before the Beginning", "duration": 548}

        # cls.song_1 = Song.objects.create(**cls.song_1_data, album=cls.album_1)
        cls.album = baker.make("Album")
        cls.song = baker.make("Song", album=cls.album)

        cls.base_url_create_song = reverse(
            "create_song",
            args=[
                cls.album.musician.id,
                cls.album.id,
            ],
        )

    def test_can_create_song(self):
        response = self.client.post(
            self.base_url_create_song, data=self.song_1_data
        )

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(len(response.data.keys()), 4)

        self.assertEqual(expected_status_code, result_status_code)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["name"], self.song_1_data["name"])
        self.assertEqual(
            response.data["duration"], self.song_1_data["duration"]
        )
        self.assertIn("album_id", response.data)

        expected_return_fields = (
            "id",
            "name",
            "duration",
            "album_id",
        )

        result_return_fields = tuple(response.data.keys())

        self.assertTupleEqual(expected_return_fields, result_return_fields)

    def test_can_list_songs(self):
        response = self.client.get(self.base_url_create_song)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

        self.assertEqual(len(response.data), 1)

        self.assertEqual(expected_status_code, result_status_code)
        expected_return_fields = (
            "id",
            "name",
            "duration",
            "album_id",
        )

        result_return_fields = tuple(response.data[0].keys())

        self.assertTupleEqual(expected_return_fields, result_return_fields)

    # def test_can_filter_products_with_no_token(self):
    #     response = self.client.get(self.base_url_filter_patch)

    #     expected_status_code = status.HTTP_200_OK
    #     result_status_code = response.status_code

    #     self.assertEqual(len(response.data.keys()), 5)

    #     self.assertEqual(expected_status_code, result_status_code)
    #     expected_return_fields = (
    #         "description",
    #         "price",
    #         "quantity",
    #         "is_active",
    #         "seller",
    #     )

    #     result_return_fields = tuple(response.data.keys())

    #     self.assertTupleEqual(expected_return_fields, result_return_fields)

    #     self.assertEqual(len(response.data["seller"].keys()), 8)

    # def test_ca_not_create_product_with_no_body(self):
    #     self.client.credentials(
    #         HTTP_AUTHORIZATION="Token " + self.token_user_1_seller.key
    #     )
    #     response = self.client.post(self.list_create_product, data={})

    #     expected_status_code = status.HTTP_400_BAD_REQUEST
    #     result_status_code = response.status_code

    #     self.assertEqual(len(response.data.keys()), 3)

    #     self.assertEqual(expected_status_code, result_status_code)
    #     expected_return_fields = (
    #         "price",
    #         "quantity",
    #         "description",
    #     )

    #     for field in expected_return_fields:
    #         self.assertEqual(response.data[field], ["This field is required."])

    #     result_return_fields = tuple(response.data.keys())

    #     self.assertTupleEqual(expected_return_fields, result_return_fields)

    # def test_can_not_create_product_with_negative_quantity(self):
    #     self.client.credentials(
    #         HTTP_AUTHORIZATION="Token " + self.token_user_1_seller.key
    #     )
    #     response = self.client.post(
    #         self.list_create_product, data=self.product_2_data
    #     )

    #     expected_status_code = status.HTTP_400_BAD_REQUEST
    #     result_status_code = response.status_code

    #     self.assertEqual(len(response.data.keys()), 1)

    #     self.assertEqual(expected_status_code, result_status_code)
    #     self.assertEqual(
    #         response.data["quantity"],
    #         ["Ensure this value is greater than or equal to 0."],
    #     )
