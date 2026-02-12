import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page Config
st.set_page_config(page_title="Math Foundations Tracker", layout="wide")

# File Path
CSV_FILE = "dashboard.csv"

def load_data():
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame(columns=["Week", "Track", "Module", "Topic", "Planned Hours", "Status", "Output Lab"])
    df = pd.read_csv(CSV_FILE)
    # Ensure Link column is string (not float NaN) to avoid Streamlit errors
    df["Output Lab"] = df["Output Lab"].fillna("")
    return df

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

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

# --- Visualizations ---
st.divider()

tab1, tab2 = st.tabs(["Analytics", "Scratchpad"])

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
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=600,
        width=800,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Do something interesting with the image data
    if canvas_result.image_data is not None:
        if st.button("Save to Notes"):
            # Ensure notes directory exists
            if not os.path.exists("notes"):
                os.makedirs("notes")
            
            # Save image
            img_data = canvas_result.image_data
            im = Image.fromarray(img_data.astype("uint8"), mode="RGBA")
            
            # Generate filename with timestamp
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"notes/note_{timestamp}.png"
            im.save(filename, "PNG")
            st.success(f"Saved to {filename}!")
            
    # Show saved notes
    if os.path.exists("notes"):
        st.divider()
        st.subheader("Saved Notes")
        note_files = sorted(os.listdir("notes"), reverse=True)
        if note_files:
            selected_note = st.selectbox("View Note:", note_files)
            if selected_note:
                st.image(f"notes/{selected_note}", caption=selected_note)

