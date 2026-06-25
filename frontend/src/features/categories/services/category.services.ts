import { apiFetch } from "../../../lib/api";
import type {
  CategoryCreate,
  CategoryUpdate,
  CategoryReadFull,
} from "../types/category.types";

const ENDPOINT = "/categorias";

export const getAllCategories = async (): Promise<CategoryReadFull[]> => {
  return apiFetch<CategoryReadFull[]>(ENDPOINT);
};

export const getCategoryById = async (id: number): Promise<CategoryReadFull> => {
  return apiFetch<CategoryReadFull>(`${ENDPOINT}/${id}`);
};

export const createCategory = async (data: CategoryCreate): Promise<CategoryReadFull> => {
  return apiFetch<CategoryReadFull>(ENDPOINT, {
    method: "POST",
    body: data,
  });
};

export const replaceCategory = async (
  id: number,
  data: CategoryCreate,
): Promise<CategoryReadFull> => {
  return apiFetch<CategoryReadFull>(`${ENDPOINT}/${id}`, {
    method: "PUT",
    body: data,
  });
};

export const updateCategory = async (
  id: number,
  data: CategoryUpdate,
): Promise<CategoryReadFull> => {
  return apiFetch<CategoryReadFull>(`${ENDPOINT}/${id}`, {
    method: "PATCH",
    body: data,
  });
};

export const deleteCategory = async (id: number): Promise<void> => {
  return apiFetch<void>(`${ENDPOINT}/${id}/desactivar`, {
    method: "PATCH",
  });
};
