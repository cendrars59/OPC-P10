from django.test import TestCase

from users.forms import UserProfileUpdate, UserUpdateForm


class TestUserUpdateForm(TestCase):
    def test_user_form_is_valid(self):

        form = UserUpdateForm(
            data={'username': 'elvis', 'email': 'elvis@isnotdead.com'}
        )

        self.assertTrue(form.is_valid())

    def test_user_form_is_empty(self):

        form = UserUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    class TestProfileUpdateForm(TestCase):
        def test_profile_form_is_valid(self):

            form = UserProfileUpdate(
                data={
                    'image': 'profiles_pics/wallpapertip_wallpaper-hd-4k_30668_k6hOwni.jpg'
                }
            )

            self.assertTrue(form.is_valid())

        def test_profil_form_is_empty(self):

            form = UserProfileUpdate(data={})

            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 1)
