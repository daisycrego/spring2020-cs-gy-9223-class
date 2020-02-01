from django.shortcuts import render
from django.views.generic import TemplateView

from mercury.models import (
    TemperatureSensor,
    AccelerationSensor,
    WheelSpeedSensor,
    SuspensionSensor,
    FuelLevelSensor,
    WindSpeedSensor
)
from ..event_check import require_event_code


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    @require_event_code
    def get(self, request, *args, **kwargs):
        temp_data = TemperatureSensor.objects.all().order_by("-created_at")
        accel_data = AccelerationSensor.objects.all().order_by("-created_at")
        ws_data = WheelSpeedSensor.objects.all().order_by("-created_at")
        ss_data = SuspensionSensor.objects.all().order_by("-created_at")
        fl_data = FuelLevelSensor.objects.all().order_by("-created_at")
        wind_speed_data = WindSpeedSensor.objects.all().order_by("-created_at")
        context = {
            "temp_data": temp_data,
            "accel_data": accel_data,
            "ws_data": ws_data,
            "ss_data": ss_data,
            "fl_data": fl_data,
            "wind_speed_data": wind_speed_data
        }
        return render(request, self.template_name, context)
