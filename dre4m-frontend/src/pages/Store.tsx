import './Store.css'
import background from '../assets/shop_background.png'
import ProductCard from '../components/ProductCard/ProductCard'
import { Link } from 'react-router-dom'
import { useProducts } from "../context/ProductsContext"


export const Store = () => {
    const { products } = useProducts()

    return (
        <>
            <section className='container'>
                <div className='container-background'>
                    <img src={background} />
                </div>
                <div className='container-title'>
                    <p>SHOP</p>
                </div>
                <div className='container-products'>
                    <div className='container-products-cards'>
                        {products.map((products) => (
                            <Link
                                key={products.id}
                                to={`/product/${products.id}`}
                                style={{ textDecoration: "none", color: "inherit" }}
                            >
                                <ProductCard name={products.name} price={products.price} />
                            </Link>
                        ))}
                    </div>
                </div>
            </section>
        </>
    )
}

export default Store