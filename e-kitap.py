import os
import requests

os.chdir("C:/Users/username/Desktop")
os.makedirs("downloaded_pdfs", exist_ok=True)

pdf_url = "https://example.pdf"
response = requests.get(pdf_url)

if response.status_code == 200:
    pdf_path = os.path.join("downloaded_pdfs", "the_tell-tale_heart.pdf")
    with open(pdf_path, 'wb') as pdf_file:
        pdf_file.write(response.content)
    print("PDF başarıyla indirildi:", pdf_path)
else:
    print("PDF indirilemedi. Durum kodu:", response.status_code)
