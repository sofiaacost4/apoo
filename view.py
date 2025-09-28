
import streamlit as st
from controller import ItemController

st.set_page_config(page_title="APOO", layout="centered")
st.title("📝 Projeto e implementação de software")

st.header("Adicionar novo item")
with st.form(key="new_item_form", clear_on_submit=True):
    nome = st.text_input("Nome do item")
    quantidade = st.number_input("Quantidade de itens")
    descricao = st.text_area("Descrição do item:")
    submit_button = st.form_submit_button(label="Adicionar")

if submit_button:
    ItemController.criarItem(nome, descricao, quantidade)
    st.rerun()

st.markdown("---")

st.header("Itens adicionados recentemente")

tds_itens = ItemController.obterTodosOsItens()

if not tds_itens:
    st.info("Não há itens adicionados.")
else:
    for item in tds_itens:
        st.subheader(item.nome)
        st.caption(f"Quantidade: {item.quantidade}")
        st.write(item.descricao)
        st.markdown("---")