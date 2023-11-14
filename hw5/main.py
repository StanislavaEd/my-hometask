
def convert_womens_size(size, system):
    sizes = {
        "international": {
            "XS": "Extra Small",
            "S": "Small",
            "M": "Medium",
            "L": "Large",
            "XL": "Extra Large"
        },
        "ukraine": {
            "32": "XXS",
            "34": "XS",
            "36": "S",
            "38": "M",
            "40": "L",
            "42": "XL",
            "44": "XXL"
        },
        "germany": {
            "32": "XS",
            "34": "S",
            "36": "M",
            "38": "L",
            "40": "XL",
            "42": "XXL"
        },
        "italy": {
            "36": "XS",
            "38": "S",
            "40": "M",
            "42": "L",
            "44": "XL",
            "46": "XXL"
        }
    }

    if size in sizes["international"]:
        if system in sizes:
            return sizes[system].get(size, f"Розмір не знайдено {'international'}")
        else:
            return "Система розмірів не підтримується"
    else:
        return "Міжнародний розмір не знайдено"

print(convert_womens_size("M", "ukraine"))  # Виводить "M" в Україні
print(convert_womens_size("XL", "germany"))  # Виводить "XL" в Німеччині
print(convert_womens_size("XXS", "italy"))  # Виводить "Розмір не знайдено"
print(convert_womens_size("L", "france"))  # Виводить "Система розмірів не підтримується"

