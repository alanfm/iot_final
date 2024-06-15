<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Environment extends Model
{
    use HasFactory;

    protected $fillable = [
        "name",
        "lux",
        "temp",
    ];

    public function sensors(): HasMany
    {
        return $this->hasMany(Sensor::class);
    }
}
