#!/bin/bash

# 設定目標目錄
TARGET_DIR="/Users/howard/dctWedding/assets/resized_photo/blog_2025-03-23/松園禪林｜戶外證婚室內宴客"

# 切換到目標目錄
cd "$TARGET_DIR"

# 找出所有 .JPG 檔案並重命名
for file in *.JPG; do
    if [ -f "$file" ]; then
        # 取得不含副檔名的檔名
        filename=${file%.JPG}
        # 使用 git mv 重新命名
        git mv -f "$file" "${filename}.jpg"
        echo "Renamed: $file -> ${filename}.jpg"
    fi
done

echo "完成重命名作業"
