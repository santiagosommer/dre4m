import './Store.css'
import ProductCard from '../components/ProductCard/ProductCard'
import { Link } from 'react-router-dom'
import { useProducts } from "../context/ProductsContext"

const background = 'https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shop_background.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaG9wX2JhY2tncm91bmQucG5nIiwiaWF0IjoxNzQ4MzU0ODQ3LCJleHAiOjIwNjM3MTQ4NDd9.vWb2T1a-z1Ght0VZUkC_Kq_5Oj47os0TiOWjKgPWdRY';

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
                                <ProductCard name={products.name} price={products.price} image={products.img} />
                            </Link>
                        ))}
                    </div>
                </div>
            </section>
        </>
    )
}

export default Store