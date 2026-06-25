interface SpinnerProps {
    message?: string;
}

const Spinner = ({ message }: SpinnerProps) => {
    return (
        <div className="lg p-3 m-3 inline-flex flex-col items-center gap-5">
            <div className="loader"></div>
            {
                message && (
                    <div className="text-md text-text-primary tracking-wide">
                        {message}
                    </div>
                )
            }
        </div>
    )
}

export default Spinner