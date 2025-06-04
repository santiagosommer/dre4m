// context/CartContext.tsx
import { createContext, useReducer, useContext, ReactNode } from "react";
import { cartReducer } from "../reducers/CartReducer";
import {
    Product, ADD_PRODUCT,
    REMOVE_PRODUCT, DECREASE_QUANTITY,
    CartAction
} from "../types";
import SideCart from "../components/SideCart/SideCart";

type CartContextType = {
    cart: Product[];
    addToCart: (product: Product) => void;
    removeFromCart: (product: Product) => void;
    decreaseQuantity: (product: Product) => void;
};

const CartContext = createContext<CartContextType | undefined>(undefined);

export const CartProvider = ({ children }: { children: ReactNode }) => {
    const [cart, dispatch] = useReducer(cartReducer, [] as Product[]);

    const addToCart = (product: Product) => {
        let existing = cart.find(item => (item.id === product.id && item.size === product.size))
        if (existing) {
            dispatch({ type: ADD_PRODUCT, payload: { ...existing, quantity: existing.quantity + 1 } });
        } else {
            dispatch({ type: ADD_PRODUCT, payload: { ...product, quantity: 1 } });
        }
    };

    const removeFromCart = (product: Product) => {
        dispatch({ type: REMOVE_PRODUCT, payload: product });
    };

    const decreaseQuantity = (product: Product) => {
        dispatch({ type: DECREASE_QUANTITY, payload: product })
    }

    return (
        <CartContext.Provider value={{ cart, addToCart, removeFromCart, decreaseQuantity }}>
            {children}
            <SideCart />
        </CartContext.Provider>
    );
};

export const useCart = (): CartContextType => {
    const context = useContext(CartContext);
    if (!context) throw new Error("useCart must be used within a CartProvider");
    return context;
};

export default CartProvider