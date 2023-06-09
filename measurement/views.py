from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     ListCreateAPIView,
                                     UpdateAPIView)

from .models import Sensor, Measurements
from .serializers import (SensorSerializer,
                          SensorFullInfoSerializer,
                          MeasurementSerializer)


class sensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class sensor_create(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class sensor_change(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class sensor_view_info(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorFullInfoSerializer


class measure_create(ListCreateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer
