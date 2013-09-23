from django.db import models
from django.utils import timezone
import datetime

class Poll(models.Model):
    question = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <  now

    was_published_recently.admin_order_dield = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    search_fields = ['question']
    date_hierarchy = 'pub_date'


class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.choice_text

