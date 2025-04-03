import './StickyImages.css'
import dre4m from '../../assets/dre4m-back-shirt.png'
import koi from '../../assets/koi-back-shirt.png'
import goya from '../../assets/goya-back-shirt.png'



export const StickyImages = () => {
    return (
        <>

            <div className="sticky-container">
                <div className='image-wrapper1'>
                    <img className='sticky-image1' src={goya} />
                </div>
                <div className='section-wrapper'>
                    <p className='section-name'>NEW IN</p>
                    <div className='image-section-wrapper'>
                        <img className='flex-image' src={dre4m} />
                        <img className='flex-image' src={goya} />
                        <img className='flex-image' src={koi} />
                    </div>
                </div>
                <div className='image-wrapper2'>
                    <img className='sticky-image2' src={dre4m} />
                </div>
                <div className='image-wrapper3'>
                    <img className='sticky-image3' src={koi} />
                </div>
            </div>


        </>
    )
}

export default StickyImages
