import { useCart } from "../../context/CartContext";
import "./SideCart.css"

export const SideCart = ({ open, onClose }) => {
    const { cart } = useCart();

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
                    <div className="cart-item">
                        <div className="remove-item">
                            <span>&times;</span>
                        </div>
                        <div className="item-img">
                            <img src="https://placehold.co/300x200" alt="Placeholder" />

                        </div>
                        <div className="item-details">
                            <p>Item name</p>
                            <strong>990</strong>
                            <div className="qty">
                                <span>-</span>
                                <strong>1</strong>
                                <span>+</span>
                            </div>
                        </div>

                    </div>
                    <ul>
                        {cart.map(item => (
                            <li key={item.id}>
                                {item.name} - ${item.price}
                            </li>
                        ))}
                    </ul>
                </div>
                {/* Cart Actions */}
                <div className="cart-actions">
                    <div className="subtotal">
                        <p>SUBTOTAL:</p>
                        <p>$<span id="subtotal-price">990</span></p>
                    </div>
                    <button>Checkout</button>

                </div>

            </div>
        </div >
    );
};

export default SideCart;