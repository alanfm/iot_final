import Button from "@/Components/dashboard/Button";

export default function Sensor({data}) {
    let status = data.status == 1? 2: 1
    return (<div className="flex flex-wrap border-t border-gray-400 py-2">
        <div className="flex-1 flex flex-col justify-center">
            <div className="pl-2 text-xl">{data.name}</div>
        </div>
        <Button status={status} href={route('sensor.toggle.status', {id: data.id})} data={{status}}/>
    </div>)
}
