from django.test import TestCase

# Create your tests here.

class TaskListPageTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/heroes')
        response = self.client.get('/hero/cloud')
        response = self.client.get('/hero/sunflowey')
        response = self.client.get('/hero/jester')
        self.assertTemplateUsed(response, 'heroes.html')
        self.assertTemplateUsed(response, 'detail_cloud.html')
        self.assertTemplateUsed(response, 'detail_sunflowey.html')
        self.assertTemplateUsed(response, 'detail_jester.html')
