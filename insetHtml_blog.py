import os
import copy
import shutil
from bs4 import BeautifulSoup

def addOg(soup, url, description, site_name, title):
    meta_elements = [
        soup.new_tag('meta', property='og:url',
                     content=url),
        soup.new_tag('meta', property='og:description',
                     content=description),
        soup.new_tag('meta', property='og:site_name', content=site_name),
        soup.new_tag('meta', property='og:title', content=title),
    ]

    return meta_elements

def addMetaName(soup, name, content):
    # 创建并添加新的<meta>元素
    new_meta = soup.new_tag('meta')
    new_meta['name'] = name
    new_meta['content'] = content

    return new_meta

def getSplitStr(str):
    if '：' in str:  # 检查行中是否包含冒号
        parts = str.split('：', 1)  # 使用冒号拆分字符串，最多拆分成两部分
        if len(parts) == 2:  # 确保成功拆分成两部分
            value_after_colon = parts[1].strip()
            return value_after_colon

def addH1(soup, title):
    # 修改<h1>元素的文本
    new_h1_text = title
    h1_element = soup.find('h1', class_='lead text-center my-5')
    h1_element.string = new_h1_text

def addli(soup, lines):
    ul_element = soup.find('ul', class_='text-center mb-5')
    # 清空現有的列表內容
    ul_element.clear()
    
    for line in lines:
        li_element = soup.new_tag('li', class_='mb-4')
        li_element.string = line
        ul_element.append(li_element)

def addBImg(soup, folder_name, description, dist_src='assets/resized_photo/blog_2025-03-23/'):
    Bimg_item = soup.find('div', class_='card-img-body work-card-img-body-main')
    
    new_img_element = soup.new_tag(
        'img', alt=description, attrs={'class': 'card-img card-img-top'}, src= dist_src+folder_name + '/首圖.jpg')
    Bimg_item.append(new_img_element)
    print(Bimg_item)

def addImg(soup, folder_name, img_src, description, dist_src='assets/resized_photo/blog_2025-03-23/'):
    water_fall_body = soup.find('div', class_='water-fall-body')
    new_water_fall_item = soup.new_tag('div', attrs={'class': 'water-fall-item'} )
    new_img_src = dist_src+folder_name+'/'+img_src
    new_img_element = soup.new_tag('img', attrs={'class': 'card-img card-img-top'}, alt=description, src=new_img_src)
    new_water_fall_item.append(new_img_element)
    water_fall_body.append(new_water_fall_item) 

def addHead(soup, tag1, tag2):
    title = tag1+'｜' + tag2 + '｜DCT Wedding 拾夢西式婚禮'
    description = tag1+'，'+tag2+'，婚禮規劃，專業婚顧，婚禮佈置花藝設計，西式婚禮團隊，婚禮婚紗攝影'
    link = 'http://dctwedding.com/portfolio_' + tag1

    # print('title:', title)
    # print('description:', description)
    # print('link:', link)

    # 查找<head>标签中的<title>标签
    title_tag = soup.head.find('title')
    if title_tag:
        title_tag.string = title

    meta_webTitle = addMetaName(soup, 'apple-mobile-web-app-title', title)
    soup.head.append(meta_webTitle)

    meta_description = addMetaName(soup, 'description', description)
    soup.head.append(meta_description)

    new_link = soup.new_tag('link', rel='stylesheet',
                            href='http://dctwedding.com/portfolio_食尚曼谷bistro&lounge')
    soup.head.append(new_link)

    meta_elements = addOg(soup, link, description,
                          "DCT Wedding 拾夢婚顧 西式婚禮 戶外婚禮", title)
    for meta_element in meta_elements:
        soup.head.append(meta_element)

def readHtml():
    # 使用绝对路径来确保可以找到文件
    html_file_path = os.path.join(os.path.dirname(__file__), 'template_blog.html')

    if not os.path.exists(html_file_path):
        # 如果找不到 template.html，使用 portfolio_La Villa 作为范本
        html_file_path = os.path.join(os.path.dirname(__file__), 'template_blog.html')
        
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 使用Beautiful Soup解析HTML 并复制一份
    soupTemplate = BeautifulSoup(html_content, 'html.parser')
    soup = copy.copy(soupTemplate)

    return soup

