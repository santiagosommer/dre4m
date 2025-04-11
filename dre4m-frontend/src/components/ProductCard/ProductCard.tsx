import './ProductCard.css'
import goya from '../../assets/goya-back-shirt.png'


export const ProductCard = () => {
    return (
        <>
            <div className='cards-container'>
                <img src={goya} alt="shirt-image" />
                <div className='card-text'>
                    <h3>ART 001 shirt</h3>
                    <p>$1,800.00</p></div>
            </div>
        </>
    )
}

export default ProductCard