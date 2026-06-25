import React from 'react'
import Spinner from './Spinner';

interface Column<T> {
    header: string;
    field: keyof T;
    render?: (value: T) => React.ReactNode;
}

interface DataTableProps<T> {
    columns: Column<T>[];
    data: T[];
    isLoading?: boolean;
    emptyMessage?: string;
    filters?: React.ReactNode
    onRowClick?: (item: T) => void
}


const DataTable = <T extends { id: number | string }>({ columns, data, isLoading, emptyMessage, filters, onRowClick }: DataTableProps<T>) => {

    if (isLoading) return (
        <div className='flex justify-center py-12'>
            <Spinner message='Cargando, por favor espere...' />
        </div>
    )

    if (data.length === 0) return (
        <div className='text-center py-12 text-text-primary text-sm'>
            {emptyMessage}
        </div>
    )

    return (
        <div className="w-full rounded-xl border border-neutral-200 bg-bg-subtle shadow-xs overflow-hidden">
            {filters && (
                <div className="p-4 border-b border-neutral-200 bg-neutral-50/50 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                    {filters}
                </div>
            )}

            <div className="w-full overflow-x-auto block">
                <table className="w-full text-sm table-fixed">
                    <colgroup>
                        {columns.map((column) => (
                            <col
                                key={column.header}
                                style={{
                                    width: column.header === "Acciones"
                                        ? "240px"
                                        : column.header === "N°"
                                            ? "60px"
                                            : undefined
                                }}
                            />
                        ))}
                    </colgroup>
                    <thead>
                        <tr className="border-b border-neutral-300 bg-bg-inverse">
                            {columns.map((column) => (
                                <th
                                    key={column.header}
                                    className={`px-4 py-3 bg-primary-200 text-left font-medium text-text-primary ${column.header === "Acciones" ? "text-right" : ""}`}>
                                    {column.header}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-neutral-200">
                        {data.map((item) => (
                            <tr
                                key={item.id}
                                onClick={() => onRowClick?.(item)}
                                className={`hover:bg-gray-200 transition-colors ${onRowClick ? "cursor-pointer" : ""
                                    }`}
                            >
                                {columns.map((column) => (
                                    <td
                                        key={column.header}
                                        className={`px-4 py-3 text-text-primary ${column.header === "Acciones" ? "text-right" : "truncate"}`}
                                    >
                                        {column.render
                                            ? column.render(item)
                                            : (item[column.field] as React.ReactNode)}
                                    </td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default DataTable