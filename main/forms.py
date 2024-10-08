from django.forms import ModelForm
from main.models import ItemEntry
from django.utils.html import strip_tags

class ItemEntryForm(ModelForm):
    class Meta:
        model = ItemEntry
        fields = ["name", "price", "description", "rarity"]

    def clean_item(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_feelings(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)