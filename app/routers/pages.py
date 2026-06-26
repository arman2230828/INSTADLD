import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Ensures `app/templates` exists
os.makedirs("app/templates", exist_ok=True)
templates = Jinja2Templates(directory="app/templates")

def get_base_context(request: Request, title: str, description: str, current_path: str):
    return {
        "request": request,
        "title": f"{title} | InstaDL",
        "description": description,
        "current_path": current_path,
        "site_name": "InstaDL",
        "site_url": str(request.base_url).rstrip("/")
    }

@router.get("/")
async def home(request: Request):
    context = get_base_context(
        request, 
        "Instagram Reels Downloader", 
        "Download Instagram Reels quickly and securely in HD without watermarks.",
        "/"
    )
    return templates.TemplateResponse("index.html", context)

@router.get("/privacy-policy")
async def privacy(request: Request):
    context = get_base_context(
        request, 
        "Privacy Policy", 
        "Privacy Policy for InstaDL.",
        "/privacy-policy"
    )
    return templates.TemplateResponse("privacy.html", context)

@router.get("/terms")
async def terms(request: Request):
    context = get_base_context(
        request, 
        "Terms of Service", 
        "Terms of Service for InstaDL.",
        "/terms"
    )
    return templates.TemplateResponse("terms.html", context)

@router.get("/contact")
async def contact(request: Request):
    context = get_base_context(
        request, 
        "Contact Us", 
        "Get in touch with the InstaDL team.",
        "/contact"
    )
    return templates.TemplateResponse("contact.html", context)

@router.get("/dmca")
async def dmca(request: Request):
    context = get_base_context(
        request, 
        "DMCA", 
        "DMCA and Copyright Information for InstaDL.",
        "/dmca"
    )
    return templates.TemplateResponse("dmca.html", context)

@router.get("/about")
async def about(request: Request):
    context = get_base_context(
        request, 
        "About Us", 
        "Learn more about InstaDL.",
        "/about"
    )
    return templates.TemplateResponse("about.html", context)
