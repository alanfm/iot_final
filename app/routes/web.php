<?php

use App\Http\Controllers\EnvironmentController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\SensorController;

Route::get('/', [HomeController::class, 'index'])->name('home');
Route::get('/charts', [HomeController::class, 'charts'])->name('charts');
Route::post('/sensor/toggle/status/{sensor:id}', [SensorController::class, 'toggleStatus'])->name('sensor.toggle.status');

Route::resource('environment', EnvironmentController::class);
// Route::get('environment/{id:environment}/edit', [EnvironmentController::class, 'edit'])->name('environment.edit');
// Route::put('environment/{id:environment}/edit', [EnvironmentController::class, 'update'])->name('environment.update');

/**
 * Status Atuadores
 * Status Sensores
 * Ambiente - lux e temp
 * name
 * id
 *
 * response - json
 */
Route::get('env/all', [EnvironmentController::class, 'all'])->name('environment.all');

/**
 * lux_value
 * hum_value
 * temp_value
 */
Route::post('sensor/all', [SensorController::class, 'all'])->name('sensor.all');


