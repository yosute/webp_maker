from PIL import Image
import shutil
import os


dir_path = "./img"

files = os.listdir(dir_path)

def convert_to_webp(input_folder, output_folder):
    # 入力フォルダ内のすべてのファイルを取得
    file_list = os.listdir(input_folder)
    compile_quality = 100
    if file_list:
      if not os.path.isdir(output_folder):
        print(output_folder)
        os.mkdir(output_folder)

      for file_name in file_list:
            
          if file_name.endswith('.png') or file_name.endswith('.jpeg') or file_name.endswith('.jpg'):
              # 画像を開く
              image = Image.open(os.path.join(input_folder, file_name))
              
              # 出力ファイル名を設定
              output_file = os.path.splitext(file_name)[0] + '.webp'

              # WebP形式に変換して保存
              image.save(os.path.join(output_folder, output_file), 'webp', quality = compile_quality)
              
              # 画像を閉じる
              image.close()
          else:
              origin_path = input_folder + '/' + file_name
              output_path = output_folder + '/' + file_name 
              shutil.move(origin_path , output_path)
            

# 使用例
# convert_to_webp('input_folder', 'output_folder')

for dir_name in files:
    inputfolder = dir_path + '/' + dir_name
    outputfolder = dir_path + '/' + dir_name + '_webp'
    if not 'webp' in inputfolder :
      convert_to_webp( inputfolder , outputfolder)