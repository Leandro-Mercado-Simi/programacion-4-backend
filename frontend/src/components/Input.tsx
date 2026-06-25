import React from 'react'
import TextInput from './TextInput'
import SelectInput from './SelectInput'
import ToggleInput from './ToggleInput'

export type SelectOption = { value: string | number, label: string }

type InputBaseProps = {
    id: string,
    label: string,
    name: string,
    error?: string,
    hint?: string,
    disabled?: boolean
}

type TextInputProps = InputBaseProps & {
    type: "text" | "email" | "number" | "password",
    value?: string | number,
    onChange: (evt: React.ChangeEvent<HTMLInputElement>) => void
}

type SelectInputProps = InputBaseProps & {
    type: "select"
    options: SelectOption[]
    value?: string | number
    onChange: (evt: React.ChangeEvent<HTMLSelectElement>) => void
}

type RadioInputProps = InputBaseProps & {
    type: "radio"
    value: string | number
    checked: boolean
    onChange: (evt: React.ChangeEvent<HTMLInputElement>) => void
}

type CheckboxInputProps = InputBaseProps & {
    type: "checkbox"
    checked: boolean
    value: string | number
    onChange: (evt: React.ChangeEvent<HTMLInputElement>) => void
}

export type CustomInputProps = | TextInputProps | SelectInputProps | RadioInputProps | CheckboxInputProps

const Input = (props: CustomInputProps) => {
    switch (props.type) {
        case "text":
        case "email":
        case "number":
        case "password":
            return <TextInput {...props} />
        case "select":
            return <SelectInput {...props} />
        case "radio":
        case "checkbox":
            return <ToggleInput {...props} />
        default:
            return null;
    }
}

export default Input