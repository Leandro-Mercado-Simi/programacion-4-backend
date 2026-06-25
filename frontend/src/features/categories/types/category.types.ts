export type CategoryCreate = {
  name: string;
  description: string;
  is_active: boolean;
};

export type CategoryUpdate = {
  name?: string;
  description?: string;
  is_active?: boolean;
};

export type CategoryRead = {
  id: number;
  name: string;
  description: string;
  is_active: boolean;
};

export type ProductBasic = {
  id: number;
  name: string;
  base_price: string;
  available: boolean;
};

export type CategoryReadFull = CategoryRead & {
  products: ProductBasic[];
};
