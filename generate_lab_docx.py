"""
generate_lab_docx.py - Generates 13 separate, beautifully styled .docx files
for the Software Engineering & Web Development Lab Manual, specifically
tailored to the 'Ledgerly' Invoice & Quotation Generator project.
"""

import os
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

WORKSPACE = Path(r"C:\Users\Krushna\Documents\Projects\Invoice Generator")
OUTPUT_DIR = WORKSPACE / "Lab Manual Docs"
DIAGRAMS_DIR = WORKSPACE / "Project Diagrams"

OUTPUT_DIR.mkdir(exist_ok=True)

# Styling Helpers
PRIMARY_COLOR = RGBColor(0x1B, 0x4D, 0x4B)   # Deep Teal #1B4D4B
HEADER_BG = "1B4D4B"                          # Table header hex
ROW_ALT_BG = "F4F6F6"                         # Light table alt row
BORDER_COLOR = "D1D5DB"                       # Light gray border

def set_cell_background(cell, hex_color):
    """Sets background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets internal padding for a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for name, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{name}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def style_heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    run = h.runs[0]
    run.font.name = 'Calibri'
    if level == 1:
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = PRIMARY_COLOR
    elif level == 2:
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)
    elif level == 3:
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x34, 0x49, 0x5E)
    return h

def set_table_borders(table, color="000000", sz="8", val="single"):
    """Sets solid borders around a table and all its interior gridlines."""
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for b in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{b}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

def add_student_info_table(doc):
    """Adds the required Student & Faculty identification table at top of document."""
    info_data = [
        ("NAME", "Kimaya Teli\nAbhishek kumar Kairamkonda\nKrishna Somani"),
        ("ROLL NO", "24102C0079\n24102C0085\n24102C0067"),
        ("BRANCH", "CMPN"),
        ("DIV", "C"),
        ("SUBJECT", "WDL LAB"),
        ("FACULTY", "Dr. Ravindra Sangle")
    ]
    table = doc.add_table(rows=len(info_data), cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table, color="000000", sz="8")

    col_widths = [Inches(1.8), Inches(4.7)]
    for row_idx, (label, val) in enumerate(info_data):
        row = table.rows[row_idx]

        # Label Cell
        c0 = row.cells[0]
        c0.width = col_widths[0]
        set_cell_margins(c0, top=100, bottom=100, left=140, right=140)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        p0.paragraph_format.line_spacing = 1.15
        r0 = p0.add_run(label)
        r0.font.name = 'Calibri'
        r0.font.size = Pt(10.5)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # Value Cell
        c1 = row.cells[1]
        c1.width = col_widths[1]
        set_cell_margins(c1, top=100, bottom=100, left=140, right=140)
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        p1.paragraph_format.line_spacing = 1.15
        r1 = p1.add_run(val)
        r1.font.name = 'Calibri'
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    doc.add_paragraph() # spacer after info table

def add_header(doc, exp_num, title, module_num=None):
    """Adds the student header table and standard professional experiment title block."""
    add_student_info_table(doc)

    p_top = doc.add_paragraph()
    p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_top = p_top.add_run("SOFTWARE ENGINEERING & WEB DEVELOPMENT LAB MANUAL")
    r_top.font.name = 'Calibri'
    r_top.font.size = Pt(13)
    r_top.font.bold = True
    r_top.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_proj = p_proj.add_run("PROJECT CASE STUDY: LEDGERLY — INVOICE & QUOTATION GENERATOR PWA")
    r_proj.font.name = 'Calibri'
    r_proj.font.size = Pt(10)
    r_proj.font.italic = True
    r_proj.font.color.rgb = RGBColor(0x7F, 0x8C, 0x8D)

    h = style_heading(doc, f"Experiment No. {exp_num}: {title}", level=1)
    h.alignment = WD_ALIGN_PARAGRAPH.LEFT
    doc.add_paragraph() # spacer

def add_code_block(doc, code_str):
    """Adds a shaded monospace code box."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F8F9FA")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(code_str)
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x2A, 0x2A, 0x2A)
    doc.add_paragraph()

def add_styled_table(doc, headers, data):
    """Creates a clean, styled table with headers and alternate row background."""
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    # Style Header
    hdr_cells = table.rows[0].cells
    for i, header_text in enumerate(headers):
        cell = hdr_cells[i]
        set_cell_background(cell, HEADER_BG)
        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(header_text)
        run.font.name = 'Calibri'
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    # Style Rows
    for row_idx, row_data in enumerate(data):
        row_cells = table.rows[row_idx + 1].cells
        bg_col = ROW_ALT_BG if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, cell_value in enumerate(row_data):
            cell = row_cells[col_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(str(cell_value))
            run.font.name = 'Calibri'
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    doc.add_paragraph()
    return table

def add_image_if_exists(doc, img_name, caption=None, width=Inches(6.0)):
    """Inserts a diagram image with caption."""
    img_path = DIAGRAMS_DIR / img_name
    if img_path.exists():
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        doc.add_picture(str(img_path), width=width)
        if caption:
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_cap = p_cap.add_run(f"Figure: {caption}")
            r_cap.font.name = 'Calibri'
            r_cap.font.size = Pt(9)
            r_cap.font.italic = True
            r_cap.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
        doc.add_paragraph()

print("Setup completed. Building all 13 Experiment DOCX files...")
