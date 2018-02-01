from django.test import TestCase
from .models import DataList
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your tests here.

class ModelTestCase(TestCase):
    "" "Kelas ini mendefinisikan test suite untuk model DataList."""

    def setUp(self):
        """Definisi test client dan test variabel lain"""
        user = User.objects.create(username="putra")
        self.name = "Write world class code"
        # self.datalist = DataList(name=self.data_name)
        """pemilik spesifik dari datalist"""
        self.datalist = DataList(name=self.name, owner=user)

    def test_model_can_create_a_datalist(self):
        """Tes model datalist bisa membuat sebuah datalist"""
        old_count = DataList.objects.count()
        self.datalist.save()
        new_count = DataList.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(self.datalist), self.name)

"""
Create a bucketlist – Handle POST request
Read a bucketlist(s) – Handle GET request
Update a bucketlist – Handle PUT request
Delete a bucketlist – Handle DELETE request
"""

class ViewTestCase(TestCase):
    """Rangkaian test buat views api"""

    def setUp(self):
        """"Definisi test client dan test variabel lain"""
        user = User.objects.create(username="putra")

        #inisialisasi client dan paksa dia untuk menggunakan autentikasi
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        #sejak instan user model tidak serializable, gunakanlah Id/PK
        # self.datalist_data = {'name':'Go to Jogja'}
        self.datalist_data = {'name':'Go to Jogja', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.datalist_data,
            format="json"
        )

    def test_api_can_create_a_datalist(self):
        """Test api memiliki kemampuan pembuatan wadah(data)"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        # """Test api dengan autorisasi dari user"""
        new_client = APIClient()
        response = new_client.get('/datalists/',
                                  kwargs={'pk': 3},
                                  format="json"
                                  )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_datalist(self):
        # """Test api bisa mengambil data dari datalist"""
        datalist = DataList.objects.get(id=1)
        response = self.client.get(
                '/datalists/',
                kwargs={'pk': datalist.id},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, datalist)

    def test_api_can_update_datalist(self):
        """Test api bisa mengubah dari sebuah data pada datalist"""
        datalist = DataList.objects.get()
        change_datalist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details',
                    kwargs={'pk': datalist.id}),
            change_datalist, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_datalist(self):
        """Test api bisa menghapus sebuah data di datalist"""
        datalist = DataList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': datalist.id}),
            format="json",
            follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)