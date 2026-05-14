import requests
import os
from tqdm import tqdm

def download_file():
    """دانلود فایل از لینک با نوار پیشرفت"""
    
    # گرفتن لینک از کاربر
    url = input("🔗 لینک فایل را وارد کنید: ")
    
    # ساخت پوشه downloads
    os.makedirs("downloads", exist_ok=True)
    
    # گرفتن نام فایل از لینک
    filename = url.split('/')[-1]
    filepath = os.path.join("downloads", filename)
    
    print(f"\n📥 شروع دانلود: {filename}")
    
    try:
        # درخواست دانلود
        response = requests.get(url, stream=True)
        response.raise_for_status()  # بررسی خطا
        
        # گرفتن حجم فایل
        total_size = int(response.headers.get('content-length', 0))
        
        # دانلود با نوار پیشرفت
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

# اجرای برنامه
if __name__ == "__main__":
    print("⚡ دانلودر حرفه‌ای")
    print("-" * 30)
    download_file()