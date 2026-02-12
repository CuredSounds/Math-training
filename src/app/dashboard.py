import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# Add project root to path so we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.core.logger import Logger

# Initialize Logger
logger = Logger().get_logger()

# Page Config
st.set_page_config(page_title="Math Foundations Tracker", layout="wide")

# File Path (Relative to src/app/dashboard.py -> ../../data/dashboard.csv)
DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")
CSV_FILE = os.path.join(DATA_DIR, "dashboard.csv")
NOTES_DIR = os.path.join(DATA_DIR, "notes")

def load_data():
    try:
        if not os.path.exists(CSV_FILE):
            logger.warning("Dashboard CSV not found, creating new one.")
            return pd.DataFrame(columns=["Week", "Track", "Module", "Topic", "Planned Hours", "Status", "Output Lab"])
        df = pd.read_csv(CSV_FILE)
        # Ensure Link column is string to avoid Streamlit errors
        df["Output Lab"] = df["Output Lab"].fillna("")
        return df
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        st.error("Failed to load data. Check logs.")
        return pd.DataFrame()

def save_data(df):
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        df.to_csv(CSV_FILE, index=False)
        logger.info("Dashboard data saved successfully.")
    except Exception as e:
        logger.error(f"Failed to save data: {e}")
        st.error("Failed to save data. Check logs.")

# Title
st.title("📚 Math Foundations for ML & Data Science")
st.markdown("Track your progress through the 16-week curriculum.")

# Load Data
if "df" not in st.session_state:
    st.session_state.df = load_data()

df = st.session_state.df

# --- Sidebar: Filters & Summary ---
st.sidebar.header("Filters")
selected_week = st.sidebar.selectbox("Select Week", ["All"] + list(df["Week"].unique()))

# --- Metrics ---
total_hours = df["Planned Hours"].sum()
completed_hours = df[df["Status"] == "Done"]["Planned Hours"].sum()
in_progress_hours = df[df["Status"] == "In Progress"]["Planned Hours"].sum() * 0.5 # Assume 50% done
progress_pct = (completed_hours + in_progress_hours) / total_hours

col1, col2, col3 = st.columns(3)
col1.metric("Total Hours Planned", f"{total_hours} h")
col2.metric("Hours Completed (Est.)", f"{completed_hours + in_progress_hours:.1f} h")
col3.metric("Progress", f"{progress_pct:.1%}")

st.progress(progress_pct)

# --- Main Data Editor ---
st.subheader("Weekly Schedule")

if selected_week != "All":
    display_df = df[df["Week"] == selected_week]
else:
    display_df = df

# Edit Data
edited_df = st.data_editor(
    display_df,
    column_config={
        "Status": st.column_config.SelectboxColumn(
            "Status",
            help="Current status of the module",
            width="medium",
            options=["Not Started", "In Progress", "Done"],
            required=True,
        ),
        "Output Lab": st.column_config.LinkColumn("Output Lab"),
        "Planned Hours": st.column_config.NumberColumn("Hours", format="%d h"),
    },
    use_container_width=True,
    hide_index=True,
    num_rows="dynamic"
)

# Save Button
if st.button("Save Changes"):
    # Update the original dataframe with changes
    # Use index to update correctly even if filtered
    # st.data_editor returns a new dataframe, we need to merge it back to the main source of truth
    
    if selected_week != "All":
        # Update only the rows that were visible/edited
        # We need to ensure we map back to the original indices if possible, 
        # but since we hid index, we rely on the fact that we passed a filtered DF. 
        # Actually data_editor with filtered DF just returns the filtered DF modified.
        # We need to update the main st.session_state.df
        
        # Strategy: iterate over the edited_df and update st.session_state.df based on matching columns (Day, Track etc)
        # Or simpler: Re-load full DF, update rows where Week == selected_week with edited_df values
        
        # But wait, data_editor doesn't return the index if hide_index=True? 
        # Actually it returns a new DF with reset index if we aren't careful.
        # Let's rely on mapping by Week + Track which should be unique key here.
        
        for index, row in edited_df.iterrows():
            # Find matching row in main DF
            mask = (st.session_state.df["Week"] == row["Week"]) & (st.session_state.df["Track"] == row["Track"])
            st.session_state.df.loc[mask, "Status"] = row["Status"]
            st.session_state.df.loc[mask, "Output Lab"] = row["Output Lab"]
            # Update other fields if editable
            
    else:
        st.session_state.df = edited_df

    save_data(st.session_state.df)
    st.success("✅ Progress saved to dashboard.csv!")
    st.rerun()

