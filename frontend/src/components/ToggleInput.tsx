import React from 'react'

type ToggleTpe = "radio" | "checkbox"

interface ToggleInputProps {
    id: string,
    label: string,
    name: string,
    value: string | number,
    type: ToggleTpe,
    checked?: boolean,
    error?: string,
    hint?: string,
    disabled?: boolean,
    onChange: (evt: React.ChangeEvent<HTMLInputElement>) => void
}

const ToggleInput = ({ type, ...props }: ToggleInputProps) => {
    return (
        <div className={`field-toggle ${props.error ? 'field-error' : ''} w-full gap-x-5`}>
            <label htmlFor={props.id} className='text-primary-500'>{props.label}</label>
            <input type={type} {...props} />
            {props.error && <span className='field-msg field-msg--error'>{props.error}</span>}
            {props.hint && !props.error && <span className='field-msg field-msg--hint'>{props.hint}</span>}
        </div>
    )
}

export default ToggleInput