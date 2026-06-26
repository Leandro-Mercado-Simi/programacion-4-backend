export type ProductCreate = {
  name: string;
  description?: string;
  base_price: number;
  images_url?: string[];
  stock: number;
  min_stock: number;
  available: boolean;
};

export type ProductUpdate = {
  name?: string;
  description?: string;
  base_price?: number;
  images_url?: string[];
  stock?: number;
  min_stock?: number;
  available?: boolean;
};

export type CategoryBasic = {
  id: number;
  name: string;
  description: string;
};

export type ProductRead = {
  id: number;
  name: string;
  description?: string;
  base_price: string;
  images_url?: string[];
  stock: number;
  min_stock: number;
  available: boolean;
  created_at: string;
  updated_at: string;
  deleted_at?: string | null;
};

export type ProductReadFull = ProductRead & {
  categories: CategoryBasic[];
};

export type PaginatedResponse<T> = {
  total: number;
  items: T[];
};
