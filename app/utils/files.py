import os, shutil, tempfile


class temporary_file_copy(object):

    def __init__(self, original_path):
        self.original_path = original_path

    def __enter__(self):
        temp_dir = tempfile.gettempdir()
        base_path = os.path.basename(self.original_path)
        self.path = os.path.join(temp_dir, base_path)
        shutil.copy2(self.original_path, self.path)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.path)
