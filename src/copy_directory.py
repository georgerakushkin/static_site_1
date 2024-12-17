import os
import shutil
import logging

def copy_directory(src_dir: str, dst_dir: str):
    try:
        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"source directory '{src_dir}' does not exist")
        
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dst_path = os.path.join(dst_dir, item)

            try:
                if os.path.isdir(src_path):
                    copy_directory(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
            except Exception as e:
                logging.error(f"Failed to copy {src_path}: {str(e)}")
    except Exception as e:
        logging.error(f"Directory copy failed: {str(e)}")
        raise