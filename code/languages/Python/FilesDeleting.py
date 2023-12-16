from pathlib import Path
import os


if __name__ == "__main__":
	current_dir = Path(__file__).parent.resolve()
	
	file_path = current_dir / "files.txt"

	with open(file_path, "a+", encoding="utf-8") as f:
		for path in sorted(list(current_dir.glob("*.*"))):
			name = path.name

			if name not in ["delete_file.py", "files.txt"]:
				f.write(f"{name}\n\n")
				os.remove(path)
			