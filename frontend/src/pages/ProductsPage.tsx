import Button from "../components/Button";
import { useFetch } from "../hooks/useFetch";
import type { ProductReadFull, PaginatedResponse } from "../features/products/types/product.types";

const ProductsPage = () => {
    const { data, loading } = useFetch<PaginatedResponse<ProductReadFull>>("/productos");

    return (
        <main className="max-w-7xl mx-auto px-4 py-8 flex flex-col gap-8">
            <div className="flex items-center justify-between">
                <h1 className="text-2xl font-bold text-text-primary">Productos</h1>
                <Button>+ Nuevo Producto</Button>
            </div>

            {loading ? (
                <div className="text-center py-12 text-text-secondary text-sm">
                    Cargando productos...
                </div>
            ) : (
                <div className="text-center py-12 text-text-secondary text-sm">
                    {data?.total ?? 0} productos encontrados
                </div>
            )}
        </main>
    );
};

export default ProductsPage;