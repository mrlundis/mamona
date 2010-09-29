from django.db import models
from django.utils.translation import ugettext_lazy as _

from mamona.abstract_mixin import AbstractMixin

BACKEND_NAME = _("A dummy backend for testing purposes")

class DummyTxnFactory(models.Model, AbstractMixin):
	comment = models.CharField(max_length=100, default="a dummy transaction")

	class Meta:
		abstract = True

	@classmethod
	def contribute(cls, payment):
		return {'payment': models.OneToOneField(payment)}

DummyTxn = None

def build_models(payment_class):
	global DummyTxn
	class DummyTxn(DummyTxnFactory.construct(payment_class)):
		pass
	return [DummyTxn]
