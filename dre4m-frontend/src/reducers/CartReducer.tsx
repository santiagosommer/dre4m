import { Product, CartAction, ADD_PRODUCT, REMOVE_PRODUCT, DECREASE_QUANTITY } from "../types";


export function cartReducer(state: Product[], action: CartAction): Product[] {

    switch (action.type) {
        case ADD_PRODUCT:
            let existing = state.find(
                (item) => item.id === action.payload.id && item.size === action.payload.size
            );
            if (existing) {
                console.log(state)
                return state.map((item) =>
                    item.id === action.payload.id && item.size === action.payload.size
                        ? { ...item, quantity: item.quantity + 1 }
                        : item
                );
            } else {
                return [...state, action.payload];
            }
        case REMOVE_PRODUCT:
            return state.filter((item) =>
                (item.id !== action.payload.id) || (item.id === action.payload.id) && (item.size !== action.payload.size)
            );
        case DECREASE_QUANTITY:
            let removeExisting = state.find(
                (item) => item.id === action.payload.id && item.size === action.payload.size
            );
            if (removeExisting && Number(action.payload.quantity) > 1) {
                return state.map((item) =>
                    item.id === action.payload.id && item.size === action.payload.size
                        ? { ...item, quantity: item.quantity - 1 }
                        : item
                )
            } else {
                return state.filter((item) =>
                    (item.id !== action.payload.id) || (item.id === action.payload.id) && (item.size !== action.payload.size)
                );
            }
        default:
            return state;
    }
}