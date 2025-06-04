import { useState, useEffect } from "react";
import { useCart } from "../../context/CartContext";
import "./SideCart.css"

export const SideCart = ({ open, onClose }) => {
    const { cart, addToCart, removeFromCart, decreaseQuantity } = useCart();
    const [itemQty, setItemQty] = useState(1);
    const [subtotal, setSubtotal] = useState(0);

    const calculateSubtotal = () => {
        return cart.reduce((acc, item) => {
            return acc + Number(item.price)
        }, 0)
    }

    useEffect(() => {
        setSubtotal(
            cart.reduce((acc, item) => acc + (Number(item.price) * Number(item.quantity)), 0)
        );
    }, [cart]);

    const increaseQty = (item) => {
        addToCart(item)
    };

    const removeItem = (item) => {
        removeFromCart(item)
    }


    const decreaseQty = (item) => {
        decreaseQuantity(item)
    }

    return (
        <div className={`cart${open ? " open" : ""}`}>
            <div className="cart-content">
                {/* Cart Header */}
                <div className="cart-header">
                    <div className="cart-header-title">
                        <h1>Cart</h1>
                    </div>
                    <span className="close-btn" onClick={onClose}>&times;</span>
                </div>
                {/* Cart Items */}
                <div className="cart-items">
                    {cart.map(item => (
                        <div className="cart-item">
                            <div className="remove-item">
                                <span onClick={() => removeItem(item)}>&times;</span>
                            </div>
                            <div className="item-img">
                                <img src={item.img[0].src} alt="Placeholder" />
                            </div>
                            <div className="item-details">
                                <p>{item.name}</p>
                                <p>{item.size}</p>
                                <strong>{item.price},00</strong>
                                <div className="qty">
                                    <span onClick={() => decreaseQty(item)}>-</span>
                                    <strong>{item.quantity}</strong>
                                    <span onClick={() => increaseQty(item)}>+</span>
                                </div>
                            </div>
                        </div>

                    ))}

                </div>
                {/* Cart Actions */}
                <div className="cart-actions">
                    <div className="subtotal">
                        <p>SUBTOTAL:</p>
                        <p>$<span id="subtotal-price">{subtotal}</span></p>
                    </div>
                    <button>Checkout</button>

                </div>

            </div>
        </div >
    );
};

export default SideCart;

function useEFfect(arg0: () => void) {
    throw new Error("Function not implemented.");
}
