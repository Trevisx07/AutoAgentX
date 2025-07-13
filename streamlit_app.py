import streamlit as st
import requests
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="AutoAgentX",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
  
    
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    .success-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="main-header">
    <h1>🤖 AutoAgentX</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">Your Only Smart AI Agent</p>
</div>
""", unsafe_allow_html=True)

API_BASE = "http://127.0.0.1:8000"


with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/artificial-intelligence.png", width=80)
    st.title("Navigation")
    
    selected = option_menu(
        menu_title=None,
        options=["📄 Summarizer", "❓ Q&A", "📝 Email Generator"],
        icons=["file-text", "question-circle", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "#667eea", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#667eea"},
        }
    )

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if selected == "📄 Summarizer":
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 📄 Document Summarizer")
        st.markdown("Upload your document and get an intelligent summary in seconds")
        
        with st.form("summarizer", clear_on_submit=True):
            file = st.file_uploader(
                "Choose a .txt file",
                type=["txt"],
                help="Upload a text document to get a concise summary"
            )
            
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
            with col_btn2:
                submitted = st.form_submit_button("✨ Generate Summary", use_container_width=True)
            
            if submitted and file:
                with st.spinner("🔄 Analyzing document..."):
                    try:
                        response = requests.post(f"{API_BASE}/summarize", files={"file": file})
                        if response.status_code == 200:
                            st.markdown('<div class="success-message">', unsafe_allow_html=True)
                            st.markdown("### 📋 Summary")
                            st.write(response.json().get("summary"))
                            st.markdown('</div>', unsafe_allow_html=True)
                        else:
                            st.error("Failed to generate summary. Please try again.")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected == "❓ Q&A":
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### ❓ Q&A on Document")
        st.markdown("Upload a document and ask questions to get intelligent answers")
        
        with st.form("qa", clear_on_submit=True):
            file_qa = st.file_uploader(
                "Upload Document for Q&A",
                type=["txt"],
                key="qa_file",
                help="Upload a document to ask questions about"
            )
            
            question = st.text_input(
                "💬 Ask your question:",
                placeholder="What would you like to know about the document?"
            )
            
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
            with col_btn2:
                submitted_qa = st.form_submit_button("🔍 Get Answer", use_container_width=True)
            
            if submitted_qa and file_qa and question:
                with st.spinner("🤔 Finding the answer..."):
                    try:
                        response = requests.post(
                            f"{API_BASE}/ask",
                            files={"file": file_qa},
                            data={"question": question}
                        )
                        if response.status_code == 200:
                            st.markdown('<div class="success-message">', unsafe_allow_html=True)
                            st.markdown("### 💡 Answer")
                            st.write(response.json().get("answer"))
                            st.markdown('</div>', unsafe_allow_html=True)
                        else:
                            st.error("Failed to get answer. Please try again.")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected == "📝 Email Generator":
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Email Generator")
        st.markdown("Generate professional emails based on your context and instructions")
        
        with st.form("email", clear_on_submit=True):
            context = st.text_area(
                "📝 Context for Email:",
                placeholder="e.g., meeting notes, project updates, client requirements...",
                height=100
            )
            
            instruction = st.text_input(
                "📋 Instruction:",
                placeholder="e.g., 'Write a follow-up email', 'Create a thank you note'..."
            )
            
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
            with col_btn2:
                submitted_email = st.form_submit_button("✉️ Generate Email", use_container_width=True)
            
            if submitted_email and context and instruction:
                with st.spinner("✍️ Crafting your email..."):
                    try:
                        response = requests.post(
                            f"{API_BASE}/email-draft",
                            data={"context": context, "instruction": instruction}
                        )
                        if response.status_code == 200:
                            st.markdown('<div class="success-message">', unsafe_allow_html=True)
                            st.markdown("### 📧 Generated Email")
                            st.write(response.json().get("email"))
                            st.markdown('</div>', unsafe_allow_html=True)
                        else:
                            st.error("Failed to generate email. Please try again.")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>🚀 Powered by AutoAgentX | Built By Het Patel</p>
</div>
""", unsafe_allow_html=True)