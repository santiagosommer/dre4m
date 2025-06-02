import './ProductCard.css'

interface ProductCardProps {
    name: string;
    price: number;
    image: string;
}

export const ProductCard = ({ name, price, image }: ProductCardProps) => {
    return (
        <>
            <div className='cards-container'>
                <img src={image} alt="shirt-image" />
                <div className='card-text'>
                    <h3>{name}</h3>
                    <p>${price}</p>
                </div>
            </div>
        </>
    )
}

export default ProductCard