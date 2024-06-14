<?php

namespace App\Http\Controllers;

use App\Models\Sensor;
use Inertia\Inertia;
use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function index(Request $request)
    {
        return Inertia::render('Index', [
            'sensors' => Sensor::select('id', 'name', 'status', 'slug')->get(),
        ]);
    }

    public function charts(Request $request)
    {
        $lux = Sensor::where('slug', 'lux')->first()?->data()->orderBy('created_at', 'desc')->get()->take(10)->map(function ($data) {
            return [
                'value' => $data->value,
                'date' => $data->created_at->format('H:i:s'),
            ];
        });

        $hum = Sensor::where('slug', 'hum')->first()?->data()->orderBy('created_at', 'desc')->get()->take(20)->map(function ($data) {
            return [
                'value' => $data->value,
                'date' => $data->created_at->format('H:i:s'),
            ];
        });

        $temp = Sensor::where('slug', 'temp')->first()?->data()->orderBy('created_at', 'desc')->get()->take(20)->map(function ($data) {
            return [
                'value' => $data->value,
                'date' => $data->created_at->format('H:i:s'),
            ];
        });

        return Inertia::render('Charts', [
            'lux' => $lux,
            'hum' => $hum,
            'temp' => $temp,
        ]);
    }
}
