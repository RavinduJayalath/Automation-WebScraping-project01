import requests
from bs4 import BeautifulSoup
import csv

url = "https://perfumeclub.lk/shop/?product_cat=men"

response = requests.get(url)
                         
soup = BeautifulSoup(response.text, "html.parser") 
                             
products = soup.find_all("div", class_="etheme-product-grid-content")



with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Product Price",])

    for product in products:
        name = product.find("h2", class_="woocommerce-loop-product__title etheme-product-grid-title").text
        price = product.find("span", class_="woocommerce-Price-amount amount").text
        
        availability = ""
        description = ""

        link = product.find("h2", class_="woocommerce-loop-product__title etheme-product-grid-title").find("a")["href"]
        
        if link:
            product_response = requests.get(link)
            new_soup = BeautifulSoup(product_response.text, "html.parser")
            details = new_soup.find("div", class_="elementor-element elementor-element-d0801bf e-con-full e-flex e-con e-child")

            availability = details.find("div", class_="elementor-widget-container").text
            description = details.find("div", class_="elementor-element elementor-element-55ef2d2 elementor-widget elementor-widget-woocommerce-product-short-description").text


        writer.writerow([name, price, availability, description])

