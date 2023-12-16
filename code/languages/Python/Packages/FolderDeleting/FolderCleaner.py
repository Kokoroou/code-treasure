import shutil
import time
from pathlib import Path


def delete_directory(path: Path):
    try:
        shutil.rmtree(path)
        print(f"Thư mục {path} đã được xóa.")
    except OSError as error:
        print(f"Có lỗi xảy ra khi xóa thư mục {path}: {error}")


if __name__ == "__main__":
    directory_path = Path("./Eduskill32bitFull/EduSkill32bitFull/Portals/ChuDe")

    if directory_path.exists():
        directory_path.resolve()

        sub_paths = list(directory_path.rglob("*"))

        if len(sub_paths) == 0:
            print(f"Thư mục {directory_path} trống.")

        for path in sub_paths:
            if path.is_file():
                path.unlink(missing_ok=True)
            elif path.is_dir():
                delete_directory(path)
    else:
        print(f"Thư mục {directory_path} không tồn tại.")
    
    print()
    print("--------------------")
    print("Chương trình sẽ kết thúc sau 5 giây.")
    time.sleep(5)
