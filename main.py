import requests
import json
import pandas as pd

def fetch_data():
    url = "https://dummyjson.com/products"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        df = pd.read_excel("data.xlsx")

        print("Kết nối thành công!")
        # print("Tổng số sản phẩm:", len(data["products"]))
        # print("Sản phẩm đầu tiên:")
        # print(json.dumps(data["products"][0], indent=2, ensure_ascii=False))
        print(df)
        return data
    except requests.exceptions.RequestException as e:
        print("Lỗi khi kết nối API:", e)
        return None


if __name__ == "__main__":
    fetch_data()
