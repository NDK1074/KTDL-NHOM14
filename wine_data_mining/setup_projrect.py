import os
import urllib.request

# 1. Định nghĩa các thư mục cần tạo
project_name = "wine_data_mining"
folders = [
    f"{project_name}/data/raw",
    f"{project_name}/data/processed",
    f"{project_name}/notebooks",
    f"{project_name}/src",
    f"{project_name}/models"
]

# Tạo các thư mục
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"📁 Đã tạo thư mục: {folder}")

# 2. Tải tập dữ liệu Wine Quality (định dạng CSV phân cách bằng dấu chấm phẩy)
# Nguồn: UCI Machine Learning Repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
raw_file_path = f"{project_name}/data/raw/wine.csv"

print("⏳ Đang tải tập dữ liệu Wine CSV từ UCI...")
try:
    urllib.request.urlretrieve(url, raw_file_path)
    print(f"✅ Đã tải và lưu dữ liệu thô thành công tại: {raw_file_path}")
except Exception as e:
    print(f"❌ Có lỗi xảy ra khi tải dữ liệu: {e}")

# 3. Tạo file requirements.txt với các thư viện Data Mining phổ biến
requirements_path = f"{project_name}/requirements.txt"
with open(requirements_path, "w") as f:
    f.write("pandas\nnumpy\nscikit-learn\nmatplotlib\nseaborn\njupyter\n")
print(f"📄 Đã tạo file: {requirements_path}")

# 4. Tạo file README.md trống
readme_path = f"{project_name}/README.md"
with open(readme_path, "w") as f:
    f.write("# Dự án Khai Thác Dữ Liệu - Wine Dataset\n\nDự án này phân tích và khai phá tập dữ liệu Wine Quality.")
print(f"📄 Đã tạo file: {readme_path}")

print("\n🚀 HOÀN TẤT! Bạn có thể bắt đầu dự án tại thư mục 'wine_data_mining'.")