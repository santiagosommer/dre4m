import background from '../assets/waved_background.jpg'
import './Store.css'
import shirt from '../assets/goya-back-shirt.png'

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
                        <div className='container-products-card'>
                            <img src={shirt} />
                        </div>
                        <div className='container-products-card'>
                            <img src={shirt} />
                        </div>
                        <div className='container-products-card'>
                            <img src={shirt} />
                        </div><div className='container-products-card'>
                            <img src={shirt} />
                        </div>
                        <div className='container-products-card'>
                            <img src={shirt} />
                        </div>
                        <div className='container-products-card'>
                            <img src={shirt} />
                        </div>
                    </div>
                </div>
            </section>
        </>
    )
}

export default Store