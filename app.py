# import packages
import streamlit as st
import pandas as pd
from datetime import date,timedelta
from Form import *
from get_form_options import *
from filter import *
from excel_functions import *

# Create an instance of the app
st.title("SEMS Dashboard Companion App")
st.sidebar.write("""
    
            ## Instructions\n 
            - Upload SEMS automated email excel file 
            - Set your parameters
            - Download output \n""")



    # Need to uploads to generate Open Orders, one is a helper file which is used for computation and feedback.
    # The master is the file downloaded from FrontEnd each day

sems_upload = st.file_uploader("Upload SEMS File", type="xlsx")

if sems_upload is not None:

    df = pd.read_excel(sems_upload, sheet_name=3, engine="openpyxl", dtype={'Action Age [Days]': str,"Modified Age [Days]": str})

    df = modify_day_age(df)
    st.sidebar.markdown("## Data Filter Parameters")
    col1, col2, col3 = st.columns([3, 6, 1])

    with col1:
        st.sidebar.write("")

    with col2:
        st.sidebar.image("./filter.png")

    with col3:
        st.sidebar.write("")



    with st.sidebar.form(key='my_form_to_submit'):

        # set dates
        start_date = start_data_date()
        end_date = end_data_date()

        # sem category
        sem_category = pick_sem_category()
        # get regions
        region_options = get_sales_regions(df)
        chosen_regions = sales_region_unique(region_options)

        # get customers
        customer_options = get_top_customers(df)
        chosen_customers = customer_unique(customer_options)
        # get carriers
        carrier_options = get_top_carriers(df)
        chosen_carriers = carrier_unique(carrier_options)

        # get sem status
        sem_status_options = get_sem_status(df)
        chosen_sem_status = sem_status_unique(sem_status_options)

        # team created by
        created_options = get_top_created(df)
        chosen_created = created_unique(created_options)

        # get assigned to team
        assigned_options = get_assigned(df)
        chosen_assigned = assigned_to_team_unique(assigned_options)

        # priority
        chosen_priority = pick_priority_category()

        # sub issue
        sub_issue_options = get_top_sub_issue(df)
        chosen_sub_issue = sub_issue_unique(sub_issue_options)



        submit_button = st.form_submit_button(label='Generate Excel File')
    if submit_button:

        def category_filter(df,sem_category):
            if len(sem_category)==3:
                return sem_category_three_chosen(df)

            if len(sem_category)==2 or len(sem_category)==1:
                return sem_category_one_two_chosen(df,sem_category)

            if len(sem_category)==0:
                return sem_category_none_chosen(df)



        df = category_filter(df,sem_category)

        # APPLY FILTERS
        df = filter_dates(df, start_date, end_date)
        df = filter_regions(df, chosen_regions)
        df = filter_customers(df, chosen_customers)
        df = filter_carriers(df, chosen_carriers)
        df = filter_sem_status(df, chosen_sem_status)
        df = filter_created(df, chosen_created)
        df = filter_assigned(df, chosen_assigned)
        df = filter_priority(df, chosen_priority)
        df = filter_sub_issue(df, chosen_sub_issue)


        if df.shape[0]==0:
            st.error("No SEMS found for the selected parameters")
        else:
            st.success("{} SEMS found for the selected parameters".format(df.shape[0]))
            to_excel = excel(df)
            download(to_excel)














