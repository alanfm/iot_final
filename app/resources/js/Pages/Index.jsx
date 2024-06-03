import { Head, Link } from "@inertiajs/react";

export default function Index() {
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
                        <span className="flex justify-center flex-1 pb-2 border-b-2 border-transparent">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="w-8 h-8" viewBox="0 0 16 16">
                                <path fillRule="evenodd" d="M6 3.5A1.5 1.5 0 0 1 7.5 2h1A1.5 1.5 0 0 1 10 3.5v1A1.5 1.5 0 0 1 8.5 6v1H14a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0v-1A.5.5 0 0 1 2 7h5.5V6A1.5 1.5 0 0 1 6 4.5zM8.5 5a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5zM0 11.5A1.5 1.5 0 0 1 1.5 10h1A1.5 1.5 0 0 1 4 11.5v1A1.5 1.5 0 0 1 2.5 14h-1A1.5 1.5 0 0 1 0 12.5zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5zm4.5.5A1.5 1.5 0 0 1 7.5 10h1a1.5 1.5 0 0 1 1.5 1.5v1A1.5 1.5 0 0 1 8.5 14h-1A1.5 1.5 0 0 1 6 12.5zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5zm4.5.5a1.5 1.5 0 0 1 1.5-1.5h1a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1-1.5 1.5h-1a1.5 1.5 0 0 1-1.5-1.5zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5z"/>
                            </svg>
                        </span>
                        <span className="flex justify-center flex-1 pb-2 border-b-2 border-transparent">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="w-8 h-8" viewBox="0 0 16 16">
                                <path d="M9.5 12.5a1.5 1.5 0 1 1-2-1.415V9.5a.5.5 0 0 1 1 0v1.585a1.5 1.5 0 0 1 1 1.415"/>
                                <path d="M5.5 2.5a2.5 2.5 0 0 1 5 0v7.55a3.5 3.5 0 1 1-5 0zM8 1a1.5 1.5 0 0 0-1.5 1.5v7.987l-.167.15a2.5 2.5 0 1 0 3.333 0l-.166-.15V2.5A1.5 1.5 0 0 0 8 1"/>
                            </svg>
                        </span>
                        <Link href="/charts" className="flex justify-center flex-1 pb-2 border-b-2 border-transparent">
                            <span>
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="w-8 h-8" viewBox="0 0 16 16">
                                    <path d="M4 11H2v3h2zm5-4H7v7h2zm5-5v12h-2V2zm-2-1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM6 7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm-5 4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1z"/>
                                </svg>
                            </span>
                        </Link>
                    </div>
                </div>
                <div className="p-2 ml-2 mr-2 bg-white rounded-md shadow-md">
                    <div className="flex flex-wrap">
                        <div className="flex-1 flex flex-col justify-center">
                            <div className="pl-2 text-xl">Sensor 1</div>
                        </div>
                        <div className="rounded-full w-14 h-14 bg-red-500 flex justify-center items-center text-white">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="w-8 h-8" viewBox="0 0 16 16">
                                <path d="M9 11c.628-.836 1-1.874 1-3a4.98 4.98 0 0 0-1-3h4a3 3 0 1 1 0 6z"/>
                                <path d="M5 12a4 4 0 1 1 0-8 4 4 0 0 1 0 8m0 1A5 5 0 1 0 5 3a5 5 0 0 0 0 10"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div className="p-2 ml-2 mr-2 bg-white rounded-md shadow-md">
                    <div className="flex flex-wrap">
                        <div className="flex-1 flex flex-col justify-center">
                            <div className="pl-2 text-xl">Sensor 2</div>
                        </div>
                        <div className="rounded-full w-14 h-14 bg-green-500 flex justify-center items-center text-white">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="h-8 w-8" viewBox="0 0 16 16">
                                <path d="M7 5H3a3 3 0 0 0 0 6h4a5 5 0 0 1-.584-1H3a2 2 0 1 1 0-4h3.416q.235-.537.584-1"/>
                                <path d="M16 8A5 5 0 1 1 6 8a5 5 0 0 1 10 0"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div className="p-2 ml-2 mr-2 bg-white rounded-md shadow-md">
                    <div className="flex flex-wrap">
                        <div className="flex-1 flex flex-col justify-center">
                            <div className="pl-2 text-xl">Sensor 3</div>
                        </div>
                        <div className="rounded-full w-14 h-14 bg-green-500 flex justify-center items-center text-white">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="h-8 w-8" viewBox="0 0 16 16">
                                <path d="M7 5H3a3 3 0 0 0 0 6h4a5 5 0 0 1-.584-1H3a2 2 0 1 1 0-4h3.416q.235-.537.584-1"/>
                                <path d="M16 8A5 5 0 1 1 6 8a5 5 0 0 1 10 0"/>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

