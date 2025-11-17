import streamlit as st

with st.form("data_request_form"):
    st.write("### Data Request Form")
    
    # Requester Information
    st.write("#### Requester Information")
    requester_name = st.text_input("Requester Name*")
    sub_department = st.selectbox("Requester Sub-Department*", ["LS-C", "LS-R", "LS-V", "LV", "LM", "LC"])
    requester_region = st.radio("Requester Region*", ["EU", "NA", "ASIA"], horizontal=True)
    
    # Demand Information
    st.write("#### Demand Information")
    demand_name = st.text_input("Demand Name*")
    demand_type = st.radio("Demand Type*", 
                           ["Dashboard", "Data from other department", 
                            "Data from external Data Provider", "Market Data"])
    demand_description = st.text_area("Demand Description*")
    
    # Business Case
    st.write("#### Business Case")
    why_needed = st.text_area("Why do I need this?*")
    consequences = st.text_area("What are the consequences if not implemented?*")
    use_case = st.text_area("Use Case*")
    
    # Timeline and Priority
    st.write("#### Timeline & Priority")
    go_live_date = st.date_input("Latest Go-Live Date*")
    priority = st.radio("Priority*", ["High", "Medium", "Low"], horizontal=True)
    
    # Additional Comments
    comments = st.text_input("Comments (Optional)")
    
    submitted = st.form_submit_button("Submit Request")
    
    if submitted:
        st.success(f"✅ Request submitted: {demand_name}")
        st.write("**Summary:**")
        st.write(f"- Requester: {requester_name} ({sub_department})")
        st.write(f"- Region: {requester_region}")
        st.write(f"- Demand Type: {demand_type}")
        st.write(f"- Priority: {priority}")
        st.write(f"- Target Go-Live: {go_live_date}")
