from fastapi import APIRouter, BackgroundTasks

from auth.base_config import current_user

from .tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report(background_tasks: BackgroundTasks, user: str):
    # 1400 ms - Клиент ждет
    #send_email_report_dashboard(user)
    # 500 ms - Задача выполняется на фоне FastAPI в event loop'е или в другом треде
    #background_tasks.add_task(send_email_report_dashboard, user)
    # 600 ms - Задача выполняется воркером Celery в отдельном процессе
    send_email_report_dashboard.delay(user)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }