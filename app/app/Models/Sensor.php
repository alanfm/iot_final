<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Sensor extends Model
{
    use HasFactory;

    public const SENSOR = 1;
    public const ACTUATOR = 2;

    protected $fillable = [
        'name',
        'status',
        'slug',
        'environment_id',
    ];

    public function data(): HasMany
    {
        return $this->hasMany(Data::class);
    }

    public function environment(): BelongsTo
    {
        return $this->belongsTo(Environment::class);
    }
}
