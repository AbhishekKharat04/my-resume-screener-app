"""
utils/export_document.py
────────────────────────
Converts a Markdown string (like a Resume or Cover Letter) into a PDF.
"""

import io
import re
import markdown
from fpdf import FPDF

def _safe_text(text: str) -> str:
    """Convert fancy quotes/emojis to basic ascii so fpdf Helvetica doesn't crash."""
    if not text:
        return ""
    # Replace common unicode dashes and box drawing with hyphens
    text = re.sub(r'[—–━]', '-', text)
    # Drop non-latin characters (like emojis)
    return text.encode('latin-1', errors='ignore').decode('latin-1')

def generate_markdown_pdf(markdown_text: str, title: str = "Document") -> bytes:
    """
    Export a Markdown string to a beautifully styled PDF.
    """
    safe_md = _safe_text(markdown_text)
    html_content = markdown.markdown(safe_md)
    
    # Inject styling to match the user's custom template (blue headers, center title, etc.)
    html_content = html_content.replace("<h1>", "<h1 align=\"center\" style=\"color: #000000;\">")
    html_content = html_content.replace(
        "<h2>", 
        "<h2 style=\"color: #0047b3; font-family: Helvetica;\">"
    )
    html_content = html_content.replace("<li>", "<li style=\"margin-bottom: 4px;\">")
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=10)
    
    # We can inject a <style> block for some overarching styles like horizontal rules
    style_block = """
    <style>
        h1 { text-align: center; }
        h2 { color: #0047b3; }
        hr { color: #0047b3; }
        p { line-height: 1.4; }
    </style>
    """
    
    pdf.write_html(style_block + html_content)
    
    buf = io.BytesIO()
    pdf.output(buf)
    
    return buf.getvalue()
