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
        return Inertia::render('Charts', [

        ]);
    }
}
