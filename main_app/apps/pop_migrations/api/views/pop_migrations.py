
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from main_app.apps.pop_migrations.api.serializers.pop_migrations import MainTableSerializers
from main_app.apps.pop_migrations.models import MainTable


class MainTableView(ListAPIView):
    serializer_class = MainTableSerializers
    permission_classes = (AllowAny,)
    queryset = MainTable.objects.all().order_by('id')
    paginate_by = 5