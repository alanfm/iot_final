<?php

namespace Database\Seeders;

use App\Models\Environment;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class EnvironmentSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        Environment::create([
            'name' => 'Sala',
            'lux' => 350,
            'temp' => 25
        ]);
        
        Environment::create([
            'name' => 'Escritório',
            'lux' => 250,
            'temp' => 20
        ]);
    }
}
