# from datetime import timedelta
from celery.schedules import crontab

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/5'
BROKER_URL = 'redis://127.0.0.1:6379/6'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'proj.tasks.add',
        # 'schedule': timedelta(seconds=30),
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16)
    }  # 这段代码表示每隔30秒执行 add 函数, 一旦使用了 scheduler, 启动 celery需要加上-B 参数  celery -A proj worker -B -l info
}
