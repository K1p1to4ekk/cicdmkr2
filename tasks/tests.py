from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            is_completed=False
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), "Test Task")

    def test_task_fields(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "Test Description")
        self.assertEqual(self.task.is_completed, False)

class TaskViewTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            is_completed=False
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertTemplateUsed(response, 'tasks/task_list.html')

    def test_task_create(self):
        response = self.client.post(reverse('task_list'), {
            'title': 'New Task',
            'description': 'New Description',
            'is_completed': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.last().title, 'New Task')