export const ADD_PRODUCT = "ADD_PRODUCT";
export const REMOVE_PRODUCT = "REMOVE_PRODUCT";

export type Product = {
    id: number;
    name: string;
    price: number;
};

export type CartAction =
    | { type: typeof ADD_PRODUCT; payload: Product }
    | { type: typeof REMOVE_PRODUCT; payload: Product };