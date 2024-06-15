<?php

use App\Http\Controllers\EnvironmentController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\SensorController;

Route::get('/', [HomeController::class, 'index'])->name('home');
Route::get('/charts', [HomeController::class, 'charts'])->name('charts');
Route::post('/sensor/toggle/status/{sensor:id}', [SensorController::class, 'toggleStatus'])->name('sensor.toggle.status');

Route::resource('environment', EnvironmentController::class);

/**
 * Status Atuadores
 * Status Sensores
 * Ambiente - lux e temp
 *
 * response - json
 */
Route::get('/environment/all', [HomeController::class, 'index'])->name('');

/**
 * lux_value
 * hum_value
 * temp_value
 */
Route::post('/sensor/all', [HomeController::class, 'index'])->name('');


