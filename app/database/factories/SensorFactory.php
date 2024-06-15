<?php

namespace Database\Factories;

use App\Models\Environment;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Sensor>
 */
class SensorFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'name' => $this->faker->word,
            'status' => $this->faker->randomElement([1, 2]),
            'slug' => $this->faker->slug,
            'type' => $this->faker->randomElement([1,2]),
            'environment_id' => Environment::all()->random()->id,
        ];
    }
}
