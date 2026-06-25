const Header = () => {
    return (
        <>
            <header className="bg-background-elevated border-b border-neutral-200 shadow-md sticky top-0 z-30">
                <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
                    <div
                        className="text-lg font-bold text-primary-500 hover:text-primary-600 transition-colors cursor-pointer"
                    >
                        Online-store
                    </div>
                </div>
            </header>
        </>
    )
}

export default Header