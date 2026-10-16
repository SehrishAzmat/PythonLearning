from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class HealthCheckTests(TestCase):
    def test_health_check_returns_success(self):
        response = self.client.get(reverse("health-check"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")


class TaskListTests(TestCase):
    def test_task_list_returns_success(self):
        response = self.client.get(reverse("task-list"))

        self.assertEqual(response.status_code, 200)

    def test_task_list_returns_two_tasks(self):
        response = self.client.get(reverse("task-list"))

        self.assertEqual(len(response.json()["tasks"]), 2)

    def test_task_list_returns_expected_fields(self):
        response = self.client.get(reverse("task-list"))
        first_task = response.json()["tasks"][0]

        self.assertEqual(
            set(first_task.keys()),
            {"id", "title", "completed"},
        )

    def test_task_list_rejects_post(self):
        response = self.client.post(
            reverse("task-list"),
            data={"title": "New task"},
        )

        self.assertEqual(response.status_code, 405)
