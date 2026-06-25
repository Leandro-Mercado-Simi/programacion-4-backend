import { useState } from "react";
import Input from "../../../components/Input";
import Button from "../../../components/Button";
import type { CategoryReadFull, CategoryCreate } from "../types/category.types";

interface CategoryFormProps {
    selected: CategoryReadFull | null;
    onSubmit: (data: CategoryCreate) => Promise<void>;
    onCancel: () => void;
}

const InitialData: CategoryCreate = {
    name: "",
    description: "",
    is_active: true,
};

const CategoryForm = ({ selected, onSubmit, onCancel }: CategoryFormProps) => {
    const [form, setForm] = useState<CategoryCreate>(
        selected
            ? { name: selected.name, description: selected.description, is_active: selected.is_active }
            : InitialData
    );
    const [loading, setLoading] = useState(false);

    const handleChange = (evt: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value, type } = evt.target;
        setForm((prev) => ({
            ...prev,
            [name]: type === "checkbox" ? (evt.target as HTMLInputElement).checked : value,
        }));
    };

    const handleSubmit = async () => {
        setLoading(true);
        try {
            await onSubmit(form);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex flex-col gap-4 w-full">
            <Input
                id="name"
                name="name"
                label="Nombre"
                type="text"
                value={form.name}
                onChange={handleChange}
            />
            <Input
                id="description"
                name="description"
                label="Descripción"
                type="text"
                value={form.description}
                onChange={handleChange}
            />
            <Input
                id="is_active"
                name="is_active"
                label="Activa"
                type="checkbox"
                value="is_active"
                checked={form.is_active}
                onChange={handleChange}
            />
            <div className="flex justify-end gap-2 pt-2">
                <Button variant="secondary" styleVariant="outlined" onClick={onCancel} disabled={loading}>
                    Cancelar
                </Button>
                <Button onClick={handleSubmit} loading={loading}>
                    Guardar
                </Button>
            </div>
        </div>
    );
};

export default CategoryForm;