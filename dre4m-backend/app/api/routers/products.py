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
                    "id": "0",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/mock-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvbW9jay1iYWNrLnBuZyIsImlhdCI6MTc0ODYzMDEyOSwiZXhwIjoyMDYzOTkwMTI5fQ.-d_WU_2oUZybXK_aW-gt5Br2tDzYcZOaPeDlijOBCPM",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/mock-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvbW9jay1iYWNrLnBuZyIsImlhdCI6MTc0ODYzMDEyOSwiZXhwIjoyMDYzOTkwMTI5fQ.-d_WU_2oUZybXK_aW-gt5Br2tDzYcZOaPeDlijOBCPM",
                    "alt": "mock-back"
                },
                {
                    "id": "1",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/mock-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvbW9jay1mcm9udC5wbmciLCJpYXQiOjE3NDg2Mjg4OTAsImV4cCI6MjA2Mzk4ODg5MH0.ioH-uMyvumupSsg0oMNuqc88v0RL-RUIAd51jnN-J2w",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/mock-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvbW9jay1mcm9udC5wbmciLCJpYXQiOjE3NDg2Mjg4OTAsImV4cCI6MjA2Mzk4ODg5MH0.ioH-uMyvumupSsg0oMNuqc88v0RL-RUIAd51jnN-J2w",
                    "alt": "mock-front"
                },
                {
                    "id": "2",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-down.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtZG93bi5wbmciLCJpYXQiOjE3NDg2Mjg5MDgsImV4cCI6MjA2Mzk4ODkwOH0.n-QAFj2VVI8EGf_HrZsvKe2t0sc_VL_SDjAelq09dxw",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-down.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtZG93bi5wbmciLCJpYXQiOjE3NDg2Mjg5MDgsImV4cCI6MjA2Mzk4ODkwOH0.n-QAFj2VVI8EGf_HrZsvKe2t0sc_VL_SDjAelq09dxw",
                    "alt": "perspective-down"
                },
                {
                    "id": "3",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtZnJvbnQucG5nIiwiaWF0IjoxNzQ4NjI5MDkyLCJleHAiOjIwNjM5ODkwOTJ9.WZZke-gjeHQnVO0XgvL_gNtKLUw1m0zwCMoooDozsog",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtZnJvbnQucG5nIiwiaWF0IjoxNzQ4NjI5MDkyLCJleHAiOjIwNjM5ODkwOTJ9.WZZke-gjeHQnVO0XgvL_gNtKLUw1m0zwCMoooDozsog",
                    "alt": "perspective-front"
                },
                {
                    "id": "4",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-lying.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV85ZDRlNzM5ZS03ZDI5LTQxNGUtYWZkMC03NjA1YTdjNDZmOGUiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtbHlpbmcucG5nIiwiaWF0IjoxNzQ4ODgyMzQyLCJleHAiOjIwNjQyNDIzNDJ9.VcpoTMd81cfCJaRLxkOIC-Q9ga_1dmVrjsnpWunPT3w",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-lying.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV85ZDRlNzM5ZS03ZDI5LTQxNGUtYWZkMC03NjA1YTdjNDZmOGUiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtbHlpbmcucG5nIiwiaWF0IjoxNzQ4ODgyMzQyLCJleHAiOjIwNjQyNDIzNDJ9.VcpoTMd81cfCJaRLxkOIC-Q9ga_1dmVrjsnpWunPT3w",
                    "alt": "perspective-lying"
                },
                {
                    "id": "5",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-up.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV85ZDRlNzM5ZS03ZDI5LTQxNGUtYWZkMC03NjA1YTdjNDZmOGUiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtdXAucG5nIiwiaWF0IjoxNzQ4OTA0NDk5LCJleHAiOjIwNjQyNjQ0OTl9.w2tfxYzazJlL3YMqy2-jcMyzEwCbvaBD6PSKpAYCy5E",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/perspective-up.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV85ZDRlNzM5ZS03ZDI5LTQxNGUtYWZkMC03NjA1YTdjNDZmOGUiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcGVyc3BlY3RpdmUtdXAucG5nIiwiaWF0IjoxNzQ4OTA0NDk5LCJleHAiOjIwNjQyNjQ0OTl9.w2tfxYzazJlL3YMqy2-jcMyzEwCbvaBD6PSKpAYCy5E",
                    "alt": "perspective-up"
                },
                {
                    "id": "6",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/real-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcmVhbC1iYWNrLnBuZyIsImlhdCI6MTc0ODYyOTE1NCwiZXhwIjoyMDYzOTg5MTU0fQ.KaMdOOEPJ1sPkdCNOvq-O7bhqg9byqkKk82mhg3mVZ8",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/real-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcmVhbC1iYWNrLnBuZyIsImlhdCI6MTc0ODYyOTE1NCwiZXhwIjoyMDYzOTg5MTU0fQ.KaMdOOEPJ1sPkdCNOvq-O7bhqg9byqkKk82mhg3mVZ8",
                    "alt": "real-back"
                },
                {
                    "id": "7",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/real-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcmVhbC1mcm9udC5wbmciLCJpYXQiOjE3NDg2MjkxNjMsImV4cCI6MTc4MDE2NTE2M30.ZKergDrbdX7lyVIhsOtWH8HOEPKYymeoZK5pTbZanz0",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/art/goya/real-front.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXJ0L2dveWEvcmVhbC1mcm9udC5wbmciLCJpYXQiOjE3NDg2MjkxNjMsImV4cCI6MTc4MDE2NTE2M30.ZKergDrbdX7lyVIhsOtWH8HOEPKYymeoZK5pTbZanz0",
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
                    "id": "0",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/brutal/dre4m/white/mock-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYnJ1dGFsL2RyZTRtL3doaXRlL21vY2stYmFjay5wbmciLCJpYXQiOjE3NDg2Mjc3MjgsImV4cCI6MjA2Mzk4NzcyOH0.8MeEfJYCdngcl_gCLP-9m6ccFmvLmVmnBGxp9uugImg",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/brutal/dre4m/white/mock-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYnJ1dGFsL2RyZTRtL3doaXRlL21vY2stYmFjay5wbmciLCJpYXQiOjE3NDg2Mjc3MjgsImV4cCI6MjA2Mzk4NzcyOH0.8MeEfJYCdngcl_gCLP-9m6ccFmvLmVmnBGxp9uugImg",
                    "alt": "mock-back"
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
                    "id": "0",
                    "src": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/asia/koi/white/mock-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXNpYS9rb2kvd2hpdGUvbW9jay1iYWNrLnBuZyIsImlhdCI6MTc0ODYyOTIxOSwiZXhwIjoyMDYzOTg5MjE5fQ.foqWWmSqQaVSnkrhseT1w3iVYf3l_BRBSNCV4bg9PRI",
                    "thumb": "https://zkdwvxlhnamlrrtdgakp.supabase.co/storage/v1/object/sign/dre4m/shirts/asia/koi/white/mock-back.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzlkNGU3MzllLTdkMjktNDE0ZS1hZmQwLTc2MDVhN2M0NmY4ZSJ9.eyJ1cmwiOiJkcmU0bS9zaGlydHMvYXNpYS9rb2kvd2hpdGUvbW9jay1iYWNrLnBuZyIsImlhdCI6MTc0ODYyOTIxOSwiZXhwIjoyMDYzOTg5MjE5fQ.foqWWmSqQaVSnkrhseT1w3iVYf3l_BRBSNCV4bg9PRI",
                    "alt": "mock-back"
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
