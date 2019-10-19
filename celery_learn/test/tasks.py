from celery import Celery

broker = "redis://127.0.0.1:6379/5"
backend = "redis://127.0.0.1:6379/6"

app = Celery("tasks", broker=broker, backend=backend)


@app.task
def add(x, y):
    return x + y

# 上述代码导入了celery，然后创建了celery 实例 app，实例化的过程中指定了任务名tasks（和文件名一致），传入了broker和backend。然后创建了一个任务函数add
