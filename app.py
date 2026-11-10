"""Frontend: interface em Python (Streamlit) que consome a API."""
import requests
import streamlit as st

API = "http://127.0.0.1:8000/empresas"

st.set_page_config(page_title="Cadastro de Empresas", page_icon="🏢")
st.title("🏢 Cadastro de Empresas")


def chamar(metodo, url=API, **kwargs):
    """Faz o pedido à API e trata os erros mais comuns."""
    try:
        r = requests.request(metodo, url, timeout=5, **kwargs)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        st.error("API desligada. Inicie-a com: uvicorn api:app --reload")
    except requests.exceptions.HTTPError as e:
        st.error(f"Erro da API: {e.response.text}")
    return None


# mensagem que sobrevive ao st.rerun()
if "msg" in st.session_state:
    st.success(st.session_state.pop("msg"))

aba1, aba2 = st.tabs(["➕ Cadastrar", "📋 Ver / Editar / Remover"])

# ---------- CREATE ----------
with aba1:
    with st.form("form_criar", clear_on_submit=True):
        nome = st.text_input("Nome *")
        nif = st.text_input("NIF")
        telefone = st.text_input("Telefone")
        cidade = st.text_input("Cidade")
        enviar = st.form_submit_button("Guardar")
    if enviar:
        if not nome.strip():
            st.warning("O nome é obrigatório.")
        else:
            res = chamar("POST", json={"nome": nome, "nif": nif, "telefone": telefone, "cidade": cidade})
            if res is not None:
                st.success(f"Empresa '{res['nome']}' cadastrada com o ID {res['id']}!")

# ---------- READ / UPDATE / DELETE ----------
with aba2:
    empresas = chamar("GET")
    if empresas is None:
        st.stop()
    if not empresas:
        st.info("Ainda não há empresas cadastradas.")
    else:
        st.dataframe(empresas, use_container_width=True, hide_index=True)
        st.divider()

        escolhida = st.selectbox(
            "Escolha uma empresa para editar ou remover",
            empresas,
            format_func=lambda e: f"{e['id']} - {e['nome']}",
        )
        eid = escolhida["id"]

        n = st.text_input("Nome", escolhida["nome"], key=f"nome_{eid}")
        i = st.text_input("NIF", escolhida["nif"], key=f"nif_{eid}")
        t = st.text_input("Telefone", escolhida["telefone"], key=f"tel_{eid}")
        c = st.text_input("Cidade", escolhida["cidade"], key=f"cid_{eid}")

        col1, col2 = st.columns(2)
        if col1.button("💾 Atualizar", use_container_width=True):
            if not n.strip():
                st.warning("O nome é obrigatório.")
            elif chamar("PUT", f"{API}/{eid}", json={"nome": n, "nif": i, "telefone": t, "cidade": c}) is not None:
                st.session_state["msg"] = "Empresa atualizada!"
                st.rerun()
        if col2.button("🗑️ Remover", use_container_width=True):
            if chamar("DELETE", f"{API}/{eid}") is not None:
                st.session_state["msg"] = "Empresa removida!"
                st.rerun()
