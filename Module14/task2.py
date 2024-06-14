import re


def extract_image_links(html_text):
    pattern = r'<img\s+[^>]*src=["\'](https?://[^"\']+\.(?:jpg|jpeg|png|gif))["\']'

    image_links = re.findall(pattern, html_text, re.IGNORECASE)

    return image_links


sample_html = input("Введите HTML текст: ")

image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")
