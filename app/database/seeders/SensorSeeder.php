<?php

namespace Database\Seeders;

use App\Models\Environment;
use App\Models\Sensor;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class SensorSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        foreach (Environment::get() as $environment) {
            Sensor::insert([
                ['name' => 'Luminosidade', 'status' => 1, 'slug' => 'lux', 'type' => 1, 'environment_id' => $environment->id, 'created_at' => date('Y-m-d H:i:s'), 'updated_at' => date('Y-m-d H:i:s')],
                ['name'=> 'Umidade', 'status'=> 1, 'slug' => 'hum', 'type' => 1, 'environment_id' => $environment->id, 'created_at' => date('Y-m-d H:i:s'), 'updated_at' => date('Y-m-d H:i:s')],
                ['name'=> 'Temperatura', 'status'=> 1, 'slug' => 'temp', 'type' => 1, 'environment_id' => $environment->id, 'created_at' => date('Y-m-d H:i:s'), 'updated_at' => date('Y-m-d H:i:s')],
                ['name'=> 'Porta', 'status'=> 1, 'slug' => 'door', 'type' => 2, 'environment_id' => $environment->id, 'created_at' => date('Y-m-d H:i:s'), 'updated_at' => date('Y-m-d H:i:s')],
                ['name'=> 'Iluminação', 'status'=> 1, 'slug' => 'light', 'type' => 2, 'environment_id' => $environment->id, 'created_at' => date('Y-m-d H:i:s'), 'updated_at' => date('Y-m-d H:i:s')],
                ['name'=> 'Ar Condicionado', 'status'=> 1, 'slug' => 'air', 'type' => 2, 'environment_id' => $environment->id, 'created_at' => date('Y-m-d H:i:s'), 'updated_at' => date('Y-m-d H:i:s')],
            ]);
        }
    }
}
