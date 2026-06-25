import DataTable from "../../../components/DataTable";
import Button from "../../../components/Button";
import type { CategoryReadFull } from "../types/category.types";
import type { SyntheticEvent } from "react";

interface CategoryListProps {
    categories: CategoryReadFull[];
    isLoading: boolean;
    onEdit: (category: CategoryReadFull) => void;
    onDelete: (id: number) => void;
    onRowClick: (category: CategoryReadFull) => void
}

const CategoryList = ({ categories, isLoading, onEdit, onDelete, onRowClick }: CategoryListProps) => {

    const columns = [
        {
            header: "N°",
            field: "id" as keyof CategoryReadFull,
        },
        {
            header: "Nombre",
            field: "name" as keyof CategoryReadFull,
        },
        {
            header: "Descripción",
            field: "description" as keyof CategoryReadFull,
        },
        {
            header: "Productos",
            field: "products" as keyof CategoryReadFull,
            render: (category: CategoryReadFull) => (
                <span>{category.products.length}</span>
            ),
        },
        {
            header: "Estado",
            field: "is_active" as keyof CategoryReadFull,
            render: (category: CategoryReadFull) => (
                <span className={`inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium ${category.is_active
                    ? "bg-success-50 text-success-600 border border-success-200"
                    : "bg-danger-50 text-danger-600 border border-danger-200"
                    }`}>
                    {category.is_active ? "Activa" : "Inactiva"}
                </span>
            ),
        },
        {
            header: "Acciones",
            field: "id" as keyof CategoryReadFull,
            render: (category: CategoryReadFull) => (
                <div className="flex justify-end gap-2">
                    <Button
                        size="md"
                        variant="info"
                        styleVariant="outlined"
                        onClick={() => onEdit(category)}
                    >
                        Editar
                    </Button>
                    <Button
                        size="md"
                        variant={`${category.is_active ? "danger" : "success"}`}
                        styleVariant="outlined"
                        onClick={(evt: SyntheticEvent) => {
                            evt.stopPropagation()
                            onDelete(category.id)
                        }}
                    >
                        {`${category.is_active ? "Desactivar" : "Reactivar"}`}
                    </Button>
                </div>
            ),
        },
    ];

    return (
        <DataTable
            columns={columns}
            data={categories}
            isLoading={isLoading}
            emptyMessage="No hay categorías registradas."
            onRowClick={onRowClick}
        />
    );
};

export default CategoryList;