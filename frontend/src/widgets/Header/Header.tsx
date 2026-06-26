import { NavLink } from "react-router-dom";

const Header = () => {
    return (
        <header className="bg-background-elevated border-b border-neutral-200 shadow-md sticky top-0 z-30">
            <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
                <div className="text-lg font-bold text-primary-500 hover:text-primary-600 transition-colors cursor-pointer">
                    Online-store
                </div>

                <nav className="flex items-center gap-6">
                    <NavLink
                        to="/categorias"
                        className={({ isActive }) =>
                            `text-sm font-medium transition-colors ${isActive
                                ? "text-primary-500 border-b-2 border-primary-500 pb-0.5"
                                : "text-text-secondary hover:text-text-primary"
                            }`
                        }
                    >
                        Categorías
                    </NavLink>
                    <NavLink
                        to="/productos"
                        className={({ isActive }) =>
                            `text-sm font-medium transition-colors ${isActive
                                ? "text-primary-500 border-b-2 border-primary-500 pb-0.5"
                                : "text-text-secondary hover:text-text-primary"
                            }`
                        }
                    >
                        Productos
                    </NavLink>
                </nav>
            </div>
        </header>
    );
};

export default Header;