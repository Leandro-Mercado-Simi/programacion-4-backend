import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Header from "../widgets/Header/Header";
import CategoriesPage from "../pages/CategoriesPage";
import ProductsPage from "../pages/ProductsPage";

const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/categorias" element={<CategoriesPage />} />
        <Route path="/productos" element={<ProductsPage />} />
        <Route path="*" element={<Navigate to="/categorias" replace />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;