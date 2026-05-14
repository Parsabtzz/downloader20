import os
import zipfile
import math

def split_file_into_parts(file_path, output_dir, part_size_mb=90):
    """
    تقسیم فایل به قطعات ۹۰ مگابایتی
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_size = os.path.getsize(file_path)
    part_size = part_size_mb * 1024 * 1024  # تبدیل به بایت
    num_parts = math.ceil(file_size / part_size)
    
    print(f"تقسیم فایل {file_path} به {num_parts} بخش")
    
    with open(file_path, 'rb') as f:
        for i in range(num_parts):
            part_file = os.path.join(output_dir, f"part_{i+1:03d}.zip")
            chunk = f.read(part_size)
            with open(part_file, 'wb') as part_f:
                part_f.write(chunk)
            print(f"بخش {i+1} از {num_parts} ایجاد شد: {part_file}")
    
    return num_parts

# استفاده
if __name__ == "__main__":
    file_to_split = input("مسیر فایل برای تقسیم: ")
    split_file_into_parts(file_to_split, "split_parts")