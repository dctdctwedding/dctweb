import os
import copy
from bs4 import BeautifulSoup
import re  # 新增 re 模組

def try_read_file(file_path):
    encodings = ['utf-8', 'utf-8-sig', 'big5', 'gbk', 'latin1', 'cp950']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
                # Check if content is valid
                if any(ord(c) > 127 for c in content):
                    try:
                        content.encode(encoding)
                        return content
                    except UnicodeEncodeError:
                        continue
                return content
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Failed to read {file_path} with encodings: {encodings}")


def getSplitStr(str):
    if not str or not isinstance(str, str):
        return None
    try:
        if '：' in str:  # 检查行中是否包含冒号
            parts = str.split('：', 1)  # 使用冒号拆分字符串，最多拆分成两部分
            if len(parts) == 2:  # 确保成功拆分成两部分
                value_after_colon = parts[1].strip()
                if value_after_colon:
                    return value_after_colon
        return None
    except Exception as e:
        print(f"Error processing string: {str}, error: {e}")
        return None


def addli(soup, html, imgURL, description, title ):

    # for line in lines:
    #     li_element = soup.new_tag('li', class_='mb-4')
    #     li_element.string = line
    #     ul_element.append(li_element)

    # 创建一个新的<li>元素
    new_li_element = soup.new_tag('li', attrs={'class': 'col my-4 wrapper'})

    # 创建并添加<a>元素
    new_a_element = soup.new_tag(
        'a', attrs={'class': 'card card-gallery'}, href=html, target='_blank')

    # 创建并添加<div>元素
    new_div_element = soup.new_tag('div', attrs={'class': 'card-img-body'})

    # 创建并添加<img>元素
    new_img_element = soup.new_tag(
        'img', alt=description, attrs={'class': 'card-img card-img-top image'}, src=imgURL)

    # 创建并添加<div>元素
    new_imageBg_element = soup.new_tag('div', attrs={'class': 'imageBg'})

    # 创建并添加<div>元素
    new_middle_element = soup.new_tag('div', attrs={'class': 'middle'})

    # 创建并添加<div>元素
    new_middle_title_element = soup.new_tag('div', attrs={'class': 'middle-title'})
    new_middle_title_element.string = title

    # 创建并添加<a>元素
    new_middle_readmore_element = soup.new_tag(
        'a',  attrs={'class': 'middle-readmore'}, href=html, target='_blank')
    new_middle_readmore_element.string = 'Read more'

    # 将所有元素按正确的层次添加到<li>元素中
    new_li_element.append(new_a_element)
    new_a_element.append(new_div_element)
    new_div_element.append(new_img_element)
    new_div_element.append(new_imageBg_element)
    new_li_element.append(new_middle_element)
    new_middle_element.append(new_middle_title_element)
    new_middle_element.append(new_middle_readmore_element)

    # 找到现有的<ul>元素
    existing_ul_element = soup.find(
        'ul', class_='row row-cols-1 row-cols-md-2 row-cols-lg-3')

    # 将新的<li>元素插入到<ul>元素的第一个位置
    existing_ul_element.insert(0, new_li_element)


def addBImg(soup, folder_name, description, dist_src='assets/resized_photo/blog_2025-03-23/'):
    Bimg_item = soup.find(
        'div', class_='card-img-body work-card-img-body-main')

    new_img_element = soup.new_tag(
        'img', alt=description, attrs={'class': 'card-img card-img-top'}, src=dist_src+folder_name + '/首圖.jpg')
    Bimg_item.append(new_img_element)
    print(Bimg_item)


def addImg(soup, folder_name, img_src, description, dist_src='assets/resized_photo/blog_2025-03-23/'):
    water_fall_body = soup.find('div', class_='water-fall-body')
    new_water_fall_item = soup.new_tag(
        'div', attrs={'class': 'water-fall-item'})
    new_img_src = dist_src+folder_name+'/'+img_src
    new_img_element = soup.new_tag(
        'img', attrs={'class': 'card-img card-img-top'}, alt=description, src=new_img_src)
    new_water_fall_item.append(new_img_element)
    water_fall_body.append(new_water_fall_item)


def readHtml(templateFile):
    html_file_path = templateFile
    html_content = try_read_file(html_file_path)

    # 使用Beautiful Soup解析HTML 並複製一份
    soupTemplate = BeautifulSoup(html_content, 'html.parser')
    soup = copy.copy(soupTemplate)

    return soup


def get_venue_order():
    """場地排序順序"""
    return {
        "1956 Vintage": 1,
        "大院子日本海軍招待所": 2,
        "克里夫莊園": 3,
        "優聖美地": 4,
        "BY33": 5,  # 使用前綴匹配
        "BY33美軍俱樂部": 5,
        "CHALET V": 6,
        "La Villa": 7,
        "W Hotel": 8,
        "WILDWOOD": 9,
        "松園禪林": 10,
        "淡水將捷金鬱金香": 11,
        "瓶蓋工廠": 12,
        "美軍俱樂部": 13,
        "航空城靈糧堂": 14,
        "蔡瑞月": 15,
        "誠品行旅": 16,
        "顏氏牧場": 17,
        "香色": 18,
        "黛安莊園": 19,
        "SPOT光點": 20
    }

def folder_sort_key(folder_name):
    """自定義排序函數"""
    venue_order = get_venue_order()
    venue = folder_name.split('｜')[0].strip()
    
    # 尋找最佳匹配的場地名稱
    for key in venue_order:
        if venue.startswith(key):
            return (venue_order[key], venue)
    return (999, venue)

def natural_sort_key(s):
    """實現自然排序的key function"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def main(data_path, template, sort_method='natural'):
    soup = readHtml(template)
    # 使用自然排序取得資料夾列表
    folders = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
    
    print("\n=== 排序前（自然排序） ===")
    folders.sort(key=natural_sort_key)  # 先用自然排序
    for folder in folders:
        print(folder)
    
    print("\n=== 場地排序後 ===")
    # 再使用場地排序
    folders.sort(key=folder_sort_key)
    for folder in folders:
        venue = folder.split('｜')[0].strip()
        order = folder_sort_key(folder)[0]
        print(f"[{order}] {folder}")
    
    for folder_name in folders:
        print(f"Processing folder: {folder_name}")

        folder_path = os.path.join(data_path, folder_name)
        print(f"子文件夹: {folder_name}")
        
        # Parse folder name for title - it contains venue and event type
        parts = folder_name.split('｜')
        venue = parts[0].strip()
        
        # 針對 event_type 移除括號內容，但只用於顯示
        event_type = parts[1].strip() if len(parts) > 1 else ''
        display_event_type = re.sub(r'（.*?）', '', event_type)  # 移除括號內容供顯示使用
        
        html_name = 'portfolio_' + folder_name + '.html'  # 保持原始檔名
        imgURL = 'assets/resized_photo/blog_2025-03-23/' + folder_name + '/首圖.jpg'  # 保持原始檔名
        description = folder_name  # 保持原始檔名
        title = venue + '|' + display_event_type  # 只有標題移除括號內容
        
        print('-------------------------')
        print(html_name)
        print(imgURL) 
        print(description)
        print(title)
        addli(soup, html_name, imgURL, description, title)
        
    output_html_file = './output/portfolio_output.html'
    with open(output_html_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))


if __name__ == "__main__":
    data_path = './data/blog_2025-03-23'
    main(data_path, 'portfolio1.html')
