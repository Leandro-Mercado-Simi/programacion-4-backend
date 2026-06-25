import { useState } from 'react';
import type { CategoryReadFull, CategoryCreate } from '../features/categories/types/category.types';
import { useFetch } from '../hooks/useFetch';
import Header from '../widgets/Header/Header'
import { createCategory, deleteCategory, updateCategory } from '../features/categories/services/category.services';
import Button from '../components/Button';
import CategoryList from '../features/categories/components/CategoryList';
import CategoryCard from '../features/categories/components/CategoryCard';
import CategoryModal from '../features/categories/components/CategoryModal';

function App() {

  const { data: categories, loading, refetch } = useFetch<CategoryReadFull[]>("/categorias")

  const [isModalOpen, setIsModalOpen] = useState(false)
  const [selected, setSelected] = useState<CategoryReadFull | null>(null)
  const [selectedCard, setSelectedCard] = useState<CategoryReadFull | null>(null)

  const handleCreate = () => {
    setSelected(null)
    setIsModalOpen(true)
  }

  const handleEdit = (category: CategoryReadFull) => {
    setSelected(category)
    setIsModalOpen(true)
  }

  const handleDelete = async (id: number) => {
    await deleteCategory(id)
    if (selectedCard?.id === id) setSelectedCard(null)
    refetch()
  }

  const handleSubmit = async (data: CategoryCreate) => {
    if (selected) {
      await updateCategory(selected.id, data)
    } else {
      await createCategory(data)
    }

    setIsModalOpen(false)
    refetch()
  }

  const handleModalClose = () => {
    setIsModalOpen(false)
    setSelected(null)
  }

  return (
    <>
      <Header />
      <main className="max-w-7xl mx-auto px-4 py-8 flex flex-col gap-8">

        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-bold text-text-primary">Categorías</h1>
          <Button onClick={handleCreate}>
            + Añadir Categoría
          </Button>
        </div>

        <div className={`flex gap-6 ${selectedCard ? "items-start" : ""}`}>
          <div className="flex-1">
            <CategoryList
              categories={categories ?? []}
              isLoading={loading}
              onEdit={handleEdit}
              onDelete={handleDelete}
              onRowClick={setSelectedCard}
            />
          </div>

          {selectedCard && (
            <div className="w-80 shrink-0">
              <CategoryCard
                category={selectedCard}
                onEdit={handleEdit}
                onDelete={handleDelete}
                onClose={() => setSelectedCard(null)}
              />
            </div>
          )}
        </div>

      </main>

      <CategoryModal
        isOpen={isModalOpen}
        onClose={handleModalClose}
        onSubmit={handleSubmit}
        selected={selected}
      />
    </>
  );
}

export default App
