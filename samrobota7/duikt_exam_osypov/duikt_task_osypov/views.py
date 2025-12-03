from django.http import HttpResponse
from django.shortcuts import render
from .models import cars_brand, cars_info

def install_demo(request):
    output = []

    brands_data = [
        {"BRAND_NAME": "Toyota", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 9},
        {"BRAND_NAME": "Ford", "BRAND_COUNTRY": "USA", "BRAND_RATING": 8},
        {"BRAND_NAME": "BMW", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9},
    ]

    cars_data = [
        {"CAR_NAME": "Corolla", "CAR_MODEL": "2023", "CAR_PRICE": 20000, "CAR_BRAND": "Toyota"},
        {"CAR_NAME": "Mustang", "CAR_MODEL": "2022", "CAR_PRICE": 35000, "CAR_BRAND": "Ford"},
        {"CAR_NAME": "X5", "CAR_MODEL": "2023", "CAR_PRICE": 60000, "CAR_BRAND": "BMW"},
    ]

    for b in brands_data:
        brand, created = cars_brand.objects.get_or_create(
            BRAND_NAME=b["BRAND_NAME"],
            defaults={
                "BRAND_COUNTRY": b["BRAND_COUNTRY"],
                "BRAND_RATING": b["BRAND_RATING"]
            },
        )
        if created:
            output.append(f"Додано бренд: {b['BRAND_NAME']}<br>")
        else:
            output.append(f"Пропуск (вже існує): {b['BRAND_NAME']}<br>")

    for c in cars_data:
        brand = cars_brand.objects.get(BRAND_NAME=c["CAR_BRAND"])
        car, created = cars_info.objects.get_or_create(
            CAR_NAME=c["CAR_NAME"],
            CAR_MODEL=c["CAR_MODEL"],
            defaults={
                "CAR_PRICE": c["CAR_PRICE"],
                "CAR_BRAND": brand
            }
        )
        if created:
            output.append(f"Додано авто: {c['CAR_NAME']}<br>")
        else:
            output.append(f"Пропуск (вже існує): {c['CAR_NAME']}<br>")

    return HttpResponse("".join(output))


def show_page(request):
    cars = cars_info.objects.all()
    return render(request, "template.html", {"cars": cars})

