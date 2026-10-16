# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def health_check(request):
    return JsonResponse(
        {
            "status": "ok",
            "message": "Task Manager API is running",
        }
    )


@require_GET
def task_list(request):
    tasks = [
        {
            "id": 1,
            "title": "Complete Django setup",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Learn HTTP methods",
            "completed": True,
        },
    ]

    return JsonResponse({"tasks": tasks})