# --- Tabs Layout ---
# --- Tabs Layout ---
st.divider()
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Analytics", "✍️ Scratchpad", "📚 Classroom", "🏋️ Practice Arena", "🚀 Simulation Lab"])

# --- Tab 1: Analytics ---
with tab1:
    st.subheader("Analytics")
    # 1. Hours by Track
    hours_by_track = df.groupby("Track")["Planned Hours"].sum().reset_index()
    fig_track = px.bar(hours_by_track, x="Track", y="Planned Hours", title="Workload Distribution by Track")
    st.plotly_chart(fig_track, use_container_width=True)

    # 2. Status Breakdown
    status_counts = df["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]
    fig_status = px.pie(status_counts, values="Count", names="Status", title="Status Breakdown", hole=0.4)
    st.plotly_chart(fig_status, use_container_width=True)

# --- Tab 2: Scratchpad ---
with tab2:
    st.subheader("✍️ Scratchpad")
    st.markdown("Use your Wacom tablet or mouse to solve problems or take notes.")

    from streamlit_drawable_canvas import st_canvas
    from PIL import Image

    # Sidebar controls for drawing
    stroke_width = st.slider("Stroke width: ", 1, 25, 3)
    stroke_color = st.color_picker("Stroke color: ", "#000000")
    bg_color = st.color_picker("Background color: ", "#ffffff")
    
    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=600,
        width=800,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Save to Notes
    if canvas_result.image_data is not None:
        if st.button("Save to Notes"):
            if not os.path.exists(NOTES_DIR):
                os.makedirs(NOTES_DIR)
            
            img_data = canvas_result.image_data
            im = Image.fromarray(img_data.astype("uint8"), mode="RGBA")
            
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(NOTES_DIR, f"note_{timestamp}.png")
            try:
                im.save(filename, "PNG")
                st.success(f"Saved to {filename}!")
                logger.info(f"Saved note: {filename}")
            except Exception as e:
                logger.error(f"Failed to save note: {e}")
                st.error("Failed to save note.")
            
    # Show saved notes
    if os.path.exists(NOTES_DIR):
        st.divider()
        st.subheader("Saved Notes")
        note_files = sorted(os.listdir(NOTES_DIR), reverse=True)
        if note_files:
            selected_note = st.selectbox("View Note:", note_files)
            if selected_note:
                st.image(os.path.join(NOTES_DIR, selected_note), caption=selected_note)

# --- Tab 3: Classroom ---
with tab3:
    st.subheader("📚 Classroom")
    st.markdown("Interactive lessons to visualize mathematical concepts.")
    
    from src.core.content import LessonManager
    
    if "lesson_manager" not in st.session_state:
        st.session_state.lesson_manager = LessonManager()
        
    lm = st.session_state.lesson_manager
    lessons = lm.get_lessons()
    
    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        subject = st.selectbox("Subject", list(lessons.keys()))
    with col_sel2:
        topic = st.selectbox("Topic", lessons[subject])
        
    content = lm.get_lesson_content(subject, topic)
    
    st.divider()
    st.markdown(f"## {content['title']}")
    st.markdown(content['markdown'])
    
    if content['figure']:
        # Interactive features for Calculus
        if subject == "Calculus" and topic == "Derivatives Intuition":
            x_val = st.slider("x value", -4.0, 4.0, 1.0, 0.1)
            
            # Re-generate figure based on slider (dynamic update)
            import numpy as np
            import plotly.graph_objects as go
            
            x = np.linspace(-5, 5, 100)
            y = x**2
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x) = x^2'))
            
            x0 = x_val
            y0 = x0**2
            slope = 2*x0
            y_tangent = slope * (x - x0) + y0
            
            fig.add_trace(go.Scatter(x=x, y=y_tangent, mode='lines', name=f'Tangent (Slope={slope:.1f})', line=dict(dash='dash', color='green')))
            fig.add_trace(go.Scatter(x=[x0], y=[y0], mode='markers', name='Point', marker=dict(size=12, color='red')))
            
            fig.update_layout(title=f"Derivative at x={x0}", xaxis_title="x", yaxis_title="f(x)", 
                              yaxis_range=[-5, 25])
            st.plotly_chart(fig, use_container_width=True)
            
        else:
            st.plotly_chart(content['figure'], use_container_width=True)

