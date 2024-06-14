<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\SensorController;

Route::get('/', [HomeController::class, 'index'])->name('home');
Route::get('/charts', [HomeController::class, 'charts'])->name('charts');
Route::post('/sensor/toggle/status/{sensor:id}', [SensorController::class, 'toggleStatus'])->name('sensor.toggle.status');

