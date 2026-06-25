import React, { useEffect } from 'react'
import { IoCloseCircle } from "react-icons/io5";

type ModalSize = "sm" | "md" | "lg"

interface ModalProps {
    isOpen: boolean,
    onClose: () => void,
    title: string,
    children: React.ReactNode,
    footer?: React.ReactNode,
    size?: ModalSize,
    closeOnBackdrop?: boolean
}

const sizeClasses: Record<ModalSize, string> = {
    sm: "max-w-[360px]",
    md: "max-w-[480px]",
    lg: "max-w-[640px]",
}

const Modal = ({ isOpen, onClose, title, children, footer, size = "md", closeOnBackdrop = true }: ModalProps) => {

    useEffect(() => {
        const handleKey = (evt: KeyboardEvent) => {
            if (evt.key === "Escape" && isOpen) onClose()
        }
        document.addEventListener("keydown", handleKey)
        return () => document.removeEventListener("keydown", handleKey)
    }, [isOpen, onClose])

    useEffect(() => {
        document.body.style.overflow = isOpen ? "hidden" : ""
        return () => { document.body.style.overflow = "" }
    }, [isOpen])

    const handleBackdrop = (evt: React.MouseEvent<HTMLDivElement>) => {
        if (closeOnBackdrop && evt.target === evt.currentTarget) onClose()
    }

    return (
        <div
            onClick={handleBackdrop}
            className={[
                "fixed inset-0 z-50 flex items-center justify-center p-4",
                "bg-neutral-50/75",
                "transition-opacity duration-200",
                isOpen ? "opacity-100 pointer-events-auto" : "opacity-0 pointer-events-none",
            ].join(' ')}
            aria-modal="true"
            role='dialog'
        >
            <div
                className={[
                    "relative w-full flex flex-col bg-white rounded-modal shadow-modal",
                    "max-h-[calc(100vh-2rem)] overflow-hidden",
                    "transition-all duration-250",
                    isOpen ? "opacity-100 translate-y-0 scale-100" : "opacity-0 translate-y-4 scale-[0.97]",
                    sizeClasses[size],
                ].join(' ')}
            >
                <div className='relative flex items-center justify-center px-6 pt-5 pb-4 border-b border-neutral-600 shrink-0'>
                    <h2 className="text-xl font-medium text-primary-500">{title}</h2>
                    <button onClick={onClose} className='absolute right-4 p-1 rounded-md text-text-primary hover:text-text-primary hover:bg-neutral-100 transition-colors'>
                        <IoCloseCircle />
                    </button>
                </div>

                <div className='px-6 py-5 overflow-y-auto flex-1 flex items-center justify-center'>
                    {children}
                </div>

                {footer && (
                    <div className="flex justify-end gap-2 px-6 pb-5 pt-3 border-t border-neutral-600 shrink-0">
                        {footer}
                    </div>
                )}
            </div>
        </div>
    )
}

export default Modal