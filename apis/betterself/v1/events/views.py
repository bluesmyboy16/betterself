from rest_framework.generics import ListCreateAPIView

from apis.betterself.v1.events.filters import SupplementEventFilter, UserActivityFilter, UserActivityEventFilter, \
    DailyProductivityLogFilter
from apis.betterself.v1.events.serializers import SupplementEventCreateUpdateSerializer, \
    SupplementEventReadOnlySerializer, ProductivityLogReadSerializer, ProductivityLogCreateSerializer, \
    UserActivitySerializer, UserActivityEventCreateSerializer, UserActivityEventReadSerializer, \
    UserActivityUpdateSerializer
from apis.betterself.v1.utils.views import ReadOrWriteSerializerChooser, UUIDDeleteMixin, UUIDUpdateMixin
from config.pagination import ModifiedPageNumberPagination
from events.models import SupplementEvent, DailyProductivityLog, UserActivity, UserActivityEvent


class SupplementEventView(ListCreateAPIView, ReadOrWriteSerializerChooser, UUIDDeleteMixin, UUIDUpdateMixin):
    model = SupplementEvent
    read_serializer_class = SupplementEventReadOnlySerializer
    write_serializer_class = SupplementEventCreateUpdateSerializer
    update_serializer_class = SupplementEventCreateUpdateSerializer
    filter_class = SupplementEventFilter
    pagination_class = ModifiedPageNumberPagination

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).select_related('supplement')

    def get_serializer_class(self):
        return self._get_read_or_write_serializer_class()


class ProductivityLogView(ListCreateAPIView, ReadOrWriteSerializerChooser, UUIDDeleteMixin):
    model = DailyProductivityLog
    pagination_class = ModifiedPageNumberPagination
    read_serializer_class = ProductivityLogReadSerializer
    write_serializer_class = ProductivityLogCreateSerializer
    filter_class = DailyProductivityLogFilter

    def get_serializer_class(self):
        return self._get_read_or_write_serializer_class()

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class UserActivityView(ListCreateAPIView, UUIDDeleteMixin, UUIDUpdateMixin):
    model = UserActivity
    serializer_class = UserActivitySerializer
    filter_class = UserActivityFilter
    pagination_class = ModifiedPageNumberPagination
    update_serializer_class = UserActivityUpdateSerializer

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class UserActivityEventView(ListCreateAPIView, ReadOrWriteSerializerChooser, UUIDDeleteMixin, UUIDUpdateMixin):
    model = UserActivityEvent
    pagination_class = ModifiedPageNumberPagination
    read_serializer_class = UserActivityEventReadSerializer
    write_serializer_class = UserActivityEventCreateSerializer
    update_serializer_class = UserActivityEventCreateSerializer
    filter_class = UserActivityEventFilter

    def get_serializer_class(self):
        return self._get_read_or_write_serializer_class()

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).select_related('user_activity')
