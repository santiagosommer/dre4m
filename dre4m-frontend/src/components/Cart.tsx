import { useCart } from "../context/CartContext"

type Product = {
    id: number;
    name: string;
    price: number;
};

// In your CartContext (not shown here), make sure cart is typed as Product[]
// Example: const [cart, setCart] = useState<Product[]>([]);

export const Cart = () => {
    const { cart, addToCart, removeFromCart } = useCart();

    const product: Product = {
        id: 1,
        name: 'Coffee',
        price: 300,
    };

    return (
        <div>
            <div>Cart</div>
            <ul>
                {cart.map((product, index) => (
                    <li key={index}>{product.name} - ${product.price}</li>
                ))}
            </ul>
            <button onClick={() => addToCart(product)}>increment</button>
            <button onClick={() => removeFromCart(product)}>decrement</button>
        </div>
    )
}