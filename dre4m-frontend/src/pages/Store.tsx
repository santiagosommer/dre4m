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
                        <ProductCard name='ART 001' price={1800.00} />
                        <ProductCard name='ART 002' price={1800.00} />
                        <ProductCard name='ART 003' price={1800.00} />
                        <ProductCard name='ART 004' price={1800.00} />
                    </div>
                </div>
            </section>
        </>
    )
}

export default Store