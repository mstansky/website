### import libraries
import numpy as np
import pandas as pd
import streamlit as st
import joblib


st.title("Financial Forecasting: Predicting the odds of bankruptcy in the S&P 500")
st.write("""
As discussed at-length in Behind the Bankruptcy Project, this is the interactive demo allowing you to explore my machine learning model predicting the individual % chance a S&P 500 member will go bankrupt in the next year.
This model, trained to identify a bankrupt company from a healthy one, ingests a S&P 500 member's financials, and based on what it learned from bankruptcies in the past decade, determines a % odds that it will go bankrupt within the next year.
""")

########################################################################################################################################################
### DATA LOADING


### A. define function to load data
@st.cache_data  # <- add decorators after trying to run the load multiple times
def load_data(path, num_rows):
    df = pd.read_csv(path, nrows=num_rows, index_col=0, converters={'CIK_number': str})
    return df


### B. Load full file
df = load_data("pages/v_one_files/Analysis_Ready_DF.csv", 539) # 539 entries in the csv


#########################################################################################################################################################

# MARK --  Create dropdown select box - input will be parsed and passed to pkl

st.subheader('Pick a company from the dropdown below to see the odds of it going bankrupt!')

option = st.selectbox("Pick your company here!", df['entity.name'], )

#st.write(f"the option chosen was: {option}")

## Open and load pickled RF model

loaded_model = joblib.load('pages/v_one_files/random_forest_model.pkl')  # Where I load in my RF model

#### Begin Prediction process......

st.subheader('Prediction')

# 1. Access my row of data, assigning it to input_data
input_data = df.loc[df['entity.name'] == option]

# 2. transform it into a numpy series
input_data = input_data.to_numpy()

# 3. drop unneeded fields
input_data = np.delete(input_data, [0, 1, 2])  # drop first 3 items

# 4. run input data through pickle
loaded_model.predict_proba(input_data.reshape(1, -1))

# 5. return prediction
prediction = loaded_model.predict(input_data[None,])
probability = loaded_model.predict_proba(input_data.reshape(1, -1))

if prediction == 1:
    st.write(
        f"Based on given financials, we predict that {option} has a {probability[0][1]:.0%} probability of going bankrupt.")
else:
    st.write(
        f"Based on given financials, we predict that {option} has a {probability[0][1]:.0%} probability of going bankrupt.")


# Make your own company!!

st.write("##")
st.write("-----------------------------------------")
st.subheader("S&P Not Enough? Enter Your Own Financials and See the Odds!")

# Splitting webpage into two columns, left will be numeric inputs for company, right will be graph visuals to show what revenue looks like
article_col1, article_col2 = st.columns(2, gap="small")

