from tests import *


class TestPages(TestCase):
    def test_home(self):
        """
            Tests to see if home page is rendered
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_blog(self):
        """
            Tests to see if blog page is rendered
        """
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        """
            Tests to see if about page is rendered and ensures that it
            is the about page based on the response.context
        """
        response = self.client.get("/about/")
        self.assertTrue('about' in response.context)
        self.assertTrue('page_content' in response.context)
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        """
            Tests to see if home registration is rendered
        """
        response = self.client.get("/registration/")
        self.assertEqual(response.status_code, 200)

    def test_resources(self):
        """
            Tests to see if resource page is rendered
        """
        response = self.client.get("/resources/")
        self.assertEqual(response.status_code, 200)

    def test_course(self):
        """
            Tests to see if course page is rendered
        """
        response = self.client.get("/course/")
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        """
            Tests to see if contact page is rendered
        """
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)


class TestPageContent(TestCase):
    def test_about_content(self):
        """
            Tests to see if the about page content is rendered correctly
            from the data base.
        """
        page = Page.objects.create(page="about",
                                   content="<h1>Umonya heading</h1>")

        response = self.client.get("/about/")
        content = response.context['page_content'][0]
        self.assertEqual([a.pk for a in response.context['page_content']], [1])
        self.assertEqual(content.page, "about")
        self.assertEqual(content.content, "<h1>Umonya heading</h1>")

    def test_about_bios(self):
        """
            Tests to see if the bios section of the about page is
            rendered correctly from the data base
        """
        about = About.objects.create(name="Umonya Name",
                                     role="Umonya Role",
                                     bios="Umonya Bios",
                                     bios_photo="path/2/Um/Photo.png",
                                     pub_date=datetime.datetime.utcnow().
                                     replace(tzinfo=utc))

        response = self.client.get("/about/")
        content = response.context['about'][0]
        self.assertEqual([a.pk for a in response.context['about']], [1])
        self.assertEqual(content.name, "Umonya Name")
        self.assertEqual(content.role, "Umonya Role")
        self.assertEqual(content.bios, "Umonya Bios")
        self.assertEqual(content.bios_photo, "path/2/Um/Photo.png")
