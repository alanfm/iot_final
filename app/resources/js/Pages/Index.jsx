import Sensor from "@/Components/Sensor";
import { Head, Link } from "@inertiajs/react";
import { useEffect, useState } from "react";

export default function Index({sensors, environments}) {
    const [status, setStatus] = useState({})
    const [box, setBox] = useState('')

    useEffect(() => {
        sensors.map(v => {
            let t = status
            t[v.slug] = v.status
            setStatus(t)
        })
    }, [sensors])

    useEffect(() => {
        setBox(environments.map((v, i) => {
            let sensor = []
            let actuator = []
            v.sensors.map((v, i) => {
                if (v.type == 1) {
                    sensor.push(<Sensor key={i + 'sensor'} data={v} />)
                } else {
                    actuator.push(<Sensor key={i + 'actuator'} data={v} />)
                }
            })
            return (
            <div key={i + 'env'} className="flex flex-col gap-2 p-2 ml-2 mr-2 bg-white rounded-md shadow-md md:w-1/2 lg:w-1/3">
                <div className="flex flex-col gap-4">
                    <div className="flex justify-between">
                        <span className="text-lg font-semibold">{v.name}</span>
                        <Link href={route('environment.edit', {id: v.id})} className="flex justify-center items-center gap-1 text-white bg-yellow-500 px-1 rounded-full w-10 h-10">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="w-5 h-5" viewBox="0 0 16 16">
                                <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"/>
                            </svg>
                        </Link>
                    </div>
                    <div className="grid grid-cols-2">
                        <div>
                            <span className="font-light">Luminosidade: </span><span>{v.lux}</span>
                        </div>
                        <div>
                            <span className="font-light">Temperatura: </span><span>{v.temp} °C</span>
                        </div>
                    </div>
                </div>
                <div className="flex flex-col">
                    <div className="flex flex-col border border-gray-400 rounded-md py-1 px-2">
                        <div className="">Atuadores</div>
                        <div className="">
                            {actuator}
                        </div>
                    </div>
                </div>
                <div className="flex flex-col">
                    <div className="flex flex-col border border-gray-400 rounded-md py-1 px-2">
                        <div className="">Sensores</div>
                        <div className="">
                            {sensor}
                        </div>
                    </div>
                </div>
            </div>)
        }))
    }, [environments])

    return (
        <>
            <Head title="Home" />
            <div className="flex flex-col w-screen h-screen gap-4 text-gray-600 bg-slate-200">
                <div className="flex flex-col bg-white shadow-md">
                <div className="flex-1 w-full p-4">
                        <div className="flex justify-center items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="h-10 w-10" viewBox="0 0 16 16">
                                <path d="M6 12.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5M3 8.062C3 6.76 4.235 5.765 5.53 5.886a26.6 26.6 0 0 0 4.94 0C11.765 5.765 13 6.76 13 8.062v1.157a.93.93 0 0 1-.765.935c-.845.147-2.34.346-4.235.346s-3.39-.2-4.235-.346A.93.93 0 0 1 3 9.219zm4.542-.827a.25.25 0 0 0-.217.068l-.92.9a25 25 0 0 1-1.871-.183.25.25 0 0 0-.068.495c.55.076 1.232.149 2.02.193a.25.25 0 0 0 .189-.071l.754-.736.847 1.71a.25.25 0 0 0 .404.062l.932-.97a25 25 0 0 0 1.922-.188.25.25 0 0 0-.068-.495c-.538.074-1.207.145-1.98.189a.25.25 0 0 0-.166.076l-.754.785-.842-1.7a.25.25 0 0 0-.182-.135"/>
                                <path d="M8.5 1.866a1 1 0 1 0-1 0V3h-2A4.5 4.5 0 0 0 1 7.5V8a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1v1a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-1a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1v-.5A4.5 4.5 0 0 0 10.5 3h-2zM14 7.5V13a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V7.5A3.5 3.5 0 0 1 5.5 4h5A3.5 3.5 0 0 1 14 7.5"/>
                            </svg>
                        </div>
                        <h1 className="text-center text-xl font-semibold">Gerenciamento de Ambientes</h1>
                        <h2 className="text-center text-lg -mt-1">Smart Environment</h2>
                    </div>
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
                    {box}
                </div>
            </div>
        </>
    );
}

