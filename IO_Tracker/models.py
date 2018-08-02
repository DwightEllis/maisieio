from django.db import models
from django.utils import timezone
# Create your models here.


class IO(models.Model):
	TPN = 'TPN'
	LIPID = 'LIP'
	ENTERAL = 'ENT'
	BOTTLE = 'BOT'
	MEDS = 'MED'
	URINE = 'URI'
	POOP = 'POO'
	EMESIS = 'EME'
	GASTRIC = 'GAS'
	IO_Choices = (
		(TPN, 'TPN'),
		(LIPID, 'Lipids'),
		(ENTERAL, 'Enteral Feeds'),
		(BOTTLE, 'Bottle Feeds'),
		(MEDS, 'Medications'),
		(URINE, 'Urine'),
		(POOP, 'Poop'),
		(EMESIS, 'Emesis'),
		(GASTRIC, 'Gastric Output')
		)
	input_type = models.CharField(
		max_length=3,
		choices =IO_Choices,
		default=TPN,
		)
	quantity = models.PositiveSmallIntegerField()
	note = models.TextField(blank=True)
	event_date = models.DateTimeField(
            default=timezone.now)
	create_date = models.DateTimeField(
            default=timezone.now)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

