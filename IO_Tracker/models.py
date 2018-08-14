from django.db import models
from django.utils import timezone
# Create your models here.


class IO(models.Model):
	TPN = 'TPN'
	LIPID = 'LIP'
	ENTERAL = 'ENT'
	BOTTLE = 'BOT'
	MEDS = 'MED'
	DIAPER = 'DIA'
	EMESIS = 'EME'
	GASTRIC = 'GAS'
	IO_Choices = (
		(TPN, 'TPN'),
		(LIPID, 'Lipids'),
		(ENTERAL, 'Enteral Feeds'),
		(BOTTLE, 'Bottle Feeds'),
		(MEDS, 'Medications'),
		(DIAPER, 'Diaper'),
		(EMESIS, 'Emesis'),
		(GASTRIC, 'Gastric Output')
		)
	input_type = models.CharField(
		max_length=3,
		choices =IO_Choices,
		default=TPN,
		)
	# quantity = models.PositiveSmallIntegerField()
	quantity = models.DecimalField(max_digits=5, decimal_places=2)
	note = models.TextField(blank=True)
	event_date = models.DateTimeField(
            default=timezone.now)
	create_date = models.DateTimeField(
            default=timezone.now)
	test = models.TextField(blank=True)
	urineFlag = models.BooleanField(default=False)
	poopFlag = models.BooleanField(default=False)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	def __str__(self):
	        return '%s %s' % (self.input_type, self.event_date.date())