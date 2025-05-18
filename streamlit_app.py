# streamlit_app.py

try:
    import streamlit as st
    from PIL import Image
except ModuleNotFoundError as e:
    print("Erro: Módulo não encontrado. Certifique-se de que 'streamlit' e 'Pillow' estão instalados usando:")
    print("pip install streamlit pillow")
    raise SystemExit

# Título do app
st.title("Loja Online de Roupas 🛍️")

# Menu lateral
menu = st.sidebar.selectbox("Navegação", ["Home", "Produtos", "Carrinho", "Contato"])

# Catálogo de produtos (exemplo simplificado)
produtos = {
    "Camiseta Unissex": {"preco": 59.90, "imagem": "camiseta.jpg"},
    "Calça Jeans": {"preco": 129.90, "imagem": "calca.jpg"},
    "Vestido Floral": {"preco": 149.90, "imagem": "vestido.jpg"},
    "Jaqueta de Couro": {"preco": 199.90, "imagem": "jaqueta.jpg"}
}

# Carrinho (mantido em sessão)
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# Página Home
if menu == "Home":
    st.header("Bem-vinde à nossa loja de roupas online!")
    st.write("Aqui você encontra estilo, conforto e preços acessíveis. Use o menu para explorar.")
    try:
        st.image("loja_banner.jpg", use_column_width=True)
    except:
        st.warning("Imagem 'loja_banner.jpg' não encontrada.")

# Página de Produtos
elif menu == "Produtos":
    st.header("Nossos Produtos")
    col1, col2 = st.columns(2)
    for i, (nome, info) in enumerate(produtos.items()):
        with col1 if i % 2 == 0 else col2:
            st.subheader(nome)
            try:
                st.image(info["imagem"], width=250)
            except:
                st.warning(f"Imagem '{info['imagem']}' não encontrada.")
            st.write(f"Preço: R$ {info['preco']:.2f}")
            if st.button(f"Adicionar ao carrinho - {nome}"):
                st.session_state.carrinho.append(nome)
                st.success(f"{nome} adicionado ao carrinho.")

# Página do Carrinho
elif menu == "Carrinho":
    st.header("Seu Carrinho")
    total = 0
    if st.session_state.carrinho:
        for item in st.session_state.carrinho:
            preco = produtos[item]["preco"]
            st.write(f"{item} - R$ {preco:.2f}")
            total += preco
        st.write(f"**Total: R$ {total:.2f}**")
        if st.button("Finalizar Compra"):
            st.success("Compra realizada com sucesso! Obrigado por comprar conosco.")
            st.session_state.carrinho = []
    else:
        st.write("Seu carrinho está vazio.")

# Página de Contato
elif menu == "Contato":
    st.header("Fale Conosco")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    mensagem = st.text_area("Mensagem")
    if st.button("Enviar"):
        if nome and email and mensagem:
            st.success("Mensagem enviada! Responderemos em breve.")
        else:
            st.warning("Por favor, preencha todos os campos.")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido com ❤️ usando Streamlit by @daniellvalentimm")
