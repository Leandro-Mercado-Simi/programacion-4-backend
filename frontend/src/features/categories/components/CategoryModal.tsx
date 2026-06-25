import Modal from "../../../components/Modal";
import CategoryForm from "./CategoryForm";
import type { CategoryReadFull, CategoryCreate } from "../types/category.types";

interface CategoryModalProps {
    isOpen: boolean;
    onClose: () => void;
    onSubmit: (data: CategoryCreate) => Promise<void>;
    selected: CategoryReadFull | null;
}

const CategoryModal = ({ isOpen, onClose, onSubmit, selected }: CategoryModalProps) => {
    return (
        <Modal
            isOpen={isOpen}
            onClose={onClose}
            title={selected ? "Editar Categoría" : "Nueva Categoría"}
            size="md"
        >
            <CategoryForm
                key={selected?.id ?? "new"}
                selected={selected}
                onSubmit={onSubmit}
                onCancel={onClose}
            />
        </Modal>
    );
};

export default CategoryModal;