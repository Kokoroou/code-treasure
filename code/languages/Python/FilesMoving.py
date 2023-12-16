from pathlib import Path
import shutil
import os

MAIN_DIR = Path(__file__).parent.resolve()


with open('Danh sách trò chơi.txt', 'w', encoding='utf-8') as file:
	file_paths = [path for path in list(MAIN_DIR.glob('*.pptx')) + list(MAIN_DIR.glob('*.ppt'))]

	for i in range(len(file_paths)):
		file_path = file_paths[i]
		file_name = file_path.name
		folder_num = i // 5 + 1
		
		new_folder_name = f'Thư mục {folder_num}'

		if i % 5 == 0:
			file.write(f'{new_folder_name}:\n')
			os.mkdir(str(Path(file_path.parent, new_folder_name)))
		file.write(f'{file_name}\n')
		if i % 5 == 4:
			file.write('\n')

		new_file_path = Path(file_path.parent, new_folder_name, file_name)
		shutil.move(str(file_path), str(new_file_path))
		
		