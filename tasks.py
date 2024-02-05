from celery import Celery

celery = Celery(__name__)

@celery.task
def create_histogram():
    return result