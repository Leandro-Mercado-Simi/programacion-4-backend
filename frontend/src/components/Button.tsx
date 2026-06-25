import React, { useRef } from 'react'

type Variant = "primary" | "secondary" | "danger" | "success" | "warning" | "info";
type StyleVariant = "filled" | "outlined" | "ghost";
type Size = "sm" | "md" | "lg";

interface ButtonProps {
    children: React.ReactNode;
    variant?: Variant;
    styleVariant?: StyleVariant;
    size?: Size;
    disabled?: boolean;
    loading?: boolean;
    iconLeft?: React.ReactNode;
    iconRight?: React.ReactNode;
    onClick?: React.MouseEventHandler<HTMLButtonElement>;
    type?: "button" | "submit" | "reset";
    className?: string

}

const variantStyles: Record<Variant, Record<StyleVariant, string>> = {
    primary: {
        filled:
            "bg-primary-500 text-white border-0 shadow-shadow-md hover:bg-primary-600 hover:shadow-shadow-lg",
        outlined:
            "bg-transparent text-primary-500 border border-primary-500 hover:bg-primary-50 hover:shadow-[0_2px_8px_rgba(227,90,40,0.15)]",
        ghost:
            "bg-transparent text-primary-500 border-0 hover:bg-transparent p-1",
    },
    secondary: {
        filled:
            "bg-secondary-500 text-text-inverse  border-0 shadow-[0_2px_4px_rgba(245,158,11,0.30)] hover:bg-secondary-600 hover:shadow-[0_4px_10px_rgba(245,158,11,0.36)]",
        outlined:
            "bg-transparent text-secondary-700 border border-secondary-400 hover:bg-secondary-50 hover:shadow-[0_2px_8px_rgba(245,158,11,0.15)]",
        ghost:
            "bg-transparent text-secondary-700 border-0 hover:bg-transparent p-1",
    },
    danger: {
        filled:
            "bg-danger-500 text-white border-0 shadow-[0_2px_4px_rgba(248,53,53,0.28)] hover:bg-danger-600 hover:shadow-[0_4px_10px_rgba(248,53,53,0.36)]",
        outlined:
            "bg-transparent text-danger-600 border border-danger-500 hover:bg-danger-50 hover:shadow-[0_2px_8px_rgba(248,53,53,0.15)]",
        ghost:
            "bg-transparent text-danger-600 border-0 hover:bg-transparent p-1",
    },
    success: {
        filled:
            "bg-success-500 text-white border-0 shadow-[0_2px_4px_rgba(79,131,61,0.28)] hover:bg-success-600 hover:shadow-[0_4px_10px_rgba(79,131,61,0.34)]",
        outlined:
            "bg-transparent text-success-600 border border-success-500 hover:bg-success-50 hover:shadow-[0_2px_8px_rgba(79,131,61,0.15)]",
        ghost:
            "bg-transparent text-success-600 border-0 hover:bg-transparent p-1",
    },
    warning: {
        filled:
            "bg-warning-500 text-white border-0 shadow-[0_2px_4px_rgba(253,124,16,0.28)] hover:bg-warning-600 hover:shadow-[0_4px_10px_rgba(253,124,16,0.34)]",
        outlined:
            "bg-transparent text-warning-700 border border-warning-500 hover:bg-warning-50 hover:shadow-[0_2px_8px_rgba(253,124,16,0.15)]",
        ghost:
            "bg-transparent text-warning-700 border-0 hover:bg-transparent p-1",
    },
    info: {
        filled:
            "bg-info-500 text-white border-0 shadow-[0_2px_4px_rgba(98,114,240,0.28)] hover:bg-info-600 hover:shadow-[0_4px_10px_rgba(98,114,240,0.34)]",
        outlined:
            "bg-transparent text-info-600 border border-info-500 hover:bg-info-50 hover:shadow-[0_2px_8px_rgba(98,114,240,0.15)]",
        ghost:
            "bg-transparent text-info-600 border-0 hover:bg-transparent p-1",
    },
}

const sizeStyles: Record<Size, string> = {
    sm: "text-sm px-[14px] py-[6px] min-h-[32px]",
    md: "text-sm px-5 py-[9px] min-h-[40px]",
    lg: "text-[15px] px-7 py-3 min-h-[48px]",
}

const Spinner = ({ dark }: { dark?: boolean }) => (
    <span
        className={`inline-block w-3.75 h-3.75 rounded-full border-2 animate-spin shrink-0 ${dark
            ? "border-black/10 border-t-secondary-700"
            : "border-white/40 border-t-white"
            }`}
    />
);

const Button = ({
    children,
    variant = "primary",
    styleVariant = "filled",
    size = "md",
    disabled = false,
    loading = false,
    iconLeft,
    iconRight,
    onClick,
    type = "button",
    className = ""
}: ButtonProps) => {

    const btnRef = useRef<HTMLButtonElement>(null);

    const handleClick: React.MouseEventHandler<HTMLButtonElement> = (evt) => {
        const btn = btnRef.current;
        if (btn) {
            const circle = document.createElement("span")
            const diameter = Math.max(btn.offsetWidth, btn.offsetHeight)
            const rect = btn.getBoundingClientRect();
            circle.style.cssText = `
                position: absolute;
                border-radius: 50%;
                pointer-events: none;
                width: ${diameter}px;
                height: ${diameter}px;
                left: ${evt.clientX - rect.left - diameter / 2}px;
                top: ${evt.clientY - rect.top - diameter / 2}px;
                background: ${styleVariant === "filled" ? "rgba(255,255,255,0.28)" : "rgba(0,0,0,0.07)"};
                transform: scale(0);
                animation: ripple 0.55s linear forwards;
            `;
            btn.appendChild(circle);
            setTimeout(() => circle.remove(), 600);
        }
        onClick?.(evt);
    }

    const isSpinnerDark = styleVariant !== "filled"

    return (
        <button
            ref={btnRef}
            type={type}
            disabled={disabled || loading}
            onClick={handleClick}
            className={[
                "relative overflow-hidden inline-flex items-center justify-center gap-1.75",
                "font-medium tracking-[0.02em] rounded-md",
                "transition-all duration-200 cursor-pointer",
                "active:scale-[0.97]",
                "disabled:opacity-50 disabled:cursor-not-allowed disabled:active:scale-100 disabled:shadow-none",
                variantStyles[variant][styleVariant],
                styleVariant !== "ghost" && sizeStyles[size],
                className,
            ].join(' ')}
        >
            {
                loading ? (
                    <>
                        <Spinner dark={isSpinnerDark} />
                        {children}
                    </>
                ) :
                    (
                        <>
                            {iconLeft && <span className="flex items-center justify-center w-4 h-4 shrink-0">{iconLeft}</span>}
                            {children}
                            {iconRight && <span className="flex items-center justify-center w-4 h-4 shrink-0">{iconRight}</span>}
                        </>
                    )
            }
        </button>
    )
}

export default Button