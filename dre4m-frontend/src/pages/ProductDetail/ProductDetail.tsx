import { Link, useParams } from "react-router-dom";
import { useCart } from "../../context/CartContext";
import { useProducts } from "../../context/ProductsContext"
import "./ProductDetail.css"
import { useEffect, useState } from "react";
import ProductCard from "../../components/ProductCard/ProductCard";
import { Gallery } from "../../components/Gallery/Gallery";

const SIZE_GUIDE = "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/SIZE_GUIDE_STANDARD_TEE_FW.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9TSVpFX0dVSURFX1NUQU5EQVJEX1RFRV9GVy5wbmciLCJpYXQiOjE3NDgzNjYxMzEsImV4cCI6MjA2MzcyNjEzMX0.9vlgSYOKST05PGAt-hcoo4L3XEoyTHqzSCSmrZVM1so"

export const ProductDetail = () => {
    const { id } = useParams();
    const { products } = useProducts();
    const product = products.find((p) => Number(p.id) === Number(id));
    if (!product) return <p>Producto no encontrado</p>;
    const photos = [];
    product.img.forEach(image => {
        photos.push({ id: image.id, src: image.src, thumb: image.thumb, alt: image.alt });
    });
    const { addToCart } = useCart();
    const [selectedSize, setSelectedSize] = useState("");
    const recommended = products
        .filter(p => p.id !== product.id)
        .slice(0, 2);


    useEffect(() => {
        setSelectedSize("");
    }, [id]);

    return (
        <div className="detail-container">
            <section className="detail-products-container">
                <Gallery images={photos} />


                <div className="detail-info">
                    <h1>{product.name}</h1>
                    <p>Precio: <strong>${product.price},00</strong></p>
                    <label htmlFor="size">Talla:</label>

                    <select
                        className="size"
                        value={selectedSize}
                        onChange={e => setSelectedSize(e.target.value)}
                    >
                        <option value="" disabled>Choose an option</option>
                        <option value="S">S</option>
                        <option value="M">M</option>
                        <option value="L">L</option>
                    </select>
                    {selectedSize && <p>Disponibilidad: {product.stock[selectedSize]}</p>}
                    <button
                        className="add-btn"
                        onClick={() => addToCart(product)}
                        disabled={!selectedSize || product.stock[selectedSize] <= 0}
                    >
                        Add to cart
                    </button>
                    <img src={SIZE_GUIDE} draggable="false" className="size-guide" />
                </div>
            </section >
            <section className="recommended-products">
                {recommended.map((prod) => (
                    <Link
                        key={prod.id}
                        to={`/product/${prod.id}`}
                        style={{ textDecoration: "none", color: "inherit" }}
                    >
                        <ProductCard name={prod.name} price={prod.price} image={prod.img[0].src} />
                    </Link>
                ))}
            </section>
        </div>
    );
};
