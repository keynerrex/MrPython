from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import Paragraph

def create_pdf(file_path, content):
    # Configurar el tamaño de página
    page_width, page_height = letter

    # Crear el objeto Canvas
    c = canvas.Canvas(file_path, pagesize=letter)

    # Definir estilos de párrafo
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        'custom_style',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.black,
        leading=14,
        spaceAfter=10,
    )
    title_style = ParagraphStyle(
        'title_style',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.black,
        leading=24,
        spaceAfter=20,
    )
    subtitle_style = ParagraphStyle(
        'subtitle_style',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.darkblue,
        leading=18,
        spaceAfter=10,
    )

    # Dividir el contenido en líneas
    lines = content.split('\n')

    # Configurar la posición inicial del texto
    text_x = 50
    text_y = page_height - 50

    # Escribir cada línea en el PDF
    for line in lines:
        if line.startswith('---'):
            # Agregar título
            title = Paragraph(line.strip('-'), title_style)
            title.wrapOn(c, page_width, page_height)
            title.drawOn(c, text_x, text_y)
            text_y -= title.height + 10
        elif line.startswith('-----'):
            # Agregar subtítulo
            subtitle = Paragraph(line.strip('-'), subtitle_style)
            subtitle.wrapOn(c, page_width, page_height)
            subtitle.drawOn(c, text_x, text_y)
            text_y -= subtitle.height + 10
        else:
            # Agregar contenido
            paragraph = Paragraph(line, custom_style)
            paragraph.wrapOn(c, page_width, page_height)
            paragraph.drawOn(c, text_x, text_y)
            text_y -= paragraph.height

    # Guardar y cerrar el archivo PDF
    c.save()

# Ejemplo de uso
file_path = 'archivo.pdf'
content = """
RX 6600 -> $ 1.056.000 --> ESTIPULADO ( )
Ram 16gb -> $ 175.000 --> ESTIPULADO ( )
Fuente 550 watts -> $ 400.000 --> ESTIPULADO ( )
Board am4 -> $ 550.000 --> ESTIPULADO ( )
Gabinete -> $ 400.000 --> ESTIPULADO ( )
TOTAL -> $ 3.261.000 --> ESTIPULADO ( $3.500.000 )

(TENER EN CUENTA SI NO SUBE MUCHO, SINO EL PRESUPUESTO SUBIRIA MAS --> $ 3.800.000 O 4.000.000)

----- QUINCENA -----
ABRIL 15 -> $ 260.000 --> NN ------
ABRIL 30 -> $ 500.000 --> $ 400.000
MAYO 15 -> $ 500.000 --> $ 450.000 --- SOBRARON --- $ 130.000
MAYO 30 -> $ 500.000 --> $
JUNIO 15 -> $ 500.000 --> $
JUNIO 30 -> $ 500.000 --> $
JULIO 15 -> $ 500.000 --> $
JULIO 30 -> $ 500.000 --> $
AGOSTO 15 -> $ 500.000 --> $
AGOSTO 30 -> $ 500.000 --> $
SEPTIEMBRE 15 -> $ 500.000 --> $
SEPTIEMBRE 30 -> $ 500.000 --> $
OCTUBRE 10 -> $ 433.520 (PROMEDIO DE PAGO) 
----- FIN CONTRATO -----

--- TOTAL CALCULADO (DESDE ABRIRL 30) -> $5.783.520 ---

QUEDARIA TOTAL PRESUPUESTO (PROMEDIO DE SOBRA) -> $ 2.522.520 <---Quedaria(Promedio)
TOTAL CALCULADO SI SUBEN LOS PRECIOS -> $ 1.783.520 <---Quedaria(Promedio)
"""

create_pdf(file_path, content)
