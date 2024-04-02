import streamlit as st
import uuid
from utils import StreamHandler, get_faiss_db, main_chain, search_uploaded_docs
import ui_config

ui = ui_config.create_ui_from_config()
st.set_page_config(page_title=ui.page_title, layout="wide", page_icon=ui.page_icon)

# CSS style injection
st.markdown(
    ui.page_markdown,
    unsafe_allow_html=True,
)
if "state" not in st.session_state:
    st.session_state["state"] = str(uuid.uuid4()).replace("-", "")

# Sidebar for file upload
with st.sidebar:
    st.markdown(
        ui.sidebar_markdown,
        unsafe_allow_html=True,
    )
    col_image, col_text = st.columns([1, 4])
    with col_image:
        st.image(ui.sidebar_image)
    with col_text:
        st.title(ui.sidebar_title)
    st.subheader(ui.sidebar_subheader)
    uploaded_files = st.file_uploader(
        "请上传财务报表以分析",
        accept_multiple_files=True,
        type=None,
    )
    if uploaded_files:
        # Process uploaded files (e.g., through FAISS to build a database)
        # st.session_state["faiss_db"] = get_faiss_db_foragent(uploaded_files)
        st.session_state["faiss_db"] = get_faiss_db(uploaded_files)
        st.success("Files uploaded successfully!")

    if st.button("勾稽关系验证"):
        if uploaded_files:
            if "faiss_db" in st.session_state:
                st.session_state["processed"] = True  # 更新状态为已处理
            else:
                st.warning("Please upload files first.")
        else:
            st.warning("No files uploaded.")
            
    # Button for additional actions (e.g., processing the uploaded files)
if st.session_state.get("processed", False):  # 检查是否已处理
    docs_response = []
    docs_response.extend(
        search_uploaded_docs(
            "financial analysis focusing on the accounting equation: assets = liabilities + equity",
            top_k=16,
        )
    )
    # st.write(docs_response)
    user_query = f"""我正在进行财务分析，特别关注于验证会计基本等式：资产=负债+所有者权益。为此，我需要从最近一期的合并资产负债表中提取以下三项关键数据：
总资产的数值。
总负债的数值。
所有者权益合计的数值。
请基于您对财务报表的理解，提供这些数据的准确数值，并简要解释这些数据对于理解公司财务状况的重要性。"""
    input = f"""Must Follow:
- Respond to "{user_query}" by using information from "{docs_response}" (if available) and your own knowledge to provide a logical, clear, and critically analyzed reply in the same language.
- Employ bullet points selectively, where they add clarity or organization.
- Cite sources in main text using the Author-Date citation style where applicable.
- Provide a list of references in markdown format of [title.journal.authors.date.](hyperlinks) at the end (or just the source file name), only for the references mentioned in the generated text.
- Use LaTeX quoted by '$' or '$$' within markdown to render mathematical formulas.

Must Avoid:
- Repeat the human's query.
- Translate cited references into the query's language.
- Preface responses with any designation such as "AI:"."""

    st_callback = StreamHandler(st.empty())
    response = main_chain().invoke(
        {"input": input},
        {"callbacks": [st_callback]},
    )
    # st.write(response["text"])

