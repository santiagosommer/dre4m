import './ProductCard.css'
import goya from '../../assets/goya-back-shirt.png'


interface ProductCardProps {
    name: string;
    price: number;
}

export const ProductCard = ({ name, price }: ProductCardProps) => {
    return (
        <>
            <div className='cards-container'>
                <img src={goya} alt="shirt-image" />
                <div className='card-text'>
                    <h3>{name}</h3>
                    <p>${price}</p>
                </div>
            </div>
        </>
    )
}

export default ProductCard