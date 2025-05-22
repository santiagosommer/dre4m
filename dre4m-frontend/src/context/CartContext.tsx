// context/CartContext.tsx
import { createContext, useReducer, useContext, ReactNode } from "react";
import { cartReducer } from "../reducers/CartReducer";
import { Product, ADD_PRODUCT, REMOVE_PRODUCT, CartAction } from "../types";

type CartContextType = {
    cart: Product[];
    addToCart: (product: Product) => void;
    removeFromCart: (product: Product) => void;
};

const CartContext = createContext<CartContextType | undefined>(undefined);

export const CartProvider = ({ children }: { children: ReactNode }) => {
    const [cart, dispatch] = useReducer(cartReducer, [] as Product[]);

    const addToCart = (product: Product) => {
        dispatch({ type: ADD_PRODUCT, payload: product });
    };

    const removeFromCart = (product: Product) => {
        dispatch({ type: REMOVE_PRODUCT, payload: product });
    };

    return (
        <CartContext.Provider value={{ cart, addToCart, removeFromCart }}>
            {children}
        </CartContext.Provider>
    );
};

export const useCart = (): CartContextType => {
    const context = useContext(CartContext);
    if (!context) throw new Error("useCart must be used within a CartProvider");
    return context;
};

export default CartProvider