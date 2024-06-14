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
            return to_route('home');
        } catch (\Exception $e) {
            return back()->with('error', $e->getMessage());
        }
    }
}
