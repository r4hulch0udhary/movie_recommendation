from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommendation.settings')

app = Celery('movie_recommendation')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-recommendations-every-day': {
        'task': 'movies.tasks.update_recommendations',
        'schedule': 86400,
    },
}