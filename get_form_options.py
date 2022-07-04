# Get customers who have had >75 SEMS. This is arbitrary and chosen for performance and usability
# To include all customers remove lambda or reduce threshold
# This function is used to populate customer multiselect widget in the additional parameter section
def get_top_customers(df):
    return (list(df["Sold-To ID"].value_counts().loc[lambda x: x>75].index))

# Get carriers who have had >40 SEMS. This is arbitrary and chosen for performance and usability
# To include all carriers remove lambda or reduce threshold
# This function is used to populate carrier multiselect widget in the additional parameter section

def get_top_carriers(df):
    return (list(df["Carrier"].value_counts().loc[lambda x: x>40].index))

# Get all teams who have had >30 SEMS. This is arbitrary and chosen for performance and usability
def get_top_created(df):
   return (list(df["Created by Team Name"].value_counts().loc[lambda x: x>30].index))


def get_sales_regions(df):
    return list(df["Sales Region"].unique()) # list of unique regions


def get_sem_status(df):
    return list(df["SEM Status"].unique()) # list of unique sem status

def get_assigned(df):
    return list(df["Assigned To Team"].unique()) # list of unique assigned teams


def get_top_sub_issue(df):
   return (list(df["SEM Sub issue Type"].value_counts().loc[lambda x: x>10].index)) # list of unique sub issues

