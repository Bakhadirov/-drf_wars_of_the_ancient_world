from rest_framework import serializers

from main_app.apps.pop_migrations.models import MainTable


class MainTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = MainTable
        fields = '__all__'