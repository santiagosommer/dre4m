import './Store.css'
import background from '../assets/shop_background.png'
import ProductCard from '../components/ProductCard/ProductCard'
import { useEffect, useState } from 'react'


export const Store = () => {
    const [products, setProducts] = useState([])

    const fetchProducts = async () => {
        try {
            const response = await fetch("https://localhost:8000/products/list", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: "include"
            })
            if (response.ok) {
                const data = await response.json()
                setProducts(data)
                console.log(data)
            }
        }
        catch (err) {

        }
    };

    useEffect(() => {
        fetchProducts()
    }, [])



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
                        {products.map((product) => (
                            <ProductCard name={product.name} price={product.price} />
                        ))}
                    </div>
                </div>
            </section>
        </>
    )
}

export default Store