from apscheduler.schedulers.background import BackgroundScheduler

from src import settings
from web.jobs import jobs


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(jobs.ppp, 'interval', seconds=settings.SCHEDULER_TIME_SEC, max_instances=1, misfire_grace_time=5)
    scheduler.start()
