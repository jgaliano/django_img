from django.shortcuts import render
from pdf2image import convert_from_path
import os

def convertir_pdf_a_imagen(request):
    poppler_path = r"C:\Users\jgali\Documents\Instaladores\poopler\poppler-0.68.0\bin"
    pdf_path = r"C:\Users\jgali\Downloads\Recibo Luz.pdf"
    saving_folder = r"C:\Users\jgali\Downloads\salida"

    try:
        pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

    try:
        c = 1
        image_urls = []
        for page in pages:
            img_name = f"img-{c}.jpeg"
            image_path = os.path.join(saving_folder, img_name)
            page.save(image_path, "JPEG")
            image_urls.append(image_path)
            c += 1
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

    return render(request, 'template.html', {'image_urls': image_urls})
