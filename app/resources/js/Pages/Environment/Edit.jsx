import { Head, Link, useForm } from "@inertiajs/react";
import { useEffect, useState } from "react";

export default function Index({environment}) {
    const {data, setData, processing, put} = useForm({
        name: environment.name,
        lux: environment.lux,
        temp: environment.temp
    })

    function submit(e) {
        e.preventDefault()
        put(route('environment.update', {id: environment.id}))
    }

    return (
        <>
            <Head title="Home" />
            <div className="flex flex-col w-screen h-screen gap-4 text-gray-600 bg-slate-200">
                <div className="flex flex-col bg-white shadow-md">
                    <div className="flex-1 w-full p-4 text-xl font-semibold text-center">Gerenciamento de Sensores</div>
                    <div className="flex flex-wrap">
                        <Link href="/" className="flex justify-center flex-1 pb-2 text-blue-500 border-b-2 border-blue-500">
                            <span >
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="w-8 h-8" viewBox="0 0 16 16">
                                    <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5z"/>
                                </svg>
                            </span>
                        </Link>
                        <Link href="/charts" className="flex justify-center flex-1 pb-2 border-b-2 border-transparent">
                            <span>
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="w-8 h-8" viewBox="0 0 16 16">
                                    <path d="M4 11H2v3h2zm5-4H7v7h2zm5-5v12h-2V2zm-2-1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM6 7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm-5 4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1z"/>
                                </svg>
                            </span>
                        </Link>
                    </div>
                </div>
                <div className="flex flex-col gap-4 md:flex-row">
                    <div className="flex flex-col flex-1 gap-2 p-2 ml-2 mr-2 bg-white rounded-md shadow-md">
                        <h1 className="text-lg font-semibold text-center my-2">Editar Ambiente</h1>
                        <form onSubmit={submit} className="flex flex-col gap-2">
                            <div className="flex flex-col">
                                <label htmlFor="">Nome</label>
                                <input type="text" value={data.name} onChange={e => setData('name', e.target.value)} className="border-gray-500 rounded-md" placeholder="Nome do ambiente" />
                            </div>
                            <div className="flex flex-col">
                                <label htmlFor="">Luminosidade padrão</label>
                                <input type="number" value={data.lux} onChange={e => setData('lux', e.target.value)} className="border-gray-500 rounded-md" placeholder="Valor da luminosidade em lumens" />
                            </div>
                            <div className="flex flex-col">
                                <label htmlFor="">Temperatura padrão</label>
                                <input type="number" value={data.temp} onChange={e => setData('temp', e.target.value)} className="border-gray-500 rounded-md" placeholder="Valor da temperatura em Graus Celsius" />
                            </div>
                            <div className="flex justify-center gap-2">
                                <button type="submit" disabled={processing} className="flex justify-between items-center gap-2 rounded-md bg-green-500 text-white py-2 px-3">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="h-4 w-4" viewBox="0 0 16 16">
                                        <path d="M0 1.5A1.5 1.5 0 0 1 1.5 0H3v5.5A1.5 1.5 0 0 0 4.5 7h7A1.5 1.5 0 0 0 13 5.5V0h.086a1.5 1.5 0 0 1 1.06.44l1.415 1.414A1.5 1.5 0 0 1 16 2.914V14.5a1.5 1.5 0 0 1-1.5 1.5H14v-5.5A1.5 1.5 0 0 0 12.5 9h-9A1.5 1.5 0 0 0 2 10.5V16h-.5A1.5 1.5 0 0 1 0 14.5z"/>
                                        <path d="M3 16h10v-5.5a.5.5 0 0 0-.5-.5h-9a.5.5 0 0 0-.5.5zm9-16H4v5.5a.5.5 0 0 0 .5.5h7a.5.5 0 0 0 .5-.5zM9 1h2v4H9z"/>
                                    </svg>
                                    <span>Salvar</span>
                                </button>
                                <Link href={route('home')} className="flex justify-between items-center gap-2 rounded-md bg-gray-500 text-white py-2 px-3">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="h-4 w-4" viewBox="0 0 16 16">
                                        <path fillRule="evenodd" d="M14.5 1.5a.5.5 0 0 1 .5.5v4.8a2.5 2.5 0 0 1-2.5 2.5H2.707l3.347 3.346a.5.5 0 0 1-.708.708l-4.2-4.2a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 8.3H12.5A1.5 1.5 0 0 0 14 6.8V2a.5.5 0 0 1 .5-.5"/>
                                    </svg>
                                    <span>Voltar</span>
                                </Link>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </>
    );
}

