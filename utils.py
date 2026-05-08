import os
import re
import subprocess
import sys
from config import DOWNLOADS_PATH


def ensure_downloads_folder():
    """Создать папку Downloads если нет"""
    os.makedirs(DOWNLOADS_PATH, exist_ok=True)


def open_downloads_folder():
    """Открыть папку Downloads в проводнике"""
    ensure_downloads_folder()
    if sys.platform == 'win32':
        os.startfile(DOWNLOADS_PATH)


def is_valid_url(url):
    """Проверка что это похоже на URL"""
    pattern = r'^https?://(www\.)?(soundcloud\.com|youtube\.com|youtu\.be|music\.youtube\.com)/.+'
    return bool(re.match(pattern, url.strip()))


def sanitize_filename(name):
    """Убрать недопустимые символы из имени файла"""
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()
