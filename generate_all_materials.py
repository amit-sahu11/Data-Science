import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable, PageBreak, KeepTogether
)

SCRATCH_DIR = r"C:\Users\amitk\Desktop\Data Science"
ASSETS_DIR = os.path.join(SCRATCH_DIR, ".assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# -------------------------------------------------------------
# Chart 1: Progress Tracker Chart (Phase 1: 100%, Phase 2: 100%)
# -------------------------------------------------------------
def make_progress_chart():
    fig, ax = plt.subplots(figsize=(7, 2.5), dpi=200)
    phases = [
        "1. Python DS", 
        "2. NumPy", 
        "3. Pandas", 
        "4. EDA & Viz", 
        "5. Math & Stats", 
        "6. ML Scikit", 
        "7. Projects"
    ]
    progress = [100, 100, 0, 0, 0, 0, 0] # Phase 1 & 2 100% Complete!
    colors_list = ['#16a34a' if p == 100 else ('#2563eb' if p > 0 else '#cbd5e1') for p in progress]
    
    bars = ax.barh(phases[::-1], progress[::-1], color=colors_list[::-1], height=0.55, edgecolor='#1e293b', linewidth=0.8)
    ax.set_xlim(0, 110)
    ax.set_xlabel('Completion Percentage (%)', fontsize=9.5, fontweight='bold', color='#1e293b')
    ax.set_title('Master Curriculum Completion (Phases 1 & 2 Complete: 100%)', fontsize=11, fontweight='bold', color='#0f172a', pad=8)
    
    for bar in bars:
        w = bar.get_width()
        if w > 0:
            ax.text(w + 2, bar.get_y() + bar.get_height()/2, f'{int(w)}%', va='center', ha='left', fontsize=8.5, fontweight='bold', color='#1e293b')
            
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#94a3b8')
    ax.spines['bottom'].set_color('#94a3b8')
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    chart_path = os.path.join(ASSETS_DIR, "progress_chart.png")
    plt.savefig(chart_path, bbox_inches='tight')
    plt.close()
    return chart_path

# -------------------------------------------------------------
# Chart 2: Broadcasting Engine Diagram
# -------------------------------------------------------------
def make_broadcasting_diagram():
    fig, (ax1, ax_op, ax2, ax_eq, ax3) = plt.subplots(1, 5, figsize=(7.2, 2.2), dpi=200, gridspec_kw={'width_ratios': [3, 0.4, 3, 0.4, 3]})
    for ax in [ax1, ax_op, ax2, ax_eq, ax3]:
        ax.set_xlim(0, 3)
        ax.set_ylim(0, 3)
        ax.axis('off')
        
    ax1.set_title("Matrix A: (3, 3)", fontsize=8.5, fontweight='bold', color='#1e3a8a')
    for r in range(3):
        for c in range(3):
            ax1.add_patch(plt.Rectangle((c*0.9+0.1, (2-r)*0.9+0.1), 0.8, 0.8, facecolor='#dbeafe', edgecolor='#2563eb', lw=1.2))
    ax1.text(1.35, 1.35, "Raw Data\n(3 samples,\n3 features)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1e3a8a')
    
    ax_op.text(1.5, 1.35, "−", ha='center', va='center', fontsize=20, fontweight='bold', color='#dc2626')
    
    ax2.set_title("Vector B: (3,) -> (3, 3)", fontsize=8.5, fontweight='bold', color='#166534')
    for r in range(3):
        for c in range(3):
            face = '#dcfce7' if r == 0 else '#f0fdf4'
            ls = '-' if r == 0 else '--'
            ax2.add_patch(plt.Rectangle((c*0.9+0.1, (2-r)*0.9+0.1), 0.8, 0.8, facecolor=face, edgecolor='#16a34a', lw=1, linestyle=ls))
    ax2.text(1.35, 2.25, "Mean Vector", ha='center', va='center', fontsize=7, fontweight='bold', color='#14532d')
    ax2.text(1.35, 0.9, "Virtually\nBroadcasted\n(Stride = 0)", ha='center', va='center', fontsize=6.5, color='#15803d', style='italic')
    
    ax_eq.text(1.5, 1.35, "=", ha='center', va='center', fontsize=18, fontweight='bold', color='#475569')
    
    ax3.set_title("Result: (3, 3)", fontsize=8.5, fontweight='bold', color='#7c3aed')
    for r in range(3):
        for c in range(3):
            ax3.add_patch(plt.Rectangle((c*0.9+0.1, (2-r)*0.9+0.1), 0.8, 0.8, facecolor='#f3e8ff', edgecolor='#9333ea', lw=1.2))
    ax3.text(1.35, 1.35, "Normalized\n(Mean-Centered\nData)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#581c87')
    
    plt.tight_layout()
    chart_path = os.path.join(ASSETS_DIR, "broadcasting_diagram.png")
    plt.savefig(chart_path, bbox_inches='tight')
    plt.close()
    return chart_path

# -------------------------------------------------------------
# BUILD: Study_Progress_Tracker.pdf
# -------------------------------------------------------------
def build_progress_tracker():
    progress_chart = make_progress_chart()
    pdf_path = os.path.join(SCRATCH_DIR, "Study_Progress_Tracker.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor('#0f172a'))
    sub_style = ParagraphStyle('DocSub', fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#475569'))
    h2_style = ParagraphStyle('DocH2', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=colors.HexColor('#1d4ed8'), spaceBefore=8, spaceAfter=4)
    body_style = ParagraphStyle('DocBody', fontName='Helvetica', fontSize=8, leading=11.5, textColor=colors.HexColor('#1e293b'))
    
    elements = []
    
    # Title Banner
    elements.append(Paragraph("📊 Data Science Long-Term Learning Progress Tracker", title_style))
    elements.append(Paragraph("Student: <b>Amit</b> &nbsp;|&nbsp; Track: <b>Data Science & Practical Machine Learning</b> &nbsp;|&nbsp; Status: <b>Phase 1 & Phase 2 Mastered! 🏆</b>", sub_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563eb'), spaceBefore=4, spaceAfter=8))
    
    # Progress Chart
    if os.path.exists(progress_chart):
        elements.append(Image(progress_chart, width=480, height=170))
        elements.append(Spacer(1, 8))
        
    # Profile & Roadmap Summary Table
    elements.append(Paragraph("🗺️ Curriculum Roadmap Status", h2_style))
    roadmap_data = [
        ["Phase", "Topic Domain", "Problems Solved", "Status"],
        ["Phase 1", "Python Core & Memory Architecture", "12 / 12", "COMPLETED (100% Mastery) ✅"],
        ["Phase 2", "NumPy Vectorization & Dispersion", "12 / 12", "COMPLETED (100% Mastery) ✅"],
        ["Phase 3", "Pandas Data Manipulation & Wrangling", "0 / --", "READY TO COMMENCE (Next Topic) 🚀"],
        ["Phase 4", "EDA & Visualization (Seaborn/Matplotlib)", "0 / --", "Pending Phase 3"],
        ["Phase 5", "Applied Statistics & Probability", "0 / --", "Pending Phase 4"],
        ["Phase 6", "Classical ML (Scikit-Learn)", "0 / --", "Pending Phase 5"],
        ["Phase 7", "End-to-End Capstone Pipelines", "0 / --", "Pending Phase 6"]
    ]
    t1 = Table(roadmap_data, colWidths=[65, 195, 95, 175])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f8fafc'), colors.white]),
        ('TEXTCOLOR', (3,1), (3,2), colors.HexColor('#166534')),
        ('FONTNAME', (3,1), (3,2), 'Helvetica-Bold'),
        ('TEXTCOLOR', (3,3), (3,3), colors.HexColor('#1d4ed8')),
        ('FONTNAME', (3,3), (3,3), 'Helvetica-Bold'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    elements.append(t1)
    elements.append(Spacer(1, 8))
    
    # Practice Sets Log Table
    elements.append(Paragraph("📝 Practice Performance Log (24 / 24 Problems Mastered)", h2_style))
    sets_data = [
        ["Set #", "Topic Focus", "Problems", "Accuracy", "Archive Location"],
        ["Set 1.1", "Memory References, Slicing, Safe Dicts", "4 / 4", "100%", "practice_archive/Session_01/Set_01"],
        ["Set 1.2", "Pipelines, Lambdas, Sanitizers", "4 / 4", "100%", "practice_archive/Session_01/Set_02"],
        ["Set 1.3", "File I/O, CSV DictReader, JSON load", "4 / 4", "100%", "practice_archive/Session_01/Set_03"],
        ["Set 2.1", "NumPy Ndarray, SIMD, arange/linspace", "4 / 4", "100%", "practice_archive/Session_02/Set_01"],
        ["Set 2.2", "2D Slicing, Axis=0/1, Boolean Masking", "4 / 4", "100%", "practice_archive/Session_02/Set_02"],
        ["Set 2.3", "Z-Scores, Argmax, Reshape, Broadcasting", "4 / 4", "100%", "practice_archive/Session_02/Set_03"]
    ]
    t2 = Table(sets_data, colWidths=[55, 205, 60, 60, 150])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f766e')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f0fdfa'), colors.white]),
        ('TEXTCOLOR', (3,1), (3,-1), colors.HexColor('#166534')),
        ('FONTNAME', (3,1), (3,-1), 'Helvetica-Bold'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    elements.append(t2)
    elements.append(Spacer(1, 8))
    
    # Study Memory Highlights
    elements.append(Paragraph("🧠 Study Memory & Milestone Log", h2_style))
    mem_text = """<b>Session 1 (Python Core & Pipelines):</b> Mastered RAM pointers vs deep copies, half-open interval indexing, and safe file I/O with context managers.<br/>
<b>Session 2 (NumPy Foundations & 2D Slicing):</b> Mastered contiguous C-memory layout, SIMD vectorization, 2D matrix sub-box extraction, and the axis collapse mental model (<code>axis=0</code> vertical drop vs <code>axis=1</code> horizontal walk).<br/>
<b>Session 3 (NumPy Statistics & Broadcasting Engine):</b> Mastered Z-score anomaly detection, <code>np.argmax</code> across axes, reshaping memory layout with <code>-1</code> wildcard, and the NumPy broadcasting engine for feature mean-centering!"""
    elements.append(Paragraph(mem_text, body_style))
    
    doc.build(elements)
    print("Study_Progress_Tracker.pdf built successfully!")

# -------------------------------------------------------------
# BUILD: Data_Science_Study_Notes.pdf
# -------------------------------------------------------------
def build_detailed_study_notes():
    mem_img = os.path.join(ASSETS_DIR, "memory_diagram.png")
    slice_img = os.path.join(ASSETS_DIR, "slicing_diagram.png")
    np_img = os.path.join(ASSETS_DIR, "numpy_memory_diagram.png")
    axis_img = os.path.join(ASSETS_DIR, "axis_diagram.png")
    broad_img = make_broadcasting_diagram()
    
    pdf_path = os.path.join(SCRATCH_DIR, "Data_Science_Study_Notes.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor('#0f172a'))
    subtitle_style = ParagraphStyle('DocSub', fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#475569'))
    h2_style = ParagraphStyle('DocH2', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=colors.HexColor('#1d4ed8'), spaceBefore=8, spaceAfter=3)
    h3_style = ParagraphStyle('DocH3', fontName='Helvetica-Bold', fontSize=9, leading=12.5, textColor=colors.HexColor('#0f172a'), spaceBefore=5, spaceAfter=2)
    body_style = ParagraphStyle('DocBody', fontName='Helvetica', fontSize=8, leading=11.5, textColor=colors.HexColor('#1e293b'))
    code_style = ParagraphStyle('DocCode', fontName='Courier', fontSize=7.2, leading=10, textColor=colors.HexColor('#0f172a'), backColor=colors.HexColor('#f1f5f9'), borderPadding=4, spaceBefore=3, spaceAfter=4)
    callout_style = ParagraphStyle('DocCallout', fontName='Helvetica-Oblique', fontSize=7.8, leading=11, textColor=colors.HexColor('#854d0e'), backColor=colors.HexColor('#fef9c3'), borderPadding=4, spaceBefore=3, spaceAfter=4)

    elements = []
    
    # Header
    elements.append(Paragraph("📚 Data Science Master Study Notes & Architecture Reference", title_style))
    elements.append(Paragraph("Student: <b>Amit</b> &nbsp;|&nbsp; Target: <b>Data Science & Practical Programming</b> &nbsp;|&nbsp; Course Version: <b>Comprehensive Textbook Edition</b>", subtitle_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563eb'), spaceBefore=4, spaceAfter=6))
    
    # Module 1
    elements.append(Paragraph("1. Python Memory Model: Reference Aliasing vs Copying", h2_style))
    elements.append(Paragraph(
        "<b>The Fundamental Law:</b> Variables are reference labels (pointers). <code>b = a</code> does not allocate new RAM; both point to the same memory block (<code>id(a) == id(b)</code>). "
        "Mutating <code>b</code> silently alters <code>a</code>. Always use <code>b = a.copy()</code> to prevent corrupting raw datasets in Data Science.",
        body_style
    ))
    if os.path.exists(mem_img):
        elements.append(Image(mem_img, width=460, height=185))
    
    # Module 2
    elements.append(Paragraph("2. Sequence Slicing Mechanics & The Half-Open Interval Rule", h2_style))
    elements.append(Paragraph(
        "<b>Formula:</b> <code>sequence[start : stop : step]</code>. The interval is strictly <b>half-open</b>: <code>[start, stop)</code>. "
        "The <code>stop</code> index is exclusive. Total elements = <code>stop - start</code>.",
        body_style
    ))
    if os.path.exists(slice_img):
        elements.append(Image(slice_img, width=460, height=130))
        
    elements.append(PageBreak())
    
    # Module 3 & 4
    elements.append(Paragraph("3. Safe Data Extraction: Dictionary .get() for Messy Datasets", h2_style))
    code_3 = """customer = {"name": "Alice", "city": "Delhi"}
# Safe O(1) hash table lookup:
age = customer.get("age", 18)       # Missing -> fallback 18 without KeyError!
city = customer.get("city", "N/A")  # Exists  -> "Delhi" """
    elements.append(Paragraph(code_3.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
    
    elements.append(Paragraph("4. Vectorized Thinking: List Comprehensions", h2_style))
    code_4 = """prices = [120, 45, 300, 85, 520]
taxed_high_prices = [p * 1.10 for p in prices if p >= 100]  # [132.0, 330.0, 572.0]"""
    elements.append(Paragraph(code_4.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
    
    # Module 5 & 6
    elements.append(Paragraph("5. Custom Data Cleaning Pipelines & Lambda Expressions", h2_style))
    code_5 = """def clean_price(raw_val):
    if not isinstance(raw_val, str) or raw_val.strip().upper() in ["N/A", "MISSING", ""]:
        return 0.0
    return float(raw_val.replace("$", "").replace(",", "").strip())

mph_to_kmh = lambda mph: round(mph * 1.60934, 2)"""
    elements.append(Paragraph(code_5.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
    
    elements.append(Paragraph("6. File Ingestion (CSV/JSON): The with open(...) as f Architecture", h2_style))
    elements.append(Paragraph(
        "• <code>open('file.csv', 'r')</code>: Requests a live stream handle from Windows.<br/>"
        "• <code>as f</code>: Assigns the live file handle to variable <code>f</code>.<br/>"
        "• <code>with</code>: Context Manager that guarantees automatic <code>f.close()</code> exits.<br/>"
        "• <code>newline=''</code>: Prevents Windows carriage returns (<code>\\r\\n</code>) from injecting blank rows.<br/>"
        "• <code>csv.DictReader(f)</code>: Maps header rows to dictionary keys per line.<br/>"
        "• <code>json.load(f)</code>: Deserializes JSON feeds into native Python dicts and lists.",
        body_style
    ))
    
    elements.append(PageBreak())
    
    # Module 7: NumPy Foundations
    elements.append(Paragraph("7. Phase 2: Numerical Computing with NumPy (Ndarrays & Vectorization)", h2_style))
    if os.path.exists(np_img):
        elements.append(Image(np_img, width=460, height=170))
    elements.append(Paragraph(
        "NumPy stores numbers in a <b>contiguous block of raw C memory</b>, avoiding scattered pointer lookups. "
        "Every element must share the same <code>dtype</code>, enabling $O(1)$ address calculation: <code>Address(i) = Base + (i * 8)</code>.",
        body_style
    ))
    
    # Module 8: Multi-Dimensional Slicing & Axis Mechanics
    elements.append(Paragraph("8. 2D Slicing, Matrix Axes (axis=0/1) & Boolean Masking", h2_style))
    elements.append(Paragraph(
        "<b>Multi-Dimensional Slicing:</b> <code>matrix[row_slice, col_slice]</code><br/>"
        "<b>Axis Collapse Rule:</b> Specifying an axis tells NumPy which axis to <b>COLLAPSE</b>!<br/>"
        "• <code>axis=0</code>: Moves <b>vertically</b> down rows, collapsing rows into 1 summary per column.<br/>"
        "• <code>axis=1</code>: Moves <b>horizontally</b> across columns, collapsing columns into 1 summary per row.",
        body_style
    ))
    if os.path.exists(axis_img):
        elements.append(Image(axis_img, width=460, height=155))
        
    elements.append(PageBreak())

    # Module 9: Statistical Dispersion & Outlier Detection
    elements.append(Paragraph("9. Statistical Dispersion & Vectorized Anomaly Detection (Z-Scores)", h2_style))
    elements.append(Paragraph(
        "In Data Science and Machine Learning, central tendency (mean, median) only tells half the story. "
        "<b>Dispersion</b> describes how spread out the data points are around that center.<br/>"
        "• <b>Variance (σ²):</b> The average of squared deviations: <code>Var = Σ (x - μ)² / N</code>. Computed with <code>np.var(a)</code>.<br/>"
        "• <b>Standard Deviation (σ):</b> The square root of variance: <code>Std = √Var</code>. Computed with <code>np.std(a)</code>.<br/>"
        "• <b>The Z-Score Transformation:</b> Measures how many standard deviations a point is away from the mean:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Z = (X - μ) / σ</b><br/>"
        "Points with <code>|Z| > 2.0</code> (or <code>3.0</code>) are statistical outliers (e.g. server latency spikes or credit card fraud).",
        body_style
    ))
    code_9 = """latencies = np.array([24.5, 26.1, 25.0, 24.8, 120.5, 25.4, 25.2, 26.0])
mean_val = np.mean(latencies)
std_val = np.std(latencies)

# Vectorized Z-Score:
z_scores = (latencies - mean_val) / std_val

# Extract raw anomaly values using boolean masking:
outliers = latencies[z_scores > 2.0]  # array([120.5])"""
    elements.append(Paragraph(code_9.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

    # Module 10: Extrema Positioning & Reshaping Mechanics
    elements.append(Paragraph("10. Extrema Positioning (argmax/argmin) & Array Reshaping", h2_style))
    elements.append(Paragraph(
        "<b>10.1 Locating Positions with argmin & argmax:</b><br/>"
        "While <code>np.max()</code> returns the maximum value, <code>np.argmax()</code> returns the <b>integer index</b> where that maximum occurred. "
        "Combined with <code>axis=0</code> or <code>axis=1</code>, it answers vital business questions:<br/>"
        "• <code>np.argmax(sales, axis=1)</code>: Peak month for <i>each store</i> (row-wise collapse).<br/>"
        "• <code>np.argmax(sales, axis=0)</code>: Top performing store for <i>each month</i> (column-wise collapse).",
        body_style
    ))
    code_10_1 = """# Reshaping with the -1 Wildcard:
# Scikit-Learn strictly requires 2D matrices (samples, features).
arr = np.arange(10, 130, 10)         # 12 elements (1D)
grid = arr.reshape(3, 4)             # 2D matrix (3, 4)
grid_t = grid.T                      # Transpose -> shape (4, 3)

first_col = grid_t[:, 0]             # 1D array of 4 items: [10, 20, 30, 40]
col_vector = first_col.reshape(-1, 1) # 2D column vector of shape (4, 1)"""
    elements.append(Paragraph(code_10_1.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

    elements.append(PageBreak())

    # Module 11: The Vectorized Broadcasting Engine
    elements.append(Paragraph("11. The NumPy Broadcasting Engine & Data Normalization", h2_style))
    elements.append(Paragraph(
        "Broadcasting is NumPy's superpower. It allows arithmetic operations between arrays of <b>different shapes</b> "
        "without copying data in RAM. It creates <b>virtual dimensions</b> by setting the memory stride along that axis to <b>0</b>.<br/>"
        "<b>The Two Golden Rules of Broadcasting:</b><br/>"
        "NumPy compares array shapes from <b>right to left</b> (trailing dimensions first):<br/>"
        "1. Two dimensions are compatible if they are <b>equal</b>, OR<br/>"
        "2. One of the dimensions is <b>1</b> (or missing, which gets prepended as 1).",
        body_style
    ))
    if os.path.exists(broad_img):
        elements.append(Image(broad_img, width=460, height=140))
        
    elements.append(Paragraph(
        "<b>Practical Machine Learning Application: Feature Mean-Centering</b><br/>"
        "Subtracting the feature means ensures all features have zero mean, speeding up gradient descent:",
        body_style
    ))
    code_11 = """houses = np.array([
    [18.0, 3.0, 15.0],   # [Area, Bedrooms, Age]
    [24.0, 4.0,  5.0],
    [12.0, 2.0, 25.0]
])

# 1. Feature means across all rows (collapses axis 0 -> shape (3,)):
feature_means = houses.mean(axis=0)  # [18.0, 3.0, 15.0]

# 2. Vectorized Broadcasting: (3, 3) - (3,) -> NumPy stretches across rows!
normalized_houses = houses - feature_means

# 3. Verification:
print(normalized_houses.mean(axis=0)) # [0.0, 0.0, 0.0]"""
    elements.append(Paragraph(code_11.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
    
    doc.build(elements)
    print("Data_Science_Study_Notes.pdf built successfully!")

if __name__ == '__main__':
    build_progress_tracker()
    build_detailed_study_notes()
