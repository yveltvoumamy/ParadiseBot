import csv
import pandas as pd
from pathlib import Path
import asyncio
from pathlib import Path
from aiogram.types import InputFile

'''

async def get_inputfile_from_jpg(file_path: Path) -> InputFile:
    with open(file_path, 'rb') as file:
        photo = file.read()
    return photo
'''

async def get_str_from_txt(file_path: Path) -> str:
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
async def add_id_to_csv(file_name: str, new_id: int, status=None) -> bool:
    df = pd.read_csv(Path('src', 'data', f'{file_name}.csv'))
    if new_id in df['id'].tolist():
        return False
    try:
        df.loc[len(df)] = pd.Series({'id': new_id, 'status': status})
    except:
        print('sloamlis tvoi kostyli ebanye')
    df.to_csv(Path('src', 'data', f'{file_name}.csv'), index=False)
    return True


def convert_csv_id_to_array(file_name: str) -> list[str]:
    df = pd.read_csv(Path('src', 'data', f'{file_name}.csv'))
    arr = df['id'].tolist()
    return arr


def get_attr_from_csv(file_name: str, attr_name: str) -> str:
    df = pd.read_csv(Path('src', 'data', f'{file_name}.csv'), encoding='CP1251')
    current_attr = df[attr_name].values[0]
    return current_attr


async def set_attr_from_csv(file_name: str, attr_name: str, new_attr: str) -> None:
    df = pd.read_csv(Path('src', 'data', f'{file_name}.csv'), encoding='CP1251')
    df[attr_name] = new_attr
    df.to_csv(Path('src', 'data', f'{file_name}.csv'), index=False, encoding='CP1251')
