"""
Created by HE on 2023/8/31.

This is a description of the file.
"""

import chardet

def replace_in_file(file_path, old_str, new_str):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            detected_encoding = chardet.detect(raw_data)['encoding']
        with open(file_path, 'r', encoding=detected_encoding) as input_file:
            file_data = input_file.read()
        # 进行字符替换
        modified_data = file_data.replace(old_str, new_str)
        with open(file_path, 'w', encoding=detected_encoding) as file:
            file.write(modified_data)
        print(f"替换 '{old_str}' 为 '{new_str}' 完成！")
    except Exception as e:
        print(f"替换过程中出现错误：{e}")


# 调用示例
file_path = 'demo.txt'  # 替换为实际文件路径
old_str = '32-bit'  # 要替换的旧文本
new_str = '33-bit'  # 要替换成的新文本

replace_in_file(file_path, old_str, new_str)