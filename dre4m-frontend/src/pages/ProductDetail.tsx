import { useParams } from 'react-router-dom';
import { useCart } from '../context/CartContext';
import { Product } from '../types';

const PRODUCTS: Product[] = [
    { id: 1, name: 'Coffee', price: 300 },
    { id: 2, name: 'Tea', price: 250 },
];

export const ProductDetail = () => {
    const { id } = useParams();
    const product = PRODUCTS.find((p) => p.id === Number(id));
    const { addToCart } = useCart();

    if (!product) return <p>Producto no encontrado</p>;

    return (
        <div>
            <h1>{product.name}</h1>
            <p>Precio: ${product.price}</p>
            <button onClick={() => addToCart(product)}>Agregar al carrito</button>
        </div>
    );
};
