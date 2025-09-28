import sqlite3
import pandas as pd
from model.py import Item

DB_name = 'item.db' # Nome do arquivo do banco de dados como uma constante

class ItemDAO:
    __objetos = []