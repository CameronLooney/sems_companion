import pandas as pd


def modify_day_age(df):
    # replacd "-" with 0 to allow us to perform calculations
    df["Modified Age [Days]"] = df["Modified Age [Days]"].replace("-", "0")
    # convert action age and modiffied age to integers, round to nearest integer
    df["Action Age [Days]"] = df["Action Age [Days]"].astype(float).round(0)
    df["Modified Age [Days]"] = df["Modified Age [Days]"].astype(float).round(0)
    return df

def sem_category_three_chosen(df):
    return df
def sem_category_one_two_chosen(df,sem_list):

    if "AOU SEMS" not in sem_list: # if AOU SEMS is not chosen
        df = df[df["CAT"] != "AOU"] # remove all AOU SEMS

    if "C2C SEMS" not in sem_list: # if C2C SEMS is not chosen
        df = df[~df["Created by Team Name"].str.contains("CSS CRU", na=False)] # remove all C2C SEMS
        df = df[~df["Created by Team Name"].str.contains("C2C", na=False)]
        df = df[~df["Assigned To Team"].str.contains("C2C", na=False)]

    if "RMA SEMS" not in sem_list: # if RMA SEMS is not chosen
        df = df[~df["Created by Team Name"].str.contains("RMA",na=False)] # remove all RMA SEMS
        df = df[~df["Carrier"].str.contains("RMA", na=False)]
        df = df[~df["Assigned To Team"].str.contains("RMA", na=False)]
    return df

def sem_category_none_chosen(df):
    # if no additional sems are chosen then remove anything related to RMA, C2C and AOU
    df = df[~df["Created by Team Name"].str.contains("RMA", na=False)]
    df = df[~df["Carrier"].str.contains("RMA", na=False)]
    df = df[~df["Assigned To Team"].str.contains("RMA", na=False)]
    df = df[~df["Created by Team Name"].str.contains("CSS CRU", na=False)]
    df = df[~df["Created by Team Name"].str.contains("C2C", na=False)]
    df = df[~df["Assigned To Team"].str.contains("C2C", na=False)]
    df = df[~df["CAT"].str.contains("AOU", na=False)]
    return df

def filter_dates(df, start_date, end_date):
    df = df[df["Created On"].between(start_date, end_date)] # filter by created on date
    return df

def filter_regions(df, chosen_regions):
    if len(chosen_regions) > 0: # if there are regions chosen
        df = df[df["Sales Region"].isin(chosen_regions)] # filter by chosen regions
    return df

def filter_customers(df, chosen_customers):
    if len(chosen_customers) > 0: # if there are customers chosen
        df = df[df['Sold-To ID'].isin(chosen_customers)] # filter by chosen customers
    return df


def filter_carriers(df, chosen_carriers):
    if len(chosen_carriers) > 0: # if there are carriers chosen
        df = df[df["Carrier"].isin(chosen_carriers)] # filter by chosen carriers
    return df

def filter_sem_status(df, chosen_sem_status):
    if len(chosen_sem_status) > 0: # if there are sem statuses chosen
        df = df[df["SEM Status"].isin(chosen_sem_status)] # filter by chosen sem statuses
    return df

def filter_created(df, chosen_created):
    if len(chosen_created) > 0: # if there are created by chosen
        df = df[df["Created by Team Name"].isin(chosen_created)] # filter by chosen created by
    return df

def filter_assigned(df, chosen_assigned):
    if len(chosen_assigned) > 0: # if there are assigned to chosen
        df = df[df["Assigned To Team"].isin(chosen_assigned)] # filter by chosen assigned to
    return df

def filter_priority(df, chosen_priority):
    if len(chosen_priority) > 0: # if there are priorities chosen
        df = df[df["Priority"].isin(chosen_priority)] # filter by chosen priorities
    return df

def filter_sub_issue(df, chosen_sem_sub_issue):
    if len(chosen_sem_sub_issue) > 0:# if there are sub issues chosen
        df = df[df["SEM Sub issue Type"].isin(chosen_sem_sub_issue)] # filter by chosen sub issues
    return df


