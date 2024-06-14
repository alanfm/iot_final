<?php

namespace Database\Seeders;

use App\Models\Data;
use App\Models\Sensor;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DataSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        Sensor::get()->map(function ($sensor) {
            Data::factory()->count(40)->state(['sensor_id' => $sensor->id])->create();
        });
    }
}
