from tortoise.fields import UUIDField, CharField, DatetimeField
from tortoise.models import Model


class MinerModel(Model):
    uuid = UUIDField(pk=True)
    name = CharField(max_length=100)
    document_type = CharField(max_length=10)
    document_number = CharField(max_length=20, unique=True)
    municipality = CharField(max_length=100)
    updated_at = DatetimeField(null=True)

    class Meta:
        table = "miners"
