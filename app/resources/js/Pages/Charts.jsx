import { Head, Link } from "@inertiajs/react";

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import { Bar, Line } from 'react-chartjs-2';
import faker from 'faker';
import { useEffect, useState } from "react";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    BarElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

export default function Charts({lux, hum, temp}) {
    const [luxChart, setLuxChart] = useState({values: [], dates: []})
    const [humChart, setHumChart] = useState({values: [], dates: []})
    const [tempChart, setTempChart] = useState({values: [], dates: []})

    useEffect(() => {
        lux.map(v => {
            let t = luxChart
            t.values.push(v.value)
            t.dates.push(v.date)
            setLuxChart(t)
        })


        hum.map(v => {
            let t = humChart
            t.values.push(v.value)
            t.dates.push(v.date)
            setHumChart(t)
        })


        temp.map(v => {
            let t = tempChart
            t.values.push(v.value)
            t.dates.push(v.date)
            setTempChart(t)
        })
    }, [lux, hum, temp])

    console.log(luxChart)

    const optionsLuxChart = {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
                display: false
            },
            title: {
                display: true,
                text: 'Dados do sensor de Luminosidade',
            },
        },
    };

    const optionsHumChart = {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
                display: false
            },
            title: {
                display: true,
                text: 'Dados do sensor de Umidade',
            },
        },
    };

    const optionsTempChart = {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
                display: false
            },
            title: {
                display: true,
                text: 'Dados do sensor de Temperatura',
            },
        },
    };

    const dataLux = {
        labels: luxChart.dates,
        datasets: [
            {
                label: 'valor',
                data: luxChart.values,
                backgroundColor: '#fdfd96',
            },
        ],
    };

    const dataHum = {
        labels: humChart.dates,
        datasets: [
            {
                label: 'valor',
                data: humChart.values,
                backgroundColor: '#77dd77',
            },
        ],
    };

    const dataTemp = {
        labels: tempChart.dates,
        datasets: [
            {
                label: 'valor',
                data: tempChart.values,
                backgroundColor: '#84b6f4',
            },
        ],
    };

    return (
        <>
            <Head title="Home" />
            <div className="flex flex-col w-screen h-screen gap-4 text-gray-600 bg-slate-200">
                <div className="flex flex-col bg-white shadow-md">
                    <div className="flex-1 w-full p-4 text-xl font-semibold text-center">Gerenciamento de Sensores</div>
                    <div className="flex flex-wrap">
                        <Link href="/" className="flex justify-center flex-1 pb-2 border-b-2 border-transparent">
                            <span >
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="w-8 h-8" viewBox="0 0 16 16">
                                    <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5z"/>
                                </svg>
                            </span>
                        </Link>
                        <Link href="/charts" className="flex justify-center flex-1 pb-2 text-blue-500 border-b-2 border-blue-500">
                            <span>
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="w-8 h-8" viewBox="0 0 16 16">
                                    <path d="M4 11H2v3h2zm5-4H7v7h2zm5-5v12h-2V2zm-2-1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM6 7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm-5 4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1z"/>
                                </svg>
                            </span>
                        </Link>
                    </div>
                </div>
                <div className="flex flex-col gap-4 md:flex-row md:grid md:grid-cols-2 md:h-1/4 lg:grid-cols-3">
                    <div className="p-2 ml-2 mr-2 bg-white rounded-md shadow-md">
                        <Line options={optionsLuxChart} data={dataLux} />
                    </div>
                    <div className="p-2 ml-2 mr-2 bg-white rounded-md shadow-md">
                        <Line options={optionsHumChart} data={dataHum} />
                    </div>
                    <div className="p-2 ml-2 mr-2 bg-white rounded-md shadow-md">
                        <Line options={optionsTempChart} data={dataTemp} />
                    </div>
                </div>
            </div>
        </>
    );
}

