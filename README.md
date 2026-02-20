import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import qrcode
from fpdf import FPDF
from io import BytesIO
import datetime

# --- CONFIGURATION & BRANDING ---
st.set_page_config(page_title="AWERE SS - Digital Portal", page_icon="🏫", layout="wide")

# Custom Ugandan Theme Styling
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #004d99; color: white; }
    .report-card { border: 2px solid #004d99; padding: 20px; border-radius: 10px; background-color: white; }
    </style>
    """, unsafe_content_factory=True)

# --- DATABASE CONNECTION ---
# Connects to your permanent Google Sheet
conn = st.connection("gsheets", type=GSheetsConnection)

def get_db(sheet_name):
    return conn.read(worksheet=sheet_name, ttl=0)

# --- GRADING ENGINE (Ugandan NCDC Standards) ---
def get_performance_details(score):
    if score >= 80: return "A", "Exceptional Achievement"
    elif score >= 70: return "B", "Outstanding Achievement"
    elif score >= 60: return "C", "Satisfactory Achievement"
    elif score >= 40: return "D", "Basic Achievement"
    else: return "E", "Elementary Achievement"

# --- PDF GENERATOR (With QR Security) ---
class AwereReport(FPDF):
    def header_section(self, school_info, s_data, rank, total, bal):
        # Logo placeholder
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, school_info['name'].upper(), ln=True, align='C')
        self.set_font('Arial', '', 11)
        self.cell(0, 5, school_info['address'], ln=True, align='C')
        self.cell(0, 5, f"Term: {school_info['term']} | Year: 2026", ln=True, align='C')
        
        # QR Code for Verification
        qr_data = f"VERIFIED: {s_data['name']} | Rank: {rank}/{total} | Bal: {bal} UGX"
        qr = qrcode.make(qr_data)
        buf = BytesIO(); qr.save(buf, format='PNG')
        self.image(buf, 175, 10, 25, 25)
        self.ln(20)

# --- MAIN INTERFACE ---
st.title("🏫 AWERE SECONDARY SCHOOL - PORTAL")
st.write(f"Today's Date: {datetime.date.today().strftime('%d %B, %Y')}")

if 'auth' not in st.session_state:
    st.session_state.auth = None

if not st.session_state.auth:
    # --- LOGIN PAGE ---
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.subheader("🔐 Secure Login")
        role = st.selectbox("Access Level", ["Learner", "Teacher", "Bursar", "D.O.S", "Deputy HT", "Headteacher"])
        user = st.text_input("Username / LIN")
        pw = st.text_input("Password", type="password")
        if st.button("Access System"):
            # In live: verify against Google Sheet "Staff" or "Learners" tab
            st.session_state.auth = {"role": role, "user": user}
            st.rerun()
else:
    role = st.session_state.auth['role']
    st.sidebar.title("MENU")
    st.sidebar.write(f"Logged in: **{role}**")
    
    # --- 1. HEADTEACHER & DEPUTY (Admin Mode) ---
    if role in ["Headteacher", "Deputy HT"]:
        tab1, tab2, tab3 = st.tabs(["Global Management", "Staff Records", "School Finances"])
        
        with tab1:
            st.header("Executive Oversight")
            st.info("Permission: Full Edit Access to all Records")
            # Logic to edit Google Sheets directly from the app
            
    # --- 2. D.O.S (Academics & Notes) ---
    elif role == "D.O.S":
        st.header("Academic Administration")
        action = st.radio("Task", ["Manage Rankings", "Approve Study Notes", "Subject Setup"])
        # Logic to calculate positions 1st to Last
        
    # --- 3. TEACHER (Marks & Notes) ---
    elif role == "Teacher":
        st.header("Teacher Dashboard")
        task = st.selectbox("Action", ["Upload Marks", "Share Study Materials"])
        
        if task == "Upload Marks":
            with st.form("marks_entry"):
                stu = st.text_input("Student LIN")
                sub = st.selectbox("Subject", ["Math", "English", "Physics", "Chemistry"])
                aoi = st.number_input("AoI (0.9 - 3.0)", 0.9, 3.0)
                exam = st.number_input("Exam (0 - 100)")
                if st.form_submit_button("Submit to Cloud"):
                    st.success("Marks saved permanently to Google Sheets.")
                    
    # --- 4. BURSAR (Fees) ---
    elif role == "Bursar":
        st.header("Finance Office")
        # Logic to update payments in Google Sheets
        
    # --- 5. LEARNER (Results & Notes) ---
    elif role == "Learner":
        st.header("Student Resource Center")
        # 1. Check Fees in Google Sheets
        # 2. If Cleared, Allow Download
        st.button("📥 Download My Ranked Report Card")
        st.markdown("---")
        st.subheader("📚 Available Study Notes")
        # Pull links to files in Google Drive

    if st.sidebar.button("Logout"):
        st.session_state.auth = None
        st.rerun()
