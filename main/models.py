import uuid
from django.db import models
from django.contrib.auth.models import User

class ItemEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	description = models.TextField()
	access_time = models.DateField(auto_now_add=True)
	rarity = models.IntegerField()

	@property
	def name_rarity(self):
		if self.rarity == 1:
			return 'Common'
		elif self.rarity == 2:
			return 'Uncommon'
		elif self.rarity == 3:
			return 'Great'
		elif self.rarity == 4:
			return 'Rare'
		elif self.rarity == 5:
			return 'Epic'
		elif self.rarity == 6:
			return 'Legendary'
		elif self.rarity == 7:
			return 'Mythical'
		else:
			return 'One of a Kind'
	def is_rare(self):
		return self.rarity > 3