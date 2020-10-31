import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x1080')


class TestUserInformationPageImage(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            options=chrome_options
        )
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def test_valide_update_profile_image(self):
        # Account creation
        self.driver.get(self.live_server_url + reverse("register"))
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys("jonyt")
        time.sleep(1)
        self.driver.find_element_by_name("email").send_keys(
            "jonyt@isnotdead.com"
        )
        time.sleep(1)
        self.driver.find_element_by_name("password1").send_keys("Dickrivers76")
        time.sleep(1)
        self.driver.find_element_by_name("password2").send_keys("Dickrivers76")
        time.sleep(1)
        self.driver.find_element_by_id("btn-register").click()
        time.sleep(5)
        # Login
        redirection_url = self.live_server_url + reverse("login")
        self.assertEqual(self.driver.current_url, redirection_url)
        self.driver.find_element_by_name("username").send_keys("jonyt")
        time.sleep(5)
        self.driver.find_element_by_name("password").send_keys("Dickrivers76")
        self.driver.find_element_by_id("btn-login").click()
        time.sleep(5)
        self.driver.find_element_by_id("profile-link").click()
        time.sleep(5)
        # Profile page
        redirection_url = self.live_server_url + reverse("profile")
        self.assertEqual(self.driver.current_url, redirection_url)
        background_picture = self.driver.find_element_by_id("div-default")
        source = background_picture.value_of_css_property("background-image")
        print(source)
        self.assertEqual(
            source,
            'url("{0}/static/dist/assets/img/bg-profile.jpg")'.format(
                self.live_server_url
            ),
        )
        # email = self.driver.find_element_by_id("p-email").text
        # self.assertEqual(email, "robert@isnotdead.com")
