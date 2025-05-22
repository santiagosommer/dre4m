import { Product, CartAction, ADD_PRODUCT, REMOVE_PRODUCT } from "../types";


export function cartReducer(state: Product[], action: CartAction): Product[] {

    switch (action.type) {
        case ADD_PRODUCT:
            return [...state, action.payload];
        case REMOVE_PRODUCT:
            return state.filter((item) => item.id !== action.payload.id);
        default:
            return state;
    }
}