import Button from "../../../components/Button";
import type { CategoryReadFull } from "../types/category.types";

interface CategoryCardProps {
    category: CategoryReadFull;
    onEdit: (category: CategoryReadFull) => void;
    onDelete: (id: number) => void;
    onClose: () => void
}

const CategoryCard = ({ category, onEdit, onDelete, onClose }: CategoryCardProps) => {
    return (
        <div className="flex flex-col bg-white rounded-lg shadow-md border border-neutral-200 overflow-hidden w-full max-w-sm">

            <div className="px-5 pt-5 pb-3 border-b border-neutral-100 flex items-start justify-between">
                <div>
                    <span className="text-xs font-medium text-text-secondary uppercase tracking-widest">
                        Categoría #{category.id}
                    </span>
                    <h3 className="text-lg font-semibold text-text-primary mt-1">
                        {category.name}
                    </h3>
                </div>
                <button
                    onClick={onClose}
                    className="p-1 rounded-md text-text-secondary hover:bg-neutral-100 transition-colors"
                >
                    ✕
                </button>
            </div>

            <div className="px-5 py-4 flex-1 flex flex-col gap-3">
                <p className="text-sm text-text-secondary">{category.description}</p>

                <div>
                    <span className="text-xs font-medium text-text-secondary uppercase tracking-wide">
                        Productos ({category.products.length})
                    </span>
                    {category.products.length > 0 ? (
                        <ul className="mt-1.5 flex flex-wrap gap-1.5">
                            {category.products.map((product) => (
                                <li
                                    key={product.id}
                                    className="text-xs bg-neutral-100 text-text-primary px-2 py-0.5 rounded-full"
                                >
                                    {product.name}
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p className="text-xs text-text-secondary mt-1">Sin productos asignados</p>
                    )}
                </div>
            </div>

            <div className="flex justify-end gap-2 px-5 py-3 border-t border-neutral-100">
                <Button
                    size="sm"
                    variant="info"
                    styleVariant="outlined"
                    onClick={() => onEdit(category)}
                >
                    Editar
                </Button>
                <Button
                    size="sm"
                    variant="danger"
                    styleVariant="outlined"
                    onClick={() => onDelete(category.id)}
                >
                    Eliminar
                </Button>
            </div>

        </div>
    );
};

export default CategoryCard;