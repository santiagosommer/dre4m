export const ADD_PRODUCT = "ADD_PRODUCT";
export const REMOVE_PRODUCT = "REMOVE_PRODUCT";
export const DECREASE_QUANTITY = "DECREASE_QUANTITY"

type img = {
    id: number,
    src: string;
    thumb: string;
    alt: string;
}

export type Product = {
    id: number;
    name: string;
    price: number;
    img: Array<img>;
    quantity: number;
    size: string;
};

export type CartAction =
    | { type: typeof ADD_PRODUCT; payload: Product }
    | { type: typeof REMOVE_PRODUCT; payload: Product }
    | { type: typeof DECREASE_QUANTITY; payload: Product };