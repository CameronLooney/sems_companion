import streamlit as st
from datetime import date,timedelta
def start_data_date():
    start_date = st.date_input('Start Date', value=(date.today() - timedelta(30))) #default to 30 days ago
    start_date = str(start_date) #convert to string
    return start_date

def end_data_date():
    end = st.date_input('End Date', value=date.today()) #default to today
    end_date = str(end) #convert to string
    return end_date


def sales_region_unique(unique_region_list):
    # filter to select only regions that have been selected
    customers = st.multiselect(
        "Pick which Sales Regions to include",
        unique_region_list,
        [])
    return customers


def customer_unique(unique_customer_list):
    # filter to select only customers that have been selected
    customers = st.multiselect(
        "Pick which customers to include",
        unique_customer_list,
        [])
    return customers


def carrier_unique(unique_carrier_list):
    # filter to select only carriers that have been selected
    carrier = st.multiselect(
        "Pick which carrier's to include",
        unique_carrier_list,
        [])
    return carrier

def created_unique(unique_created_list):

    createdby= st.multiselect(
        "Pick which team created the SEMS to include",
        unique_created_list,
        [])
    return createdby

def pick_sem_category():
    #
    customers = st.multiselect(
        "Pick which additional SEM Types to include",
        ["RMA SEMS", "C2C SEMS", "AOU SEMS"],
        [])
    return customers


def sem_status_unique(unique_sem_status_list):
    status = st.multiselect(
        "Pick which SEM status to include",
        unique_sem_status_list,
        [])
    return status

def assigned_to_team_unique(unique_assigned_to_team_list):
    assigned = st.multiselect(
        "Pick which assigned to team to include",
        unique_assigned_to_team_list,
        [])
    return assigned

def pick_priority_category():
    customers = st.multiselect(
        "Pick which Priority to include",
        ["P1","P2"],
        [])
    return customers

def sub_issue_unique(unique_sub_issue_list):
    assigned = st.multiselect(
        "Pick which SEMS sub issue's to include",
        unique_sub_issue_list,
        [])
    return assigned