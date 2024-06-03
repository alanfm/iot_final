<?php

namespace App\Http\Controllers;

use Inertia\Inertia;
use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function index(Request $request)
    {
        return Inertia::render('Index', [

        ]);
    }

    public function charts(Request $request)
    {
        return Inertia::render('Charts', [

        ]);
    }
}
