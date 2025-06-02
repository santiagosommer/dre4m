# From imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Local imports
from app.api.models.product_api_models import Product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
async def create_product_endpoint(product: Product):
    print(product)


@router.get("/list")
async def list_products():
    returning_products = [
        {
            "id": "1",
            "name": "ART 001 TSHIRT",
            "price": "990",
            "img": [
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/mock-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvbW9jay1iYWNrLnBuZyIsImlhdCI6MTc0ODYzMDEyOSwiZXhwIjoyMDYzOTkwMTI5fQ.-d_WU_2oUZybXK_aW-gt5Br2tDzYcZOaPeDlijOBCPM",
                    "alt": "mock-back"
                },
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/mock-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvbW9jay1mcm9udC5wbmciLCJpYXQiOjE3NDg2Mjg4OTAsImV4cCI6MjA2Mzk4ODg5MH0.ioH-uMyvumupSsg0oMNuqc88v0RL-RUIAd51jnN-J2w",
                    "alt": "mock-front"
                },
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-down.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtZG93bi5wbmciLCJpYXQiOjE3NDg2Mjg5MDgsImV4cCI6MjA2Mzk4ODkwOH0.n-QAFj2VVI8EGf_HrZsvKe2t0sc_VL_SDjAelq09dxw",
                    "alt": "perspective-down"
                },
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtZnJvbnQucG5nIiwiaWF0IjoxNzQ4NjI5MDkyLCJleHAiOjIwNjM5ODkwOTJ9.WZZke-gjeHQnVO0XgvL_gNtKLUw1m0zwCMoooDozsog",
                    "alt": "perspective-front"
                },
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-lying.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV85ZDRlNzM5ZS03ZDI5LTQxNGUtYWZkMC03NjA1YTdjNDZmOGUiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtbHlpbmcucG5nIiwiaWF0IjoxNzQ4ODgyMzQyLCJleHAiOjIwNjQyNDIzNDJ9.VcpoTMd81cfCJaRLxkOIC-Q9ga_1dmVrjsnpWunPT3w",
                    "alt": "perspective-lying"
                },
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-up.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtdXAucG5nIiwiaWF0IjoxNzQ4NjI5MTM5LCJleHAiOjIwNjM5ODkxMzl9.YXXSFNccuVrXiA7iBtGZL9IZCFR9xBifizD8mIhKuKY",
                    "alt": "perspective-up"
                },
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/real-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcmVhbC1iYWNrLnBuZyIsImlhdCI6MTc0ODYyOTE1NCwiZXhwIjoyMDYzOTg5MTU0fQ.KaMdOOEPJ1sPkdCNOvq-O7bhqg9byqkKk82mhg3mVZ8",
                    "alt": "real-back"
                },
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/real-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcmVhbC1mcm9udC5wbmciLCJpYXQiOjE3NDg2MjkxNjMsImV4cCI6MTc4MDE2NTE2M30.ZKergDrbdX7lyVIhsOtWH8HOEPKYymeoZK5pTbZanz0",
                    "alt": "real-front"
                },

            ],
            "stock": {
                "S": 0,
                "M": 1,
                "L": 3
            }
        },
        {
            "id": "2",
            "name": "BRUTAL 001 TSHIRT",
            "price": "990",
            "img": [
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/dre4m-back-shirt.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9kcmU0bS1iYWNrLXNoaXJ0LnBuZyIsImlhdCI6MTc0ODM2MDQwNywiZXhwIjoyMDYzNzIwNDA3fQ.bsBeGIB6AfwmON0kXWYC0PtSQr0DPpdQ9qbOPxHqRu0",
                    "alt": "Dre4m front mock"
                }
            ],
            "stock": {
                "S": 0,
                "M": 1,
                "L": 3
            }
        },
        {
            "id": "3",
            "name": "ASIA 001 TSHIRT",
            "price": "990",
            "img": [
                {
                    "url": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/koi-back-shirt.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9rb2ktYmFjay1zaGlydC5wbmciLCJpYXQiOjE3NDgzNjA0NzYsImV4cCI6MjA2MzcyMDQ3Nn0.X6mqm0JDFHLPcawDYm32ALpZ-_QU9mJzjJRsjfEG9fw",
                    "alt": "Koi front Mock"
                }
            ],
            "stock": {
                "S": 0,
                "M": 1,
                "L": 3
            }
        }
    ]
    return JSONResponse(content=returning_products)
