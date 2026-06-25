import React from 'react'
import { FaChevronCircleDown } from "react-icons/fa";
import type { SelectOption } from './Input'

interface SelectInputProps {
    id: string,
    label: string,
    name: string,
    value?: string | number,
    options: SelectOption[],
    error?: string,
    hint?: string,
    disabled?: boolean,
    onChange: (evt: React.ChangeEvent<HTMLSelectElement>) => void
}

const SelectInput = ({ id, label, name, value, options, error, hint, disabled, onChange }: SelectInputProps) => {
    return (
        <div className={`field ${error ? "field-error" : ""}`}>
            <select
                id={id}
                name={name}
                value={value}
                disabled={disabled}
                onChange={onChange}
                className={`field-input field-select ${value ? "has-value" : ""}`}
            >
                <option value="" disabled hidden></option>
                {options.map(opt => (
                    <option key={opt.value} value={opt.value}>{opt.label}</option>
                ))}
            </select>
            <label htmlFor={id} className='field-label'>{label}</label>
            <span className='field-select-arrow'>{<FaChevronCircleDown />}</span>
            {error && <span className='field-msg field-msg--error'>{error}</span>}
            {hint && !error && <span className='field-msg field-msg--hint'>{hint}</span>}
        </div>
    )
}

export default SelectInput