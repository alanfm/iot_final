<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreEnvironmentRequest;
use App\Http\Requests\UpdateEnvironmentRequest;
use App\Models\Environment;
use Illuminate\Http\Response;
use Inertia\Inertia;

class EnvironmentController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {

    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreEnvironmentRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Environment $environment)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Environment $environment)
    {
        return Inertia::render('Environment/Edit', [
            'environment' => $environment,
        ]);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateEnvironmentRequest $request, Environment $environment)
    {
        try {
            $environment->update($request->validated());
            return to_route('home')->with('success','Ambiente Atualizado com sucesso!');
        } catch (\Exception $e) {
            return back()->with('error', $e->getMessage());
        }
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Environment $environment)
    {
        //
    }

    public function all()
    {
        $environment = Environment::first();
        $sensors = [];
        foreach($environment->sensors as $sensor) {
            $sensors[$sensor->slug] = $sensor->status == 2? true: false;
        }

        $response = [
            'env_lux' => $environment->lux,
            'env_temp' => $environment->temp,
        ];


        return response()->json(array_merge($response, $sensors));
    }
}