with article_col1:
    ### BEGIN MYOC FORM
    dfForm = st.form(key='dfForm')
    with dfForm:
        dfColumns = st.columns(3)
        with dfColumns[0]:
            Rev3 = st.number_input("Revenue 3 Yrs", value=15000000, placeholder=1500000)
            NI_3 = st.number_input("Net Income 3 Yrs", value=5000000, placeholder=1500000)
            st.write("-----------------------------------------")
            opcf3 = st.number_input("Operating Cash Flow 3 Yrs", value=1000000, placeholder=1000000)
            incf3 = st.number_input("Investing Cash Flow 3 Yrs", value=2000000, placeholder=2000000)
            fncf3 = st.number_input("Financing Cash Flow 3 Yrs", value=500000, placeholder=500000)
            st.write("-----------------------------------------")
            cash3 = st.number_input("Cash 3 Yrs", value=6000000, placeholder=6000000)
            assets3 = st.number_input("Asets 3 Yrs", value=10000000, placeholder=1000000)
            liab3 = st.number_input("Liabilities 3 Yrs", value=1000000, placeholder=1000000)
            eq3 = st.number_input("Equity 3 Yrs", value=9000000, placeholder=9000000)

        with dfColumns[1]:
            Rev2 = st.number_input("Revenue 2 Yrs", value=17500000, placeholder=17500000)
            NI_2 = st.number_input("Net Income 2 Yrs", value=6000000, placeholder=6000000)
            st.write("-----------------------------------------")
            opcf2 = st.number_input("Operating Cash Flow 2 Yrs", value=1200000, placeholder=1200000)
            incf2 = st.number_input("Investing Cash Flow 2 Yrs", value=500000, placeholder=500000)
            fncf2 = st.number_input("Financing Cash Flow 2 Yrs", value=900000, placeholder=900000)
            st.write("-----------------------------------------")
            cash2 = st.number_input("Cash 2 Yrs", value=500000, placeholder=500000)
            assets2 = st.number_input("Asets 2 Yrs", value=9000000, placeholder=9000000)
            liab2 = st.number_input("Liabilities 2 Yrs", value=6000000, placeholder=6000000)
            eq2 = st.number_input("Equity 2 Yrs", value=4000000, placeholder=4000000)

        with dfColumns[2]:
            Rev1 = st.number_input("Revenue 1 Yrs", value=10000000, placeholder=10000000)
            NI_1 = st.number_input("Net Income 1 Yrs", value=500000, placeholder=500000)
            st.write("-----------------------------------------")
            opcf1 = st.number_input("Operating Cash Flow 1 Yrs", value=1000000, placeholder=1000000)
            incf1 = st.number_input("Investing Cash Flow 1 Yrs", value=200000, placeholder=200000)
            fncf1 = st.number_input("Financing Cash Flow 1 Yrs", value=1500000, placeholder=1500000)
            st.write("-----------------------------------------")
            cash1 = st.number_input("Cash 1 Yrs", value=1200000, placeholder=1200000)
            assets1 = st.number_input("Asets 1 Yrs", value=7000000, placeholder=7000000)
            liab1 = st.number_input("Liabilities 1 Yrs", value=8000000, placeholder=8000000)
            eq1 = st.number_input("Equity 1 Yrs", value=-1000000, placeholder=-1000000)

        # Saving the user-submitted company as a list
        custom_company = [Rev3, NI_3, opcf3, incf3, fncf3, cash3, assets3, liab3, eq3,
                          Rev2, NI_2, opcf2, incf2, fncf2, cash2, assets2, liab2, eq2,
                          Rev1, NI_1, opcf1, incf1, fncf1, cash1, assets1, liab1, eq1
                          ]
        # putting custom co into format required for model prediction:
        custom_co_ratios = [(Rev1 / Rev2) - 1, (Rev1 / Rev3) - 1,
                            (NI_1 / NI_2) - 1, (NI_1 / NI_3) - 1,
                            (opcf1 / Rev1), (opcf2 / Rev2), (opcf3 / Rev3),
                            (incf1 / Rev1), (incf2 / Rev2), (incf3 / Rev3),
                            (fncf1 / Rev1), (fncf2 / Rev2), (fncf3 / Rev3),
                            (incf1 / opcf1), (incf2 / opcf2), (incf3 / opcf3),
                            (fncf1 / opcf1), (fncf2 / opcf2), (fncf3 / opcf3),
                            (opcf1 / opcf2) - 1, (opcf1 / opcf3) - 1,
                            (incf1 / incf2) - 1, (incf1 / incf3) - 1,
                            (fncf1 / fncf2) - 1, (fncf1 / fncf3) - 1,
                            (cash1 / Rev1), (cash2 / Rev2), (cash3 / Rev3),
                            (Rev1 / assets1), (Rev2 / assets2), (Rev3 / assets3),
                            (assets1 / liab1), (assets2 / liab2), (assets3 / liab3),
                            (cash1 / opcf1), (cash2 / opcf2), (cash3 / opcf3)]

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("processing your companys chances....")
            # Pass information through the pickle ML Model...

            # 2. transform custom company into a numpy series
            input_data2 = np.array(custom_co_ratios)

            # 4. call pickle and run input data through pickle
            loaded_model_1 = joblib.load('pages/v_one_files/random_forest_model2.pkl')
            loaded_model_1.predict_proba(input_data2.reshape(1, -1))

            # 5. return prediction
            custom_prediction = loaded_model_1.predict(input_data2[None,])
            custom_probability = loaded_model_1.predict_proba(input_data2.reshape(1, -1))

            if custom_prediction == 1:
                st.write(
                    f"Based on given financials, we predict that your company has a {custom_probability[0][1]:.0%} probability of going bankrupt. Prepare for Doom.")
            else:
                st.write(
                    f"Based on given financials, we predict that  your company has a {custom_probability[0][1]:.0%} probability of going bankrupt.")
#########

### END MYOC FORM (column 1)


# Making some easy access lists from the input section
Revenue = [Rev3, Rev2, Rev1]
Net_Income = [NI_3, NI_2, NI_1]
Operating_CashFlow = [opcf3, opcf2, opcf1]
Investing_CashFlow = [incf3, incf2, incf1]
Financing_CashFlow = [fncf3, fncf2, fncf1]
cash_balance = [cash3, cash2, cash1]
assets_amt = [assets3, assets2, assets1]
liabilities_amt = [liab3, liab2, liab1]
equity_amt = [eq3, eq2, eq1]

### BEGIN BS ITEM VISUALS
with article_col2:
    # Save chart info as np array so as to change shape for chart
    chart_information = np.array(custom_company)

    # Chart 1: Show Company Revenue and Net Income
    chart_data1 = pd.DataFrame(
        {"Revenue": np.array(Revenue),
         "Net Income": np.array(Net_Income)
         })
    # ,title = "Income Statement")
    st.area_chart(chart_data1)

    # Chart 2: Show Operating Cash Flow
    chart_data2 = pd.DataFrame({
        "Operating Cash Flow": Operating_CashFlow,
        "Investing Cash Flow": Investing_CashFlow,
        "Financing Cash Flow": Financing_CashFlow
    })
    st.area_chart(chart_data2)

    # Chart 3: Show Company Balance Sheet Inforamtion
    chart_data3 = pd.DataFrame({
        "Cash Balance": cash_balance,
        "Assets Total": assets_amt,
        "Liabilities Total": liabilities_amt,
        "Equity Total": equity_amt
    })
    st.area_chart(chart_data3)

### END CHARTS


st.write("End of page.  Hope you had fun!")


# COMMENTED OUT
##########################################################################################################################################################
# # SHOWING DATAFRAME AT BOTTOM
#
# st.write("##")
# st.write("-----------------------------------------")
# st.write("##")
#
# ### C. Display the dataframe in the app
# st.subheader('A preview of the model\'s data.')
# st.dataframe(df)
#
# ###############################