# --- Tab 4: Practice Arena ---
with tab4:
    st.subheader("🏋️ Practice Arena")
    st.markdown("Infinite practice problems generated on the fly.")

    # Import generator inside the app to avoid circular imports if any
    try:
        from src.core.modules.math_foundations.generator import MathGenerator
        
        if "generator" not in st.session_state:
            st.session_state.generator = MathGenerator()
        
        category = st.selectbox("Select Topic:", ["Calculus (Derivatives)", "Linear Algebra (Dot Product)"])
        
        if st.button("New Problem"):
            st.session_state.current_problem = st.session_state.generator.get_problem(category)
        
        if "current_problem" in st.session_state:
            problem = st.session_state.current_problem
            st.markdown("### Question:")
            st.latex(problem.get("question", ""))
            
            with st.expander("Show Answer"):
                st.markdown("### Answer:")
                st.latex(problem.get("answer", ""))
    except ImportError:
        st.error("Generator module not found. Check src/core/modules/math_foundations/generator.py")

# --- Tab 5: Simulation Lab ---
with tab5:
    st.subheader("🚀 Rocket Trajectory Simulator")
    st.markdown("Experiment with Physics and Calculus by launching virtual rockets.")
    
    col_config, col_plot = st.columns([1, 3])
    
    with col_config:
        st.markdown("#### Vehicle Config")
        thrust = st.slider("Engine Thrust (N)", 1000, 20000, 5000, step=500)
        fuel_mass = st.slider("Fuel Mass (kg)", 10, 200, 50, step=5)
        dry_mass = st.slider("Dry Mass (kg)", 10, 500, 100, step=10)
        burn_time = st.slider("Burn Time (s)", 1.0, 30.0, 10.0, step=0.5)
        
        launch = st.button("🔥 LAUNCH", type="primary")
        
    with col_plot:
        if launch:
            # Run Simulation
            try:
                from src.core.modules.physics.simulation import RocketSimulator
                sim = RocketSimulator(dry_mass, fuel_mass, thrust, burn_time)
                results = sim.run()
                
                # Metrics
                max_alt = results["Altitude (m)"].max()
                max_vel = results["Velocity (m/s)"].max()
                flight_time = results["Time (s)"].max()
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Apogee (Max Alt)", f"{max_alt:.1f} m")
                m2.metric("Top Speed", f"{max_vel:.1f} m/s")
                m3.metric("Flight Duration", f"{flight_time:.1f} s")
                
                # Plot
                fig = px.line(results, x="Time (s)", y=["Altitude (m)", "Velocity (m/s)"], 
                              title="Flight Telemetry", labels={"value": "Magnitude"})
                st.plotly_chart(fig, use_container_width=True)
                
            except ImportError:
                 st.error("Physics module not found. Check src/core/modules/physics/simulation.py")
        else:
             st.info("Adjust parameters and click Launch to see the flight path.")

