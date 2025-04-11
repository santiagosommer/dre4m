import background from '../assets/waved_background.jpg'
import './Store.css'
import ProductCard from '../components/ProductCard/ProductCard'


export const Store = () => {
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
                        <ProductCard />
                        <ProductCard />
                        <ProductCard />
                        <ProductCard />
                    </div>
                </div>
            </section>
        </>
    )
}

export default Store