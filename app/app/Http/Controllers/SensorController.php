<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreSensorRequest;
use App\Http\Requests\UpdateSensorRequest;
use App\Models\Sensor;
use PhpMqtt\Client\Facades\MQTT;

class SensorController extends Controller
{
    public function toggleStatus(UpdateSensorRequest $request, Sensor $sensor)
    {
        $_mqtt = [
            'air' => [
                'topic' => 'cmnd/IoT-UFC/arcond/irsend',
                'cmd' => [
                    '{\"Protocol\":\"COOLIX\",\"Bits\":24,\"Data\":\"0xB27BE0\",\"DataLSB\":\"0x4DDE07\",\"Repeat\":0,\"IRHVAC\":{\"Vendor\":\"COOLIX\",\"Model\":-1,\"Mode\":\"Cool\",\"Power\":\"Off\",\"Celsius\":\"On\",\"Temp\":17,\"FanSpeed\":\"Auto\",\"SwingV\":\"Off\",\"SwingH\":\"Off\",\"Quiet\":\"Off\",\"Turbo\":\"Off\",\"Econo\":\"Off\",\"Light\":\"Off\",\"Filter\":\"Off\",\"Clean\":\"Off\",\"Beep\":\"Off\",\"Sleep\":-1}}',
                    '{\"Protocol\":\"COOLIX\",\"Bits\":24,\"Data\":\"0xB2BF00\",\"DataLSB\":\"0x4DFD00\",\"Repeat\":0,\"IRHVAC\":{\"Vendor\":\"COOLIX\",\"Model\":-1,\"Mode\":\"Cool\",\"Power\":\"On\",\"Celsius\":\"On\",\"Temp\":17,\"FanSpeed\":\"Auto\",\"SwingV\":\"Off\",\"SwingH\":\"Off\",\"Quiet\":\"Off\",\"Turbo\":\"Off\",\"Econo\":\"Off\",\"Light\":\"Off\",\"Filter\":\"Off\",\"Clean\":\"Off\",\"Beep\":\"Off\",\"Sleep\":-1}}']],
            'light' => [
                'topic' => 'cmnd/IoT-UFC/ligth/power',
                'cmd' => ['ON', 'OFF'],
            ],
            'door' => [
                'topic' => 'cmnd/IoT-UFC/door/power',
                'cmd' => ['ON', 'OFF'],
            ],
        ];

        try {
            if ($sensor->type == Sensor::ACTUATOR) {
                $mqtt = MQTT::connection();
                $mqtt->publish($_mqtt[$sensor->slug]['topic'], $_mqtt[$sensor->slug]['cmd'][$request->status == 2? 0: 1]);
            }

            $sensor->update(['status' => $request->status]);
            return to_route('home');
        } catch (\Exception $e) {
            return back()->with('error', $e->getMessage());
        }
    }

    public function all(StoreSensorRequest $request)
    {
        try {
            $luxSensor = Sensor::where('slug', 'lux')->first();
            $tempSensor = Sensor::where('slug', 'temp')->first();
            $humSensor = Sensor::where('slug', 'hum')->first();

            $luxSensor->data()->create(['value' => $request->lux_value]);
            $tempSensor->data()->create(['value' => $request->temp_value]);
            $humSensor->data()->create(['value' => $request->hum_value]);

            return response()->json(['message' => 'success'], 201);
        } catch (\Exception $e) {
            return response()->json(['message' => 'error'], 400);
        }
    }
}
