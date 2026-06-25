import React, { useState } from 'react'
import { FaRegEye, FaRegEyeSlash } from "react-icons/fa";

interface TextInputProps {
    id: string,
    label: string,
    name: string,
    type: "text" | "email" | "number" | "password",
    value?: string | number,
    error?: string
    hint?: string,
    disabled?: boolean,
    onChange: (evt: React.ChangeEvent<HTMLInputElement>) => void
}

const TextInput = ({ id, label, name, type, value, error, hint, disabled, onChange }: TextInputProps) => {

    const [showPassword, setShowPassword] = useState(false);
    const inputType = type === "password" ? (showPassword ? "text" : "password") : type

    return (
        <div className={`field ${error ? "field-error" : ""}`}>
            <input
                id={id}
                name={name}
                type={inputType}
                value={value}
                disabled={disabled}
                onChange={onChange}
                placeholder=" "
                className='field-input'
            />
            <label htmlFor={id} className='field-label'>{label}</label>
            {
                type === "password" && (
                    <button
                        type='button'
                        tabIndex={-1}
                        onClick={() => setShowPassword(prev => !prev)}
                        className='field-pw-toggle'
                    >
                        {!showPassword ?
                            (<FaRegEye />)
                            :
                            (<FaRegEyeSlash />)
                        }
                    </button>
                )}
            {error && <span className='field-msg field-msg--error'>{error}</span>}
            {hint && !error && <span className='field-msg field-msg--hint'>{hint}</span>}

        </div>
    )
}

export default TextInput