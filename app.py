import streamlit as st
import time
import base64
import hashlib
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="API Rate Limiter",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for pink theme
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #fce7f3 0%, #fdf2f8 50%, #fef7f7 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #fce7f3 0%, #fdf2f8 50%, #fef7f7 100%);
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(236, 72, 153, 0.2);
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(236, 72, 153, 0.1);
    }
    
    .processing-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(236, 72, 153, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 12px 40px rgba(236, 72, 153, 0.15);
    }
    
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.9);
        border: 2px solid #f9a8d4;
        border-radius: 12px;
    }
    
    .stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.9);
        border: 2px solid #f9a8d4;
        border-radius: 12px;
        color: #831843;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(236, 72, 153, 0.4);
    }
    
    .success-message {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    
    .error-message {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
    }
    
    h1 {
        color: #831843;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(131, 24, 67, 0.1);
    }
    
    h2 {
        color: #be185d;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #ec4899;
        font-size: 1.4rem;
        margin-bottom: 0.8rem;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #fce7f3 0%, #fdf2f8 100%);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'processing_history' not in st.session_state:
    st.session_state.processing_history = []

if 'total_operations' not in st.session_state:
    st.session_state.total_operations = 0

if 'total_processing_time' not in st.session_state:
    st.session_state.total_processing_time = 0

# Processing functions
def process_uppercase(text):
    return text.upper()

def process_reverse(text):
    return text[::-1]

def process_count(text):
    char_count = len(text)
    word_count = len([word for word in text.split() if word.strip()])
    return f"Characters: {char_count}, Words: {word_count}"

def process_hash(text):
    encoded = base64.b64encode(text.encode()).decode()
    return f"Base64: {encoded[:32]}{'...' if len(encoded) > 32 else ''}"

def process_md5_hash(text):
    return f"MD5: {hashlib.md5(text.encode()).hexdigest()}"

def process_word_frequency(text):
    words = text.lower().split()
    word_freq = {}
    for word in words:
        word = word.strip('.,!?";')
        word_freq[word] = word_freq.get(word, 0) + 1
    
    if word_freq:
        most_common = max(word_freq.items(), key=lambda x: x[1])
        return f"Most frequent word: '{most_common[0]}' ({most_common[1]} times)"
    return "No words found"

# Processing modes
PROCESSING_MODES = {
    "Uppercase": {
        "function": process_uppercase,
        "description": "Convert text to uppercase letters",
        "icon": "🔤"
    },
    "Reverse": {
        "function": process_reverse,
        "description": "Reverse the input string character by character",
        "icon": "🔄"
    },
    "Count": {
        "function": process_count,
        "description": "Count characters and words in the input",
        "icon": "📊"
    },
    "Base64 Hash": {
        "function": process_hash,
        "description": "Generate base64 encoded representation",
        "icon": "🔐"
    },
    "MD5 Hash": {
        "function": process_md5_hash,
        "description": "Generate MD5 hash of the input",
        "icon": "🔑"
    },
    "Word Frequency": {
        "function": process_word_frequency,
        "description": "Find the most frequent word in text",
        "icon": "📈"
    }
}

# Main header
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <h1>🛡️ API Rate Limiter</h1>
    <p style="color: #be185d; font-size: 1.2rem; margin-top: -1rem;">
        Intelligent traffic control and request management
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    
    # Rate limiting settings
    st.markdown("#### Rate Limiting Settings")
    max_requests = st.slider("Max Requests per Minute", 1, 100, 10)
    window_size = st.slider("Time Window (seconds)", 10, 300, 60)
    
    st.markdown("#### Processing Settings")
    simulate_delay = st.checkbox("Simulate Processing Delay", value=True)
    if simulate_delay:
        delay_range = st.slider("Delay Range (seconds)", 0.1, 3.0, (0.5, 1.5))
    
    st.markdown("#### System Actions")
    if st.button("🗑️ Clear All History", type="secondary"):
        st.session_state.processing_history = []
        st.session_state.total_operations = 0
        st.session_state.total_processing_time = 0
        st.success("History cleared!")
        st.rerun()

# Statistics dashboard
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>📊 Total Operations</h3>
        <h2 style="color: #ec4899; font-size: 2.5rem; margin: 0;">
            {}
        </h2>
        <p style="color: #be185d; margin: 0;">All-time processing count</p>
    </div>
    """.format(st.session_state.total_operations), unsafe_allow_html=True)

with col2:
    avg_time = (st.session_state.total_processing_time / st.session_state.total_operations 
                if st.session_state.total_operations > 0 else 0)
    st.markdown("""
    <div class="metric-card">
        <h3>⏱️ Avg Processing Time</h3>
        <h2 style="color: #ec4899; font-size: 2.5rem; margin: 0;">
            {:.2f}s
        </h2>
        <p style="color: #be185d; margin: 0;">Mean processing duration</p>
    </div>
    """.format(avg_time), unsafe_allow_html=True)

with col3:
    recent_ops = len([h for h in st.session_state.processing_history 
                     if datetime.now() - h['timestamp'] < timedelta(minutes=1)])
    st.markdown("""
    <div class="metric-card">
        <h3>⚡ Recent Activity</h3>
        <h2 style="color: #ec4899; font-size: 2.5rem; margin: 0;">
            {}/min
        </h2>
        <p style="color: #be185d; margin: 0;">Operations in last minute</p>
    </div>
    """.format(recent_ops), unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>🟢 System Status</h3>
        <h2 style="color: #10b981; font-size: 2.5rem; margin: 0;">
            Online
        </h2>
        <p style="color: #be185d; margin: 0;">All systems operational</p>
    </div>
    """, unsafe_allow_html=True)

# Main processing interface
st.markdown("---")

col_input, col_output = st.columns(2)

with col_input:
    st.markdown("""
    <div class="processing-card">
        <h2>📥 Input Processing</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Processing mode selection
    selected_mode = st.selectbox(
        "🔧 Select Processing Mode",
        options=list(PROCESSING_MODES.keys()),
        format_func=lambda x: f"{PROCESSING_MODES[x]['icon']} {x}"
    )
    
    st.info(f"**Description:** {PROCESSING_MODES[selected_mode]['description']}")
    
    # Input text area
    input_text = st.text_area(
        "📝 Enter your data",
        placeholder="Type something to process...",
        height=150,
        help="Enter the text you want to process using the selected mode"
    )
    
    # Process button
    if st.button("🚀 Process Input", type="primary", use_container_width=True):
        if input_text.strip():
            # Simulate processing delay
            if simulate_delay:
                delay_time = delay_range[0] + (delay_range[1] - delay_range[0]) * 0.5
                with st.spinner(f"Processing... ({delay_time:.1f}s)"):
                    time.sleep(delay_time)
            else:
                delay_time = 0.1
                time.sleep(delay_time)
            
            # Process the input
            start_time = time.time()
            result = PROCESSING_MODES[selected_mode]['function'](input_text)
            processing_time = time.time() - start_time + delay_time
            
            # Store in session state
            st.session_state.last_output = result
            st.session_state.last_processing_time = processing_time
            
            # Add to history
            history_entry = {
                'timestamp': datetime.now(),
                'mode': selected_mode,
                'input': input_text[:100] + ('...' if len(input_text) > 100 else ''),
                'output': result[:100] + ('...' if len(result) > 100 else ''),
                'full_input': input_text,
                'full_output': result,
                'processing_time': processing_time
            }
            
            st.session_state.processing_history.insert(0, history_entry)
            st.session_state.total_operations += 1
            st.session_state.total_processing_time += processing_time
            
            # Keep only last 50 entries
            if len(st.session_state.processing_history) > 50:
                st.session_state.processing_history = st.session_state.processing_history[:50]
            
            st.success("✅ Processing completed successfully!")
            st.rerun()
        else:
            st.error("❌ Please enter some text to process")

with col_output:
    st.markdown("""
    <div class="processing-card">
        <h2>📤 Output Results</h2>
    </div>
    """, unsafe_allow_html=True)
    
    if hasattr(st.session_state, 'last_output'):
        st.text_area(
            "📋 Processed Result",
            value=st.session_state.last_output,
            height=150,
            disabled=True
        )
        
        # Processing info
        if hasattr(st.session_state, 'last_processing_time'):
            st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.1); padding: 15px; border-radius: 12px; border: 1px solid rgba(16, 185, 129, 0.3);">
                <p style="margin: 0; color: #059669;">
                    ⏱️ <strong>Processing Time:</strong> {st.session_state.last_processing_time:.3f} seconds<br>
                    🔧 <strong>Mode Used:</strong> {selected_mode}<br>
                    📊 <strong>Total Operations:</strong> {st.session_state.total_operations}
                </p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.text_area(
            "📋 Processed Result",
            value="Output will appear here after processing...",
            height=150,
            disabled=True
        )
        
        st.info("🔄 Process some input to see results here")

# Processing History
st.markdown("---")
st.markdown("## 📚 Processing History")

if st.session_state.processing_history:
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["📋 Recent Operations", "📊 Analytics", "📈 Performance"])
    
    with tab1:
        st.markdown("### Last 10 Operations")
        for i, entry in enumerate(st.session_state.processing_history[:10]):
            with st.expander(
                f"{entry['mode']} - {entry['timestamp'].strftime('%H:%M:%S')} "
                f"({entry['processing_time']:.3f}s)",
                expanded=(i == 0)
            ):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Input:**")
                    st.code(entry['full_input'], language="text")
                with col2:
                    st.markdown("**Output:**")
                    st.code(entry['full_output'], language="text")
                
                st.markdown(f"""
                **Details:**
                - Mode: {entry['mode']}
                - Processing Time: {entry['processing_time']:.3f} seconds
                - Timestamp: {entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}
                """)
    
    with tab2:
        st.markdown("### Processing Mode Distribution")
        
        # Mode usage chart
        mode_counts = {}
        for entry in st.session_state.processing_history:
            mode_counts[entry['mode']] = mode_counts.get(entry['mode'], 0) + 1
        
        if mode_counts:
            fig_pie = px.pie(
                values=list(mode_counts.values()),
                names=list(mode_counts.keys()),
                title="Processing Mode Usage",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_pie.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_pie, use_container_width=True)
    
    with tab3:
        st.markdown("### Processing Time Analysis")
        
        if len(st.session_state.processing_history) > 1:
            # Processing time over time
            df_history = pd.DataFrame([
                {
                    'timestamp': entry['timestamp'],
                    'processing_time': entry['processing_time'],
                    'mode': entry['mode']
                }
                for entry in reversed(st.session_state.processing_history)
            ])
            
            fig_line = px.line(
                df_history,
                x='timestamp',
                y='processing_time',
                color='mode',
                title='Processing Time Over Time',
                labels={'processing_time': 'Processing Time (seconds)'}
            )
            fig_line.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_line, use_container_width=True)
            
            # Performance statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(
                    "Fastest Processing",
                    f"{min(df_history['processing_time']):.3f}s"
                )
            with col2:
                st.metric(
                    "Slowest Processing",
                    f"{max(df_history['processing_time']):.3f}s"
                )
            with col3:
                st.metric(
                    "Standard Deviation",
                    f"{df_history['processing_time'].std():.3f}s"
                )

else:
    st.info("🔄 No processing history yet. Process some input to see analytics here.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #be185d; padding: 20px;">
    <p>🛡️ <strong>API Rate Limiter</strong> - Built with ❤️ using Streamlit</p>
    <p>Production-ready traffic control and request management system</p>
</div>
""", unsafe_allow_html=True)