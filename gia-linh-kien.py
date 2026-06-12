def calculate_average_price(prices):
    if not prices:
        return 0
    return sum(prices) / len(prices)

# Dữ liệu giá ổ cứng SSD Samsung và RAM DDR5
component_prices = [1500000, 1550000, 1600000, 1800000] 
print(f"Giá linh kiện trung bình: {calculate_average_price(component_prices)} VND")