import shutil
import os


class FileBackupManager:
    """
    Менеджер для автоматичного резервного копіювання файлів перед їх обробкою.
    Якщо обробка пройде успішно, оригінальний файл замінюється новим.
    Якщо виникне помилка, резервна копія відновлюється.
    """

    def __init__(self, file_path: str, backup_dir: str):
        """
        Ініціалізація менеджера резервного копіювання.
        """
        self.file_path = file_path
        self.backup_dir = backup_dir
        self.backup_path = os.path.join(backup_dir, os.path.basename(file_path))
        self.backup_created = False

    def create_backup(self) -> bool:
        """
        Створення резервної копії файлу перед обробкою.
        """
        try:
            shutil.copy2(self.file_path, self.backup_path)
            self.backup_created = True
            print(f"Backup created: {self.backup_path}")
            return True
        except Exception as e:
            print(f"Error while creating the backup: {e}")
            return False

    def restore_backup(self) -> bool:
        """
        Відновлення резервної копії в разі помилки.
        """
        if not self.backup_created:
            print("Backup was not created, restoration is not possible.")
            return False
        try:
            shutil.copy2(self.backup_path, self.file_path)
            print(f"Backup restored: {self.file_path}")
            return True
        except Exception as e:
            print(f"Error while restoring the backup: {e}")
            return False

    def process_file(self, process_function) -> bool:
        """
        Обробка файлу з перевіркою резервного копіювання.
        """
        if not self.create_backup():
            return False

        try:
            # Create a temporary file path for processed file
            temp_processed_file_path = self.file_path + '.processed'

            if process_function(self.file_path, temp_processed_file_path):
                # Rename processed file to original file
                os.rename(temp_processed_file_path, self.file_path)
                print(f"Original file replaced with the new one: {self.file_path}")
                return True
            else:
                print("Processing was not successful.")
                return False
        except Exception as e:
            print(f"Error during file processing: {e}")
            self.restore_backup()
            return False


# Приклад використання:
def example_process(file_path: str, temp_file_path: str) -> bool:
    """
    Приклад функції для обробки файлу.
    """
    try:
        # Create the processed file at the temporary file path
        with open(temp_file_path, 'w') as file:
            file.write("New text added to the file.")
        return True
    except Exception as e:
        print(f"Error while processing the file: {e}")
        return False


# Введіть шляхи до файлів
original_file_path = '/Users/anton01.16.23/Desktop/untitled folder/sample3.txt'
backup_directory = '/Users/anton01.16.23/Desktop'

# Створення менеджера та обробка файлу
manager = FileBackupManager(original_file_path, backup_directory)
manager.process_file(example_process)
