from typing import List
import streamlit as st

from model import Item
from database import ItemDAO

class ItemController: 
    dao = ItemDAO() 
                                                                                                                            
    @staticmethod
    @st.cache_data
    def obterTodosOsItens() -> List[Item]:  #obterTodosOsItens() -> list[Item]
        return ItemController.dao.listarTodos()

    @staticmethod
    def criarItem(nome: str, descricao: str, quantidade: int):  #criarItem(nome: string, descricao: string, quantidade: int)
        if len(nome) < 5:
            st.error("O nome do item deve ter pelo menos 5 caracteres.")
            return
        novo_item = Item(nome=nome, descricao=descricao, quantidade=quantidade)
        ItemController.dao.adicionar(novo_item)
        st.cache_data.clear()
    
#Criar uma classe ItemController com os seguintes métodos, que farão a interface com a View:
#criarItem(nome: string, descricao: string, quantidade: int)
#obterTodosOsItens() -> list[Item]