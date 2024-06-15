<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreSensorRequest;
use App\Http\Requests\UpdateSensorRequest;
use App\Models\Sensor;

class SensorController extends Controller
{
    public function toggleStatus(UpdateSensorRequest $request, Sensor $sensor)
    {
        try {
            $sensor->update(['status' => $request->status]);
            // Adicionar o comando para mensagem do MQTT
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
