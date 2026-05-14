import requests
import os
from tqdm import tqdm
from urllib.parse import urlparse, unquote

def clean_filename(filename):
    """پاک کردن کاراکترهای غیرمجاز از اسم فایل"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def get_filename_from_url(url):
    """استخراج اسم فایل از لینک"""
    # جدا کردن قسمت مسیر از لینک
    parsed = urlparse(url)
    path = unquote(parsed.path)
    
    # گرفتن آخرین قسمت مسیر
    filename = os.path.basename(path)
    
    # اگر اسم فایل خالی بود یا پسوند نداشت
    if not filename or '.' not in filename:
        filename = "downloaded_file"
    
    return clean_filename(filename)

def download_file():
    """دانلود فایل از لینک با نوار پیشرفت"""
    
    url = input("🔗 لینک فایل را وارد کنید: ")
    
    os.makedirs("downloads", exist_ok=True)
    
    # گرفتن اسم فایل مناسب
    filename = get_filename_from_url(url)
    filepath = os.path.join("downloads", filename)
    
    print(f"\n📥 شروع دانلود: {filename}")
    
    try:
        # اضافه کردن هدرهای مناسب برای pixeldrain
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, stream=True, headers=headers)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filepath, 'wb') as f:
            with tqdm(total=total_size, unit='B', unit_scale=True, desc="پیشرفت") as pbar:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    pbar.update(len(chunk))
        
        print(f"\n✅ دانلود کامل شد: {filepath}")
        print(f"📂 فایل در پوشه 'downloads' ذخیره شد")
        
    except Exception as e:
        print(f"\n❌ خطا: {e}")
        print("لطفاً لینک را بررسی کنید")

if __name__ == "__main__":
    print("⚡ دانلودر حرفه‌ای")
    print("-" * 30)
    download_file()
