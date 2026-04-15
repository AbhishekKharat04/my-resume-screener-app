"""
utils/export_document.py
────────────────────────
Converts a Markdown string (Resume/Cover Letter) into a beautifully styled PDF.
"""

import io
import re
from fpdf import FPDF

def _clean(txt: str) -> str:
    """Sanitize text for FPDF Helvetica and strip markdown characters."""
    if not txt:
        return ""
    txt = txt.replace("—", "-").replace("━", "-").replace("–", "-")
    txt = txt.replace("*", "").replace("`", "")
    # Collapse 50+ repeating unbreakable characters (like dashes) to prevent 'Not enough horizontal space' FPDF crashes
    txt = re.sub(r'([-_=~+])\1{50,}', r'\1\1\1', txt)
    return txt.encode('latin-1', errors='ignore').decode('latin-1').strip()

def generate_markdown_pdf(markdown_text: str, title: str = "Document") -> bytes:
    """
    Parses structural Markdown into a highly styled, ATS-compliant PDF resume layout.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Brand colors and styling matches the user template
    blue = (0, 71, 179)
    black = (0, 0, 0)
    dark_gray = (60, 60, 60)
    
    lines = markdown_text.split("\n")
    
    for line in lines:
        raw_line = line.strip()
        if not raw_line:
            pdf.ln(2)
            continue
            
        # ── Title (Name) ──
        if raw_line.startswith("# "):
            pdf.set_font("Helvetica", "B", 22)
            pdf.set_text_color(*black)
            pdf.cell(0, 10, _clean(raw_line[2:]), ln=True, align="C")
            pdf.ln(1)
            
        # ── Section Headers ──
        elif raw_line.startswith("## "):
            pdf.ln(4)
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_text_color(*blue)
            header_str = _clean(raw_line[3:]).upper()
            pdf.cell(0, 6, header_str, ln=True, align="L")
            # Accent line
            pdf.set_draw_color(*blue)
            pdf.line(pdf.get_x(), pdf.get_y(), 200, pdf.get_y())
            pdf.ln(2)
            
        # ── Sub-headers (Job Titles, Degrees) ──
        elif raw_line.startswith("### "):
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(*black)
            pdf.cell(0, 6, _clean(raw_line[4:]), ln=True)
            
        # ── Bullet Points ──
        elif raw_line.startswith("* ") or raw_line.startswith("- "):
            content = raw_line[2:].strip()
            pdf.set_text_color(*black)
            pdf.set_font("Helvetica", "", 10)
            
            # Convert Markdown bold to HTML bold
            html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', _clean(content))
            # fpdf2 write_html supports <ul><li> natively
            pdf.write_html(f"<ul><li>{html_content}</li></ul>")
                
        # ── Standard text (Paragraphs, contact info, or italicized sub-lines) ──
        else:
            # Check for right-aligned date lines (Company | Location | Date)
            if "|" in raw_line and not raw_line.endswith(".") and len(raw_line) < 120:
                parts = [p.strip() for p in raw_line.split("|")]
                if len(parts) >= 2 and any(month in parts[-1] for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Present", "202"]):
                    # This is likely a subtitle line with a date on the right
                    pdf.set_font("Helvetica", "I", 10)
                    pdf.set_text_color(*dark_gray)
                    left_str = _clean(" | ".join(parts[:-1]))
                    right_str = _clean(parts[-1])
                    
                    pdf.cell(140, 5, left_str, ln=False)
                    pdf.cell(0, 5, right_str, ln=True, align="R")
                    continue
            
            # Normal paragraph or contact info
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(*black)
            
            # If it's a short line with pipes (like contact info at top), center it
            if "|" in raw_line and len(raw_line) < 130 and "github" not in raw_line.lower() and "linkedin" not in raw_line.lower() and not raw_line.endswith("."):
                pdf.cell(0, 5, _clean(raw_line), ln=True, align="C")
            elif ("github" in raw_line.lower() or "linkedin" in raw_line.lower()) and len(raw_line) < 130:
                html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', _clean(raw_line))
                pdf.write_html(f"<div align=\"center\">{html_content}</div>")
            else:
                # Regular paragraph block
                html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', _clean(raw_line))
                pdf.write_html(f"<p>{html_content}</p>")

    buf = io.BytesIO()
    pdf.output(buf)
    return buf.getvalue()
