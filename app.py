
import pickle
import streamlit as st
import pandas as pd
import numpy as np

classifier = pickle.load(open('final_pipeline.pkl','rb'))

st.set_page_config(page_title = 'Customer Analysis Web App', layout='centered')
st.title('Customer Analysis Web App')

def segment_customers(input_data):
    
    prediction=classifier.predict(pd.DataFrame(input_data, columns=['Income','Kidhome','Teenhome','Age','Partner','Education_Level']))
    print(prediction)
    pred_1 = 0
    if prediction == 0:
            pred_1 = '--cluster 0-- ' + \
                        "Promotion acceptance will be rare and "+ \
                        "Very few complete purchases will be using discounts"

    elif prediction == 1:
            pred_1 = '--cluster 1-- ' + \
                        " Promotion acceptance ratio is 0.5 and " + \
                        "Completing purchases using discounts will be rare"

    elif prediction == 2:
            pred_1 = '--cluster 2-- ' + \
                        "Promotion acceptance ratio is poor and " + \
                        "Will be highly interested in completing purchases using discounts"

    elif prediction == 3:
            pred_1 = '--cluster 3-- ' + \
                        "Promotion acceptance is rare and " + \
                        "Will be highly interested in completing purchases using discounts"

    return pred_1

def main():
    
    Income = st.text_input("Type In The Household Income")
    Kidhome = st.radio ( "Select Number Of Kids In Household", ('0', '1','2') )
    Teenhome = st.radio ( "Select Number Of Teens In Household", ('0', '1','2') )
    Age = st.slider ( "Select Age", 18 , 85 )
    Partner = st.radio ( "Livig With Partner?", ('Yes', 'No') )
    Education_Level = st.radio ( "Select Education", ("Undergraduate", "Graduate", "Postgraduate") )
    
    result = ""

    if st.button("Segment Customer"):
        result=segment_customers([[Income,Kidhome,Teenhome,Age,Partner,Education_Level]])
    
    st.success(result)
    

if __name__ == '__main__':
        main ()
        