def copy_images(src_folder, dest_folder):
    """复制图片到目标文件夹"""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for file in os.listdir(src_folder):
        if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, file)
            shutil.copy2(src_path, dest_path)

def main(data_path):
    # 指定资料来源和图片目标路径
    IMAGE_DEST_PATH = 'assets/resized_photo/blog_2025-03-23'
    
    for folder_name in os.listdir(data_path):
        folder_path = os.path.join(data_path, folder_name)
        
        if os.path.isdir(folder_path):
            print(f"处理文件夹: {folder_name}")
            
            # 创建并复制图片到目标文件夹
            dest_folder = os.path.join(IMAGE_DEST_PATH, folder_name)
            copy_images(folder_path, dest_folder)
            print(f"已复制图片到：{dest_folder}")
            
            # 继续处理其他任务
            soup = readHtml()
            txt_files = [file for file in os.listdir(
                folder_path) if file.endswith('.txt')]
            print(f"找到的 .pages 檔案: {txt_files}")  # 印出找到的 .pages 檔案

            first_line = 'test'
            for txt_file in txt_files:
                txt_path = os.path.join(folder_path, txt_file)
                print(f"正在處理檔案: {txt_path}")  # 印出當前處理的檔案路徑
                encodings = ['utf-8', 'big5', 'gb2312', 'gbk']
                
                for encoding in encodings:
                    try:
                        with open(txt_path, 'r', encoding=encoding) as file:
                            first_line = file.readline().strip()
                            lines = file.readlines()
                            print(f"使用編碼 {encoding} 成功讀取檔案")
                            print(f"第一行內容: {first_line}")
                            print(f"所有行內容:")
                            for i, line in enumerate(lines, 1):
                                print(f"第 {i} 行: {line.strip()}")
                            addHead(soup, first_line, getSplitStr(lines[1]))
                            addH1(soup, first_line)
                            addli(soup, lines)
                            break  # 如果成功读取，跳出编码尝试循环
                    
                    except UnicodeDecodeError:
                        continue  # 如果当前编码失败，尝试下一个编码
                    except FileNotFoundError:
                        print(f'找不到文件：{txt_path}')
                        break
                    except Exception as e:
                        print(f"处理文件时发生错误：{str(e)}")
                        break
            addBImg(soup, folder_name, folder_name)
            # 获取子文件夹中的所有图片文件的文件名
            
            image_files = [filename for filename in os.listdir(
                folder_path) if filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            
            # 排序圖片檔案，忽略首圖
            sorted_images = sorted([img for img in image_files if img != "首圖.jpg"], 
                                 key=lambda x: int(''.join(filter(str.isdigit, x or '0')) or '0'))
            
            for image_file in sorted_images:
                addImg(soup, folder_name, image_file, folder_name)

            output_html_file = './output/portfolio_' + folder_name + '.html'  # 指定要保存修改后的HTML的文件路径
            with open(output_html_file, 'w', encoding='utf-8') as file:
                file.write(str(soup))
            
if __name__ == "__main__":
    # 检查必要文件和目录
    if not os.path.exists('template_blog.html'):
        print("错误：找不到 template_blog.html 文件")
        exit(1)

    data_path = os.path.join(os.path.dirname(__file__), 'data/blog_2025-03-23')
    if not os.path.exists(data_path):
        print(f"错误：找不到资料目录：{data_path}")
        print("请建立目录结构：./data/blog_2025-03-23/")
        exit(1)

    # 确保输出目录存在
    if not os.path.exists('./output'):
        print("创建输出目录：./output/")
        os.makedirs('./output')

    try:
        main(data_path)
        print("处理完成！输出文件在 output 目录中")
    except Exception as e:
        print(f"执行时发生错误：{str(e)}")
