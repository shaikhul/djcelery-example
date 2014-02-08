import datetime
from django.utils import timezone
from celery import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from cleanup_manager.models import Poll

@task
def do_a_manual_task(poll_id):
	"""
	this is an example task that can be used manually from application
	ex.
	>>> from cleanup_manager.models import Poll
	>>> from cleanup_manager.tasks import do_a_manual_task
	>>> poll = Poll.objects.get(pk=1)
	>>> do_a_manual_task.apply_async(poll.id)
	"""
	logger = do_a_manual_task.get_logger()
	try:
		poll = Poll.objects.get(pk=poll_id)
		poll.save()
		logger.info('The question was %s' % poll.question)
	except Poll.DoesNotExist:
		logger.info('Poll dees not exist in database!')


@periodic_task(run_every=crontab(minute='*/10'))
def cleanup_database():
	"""
	this is an example of periodic_task that will be executed on every 10 minutes
	this task will basically removed polls that were created 30 minutes before
	for periodic_task we need to define a schedulers 
	we have define CELERYBEAT_SCHEDULER into settings.py
	"""
	expiry_date = datetime.datetime.utcnow().replace(tzinfo=timezone.utc) - datetime.timedelta(minutes=30)
	Poll.objects.filter(created_at__lt=expiry_date).delete()
	pass