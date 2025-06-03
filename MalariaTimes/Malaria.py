import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import math as mt
from PIL import Image
import numpy as np
import csv

# functions
def Find_Cases(country_tofind):
    if country_tofind == 'None':
                pass
    else:
        year = st.selectbox("Choose year",year_list[0:])
        Index = year_list.index(year)
        if Index == 0:
            pass
        else:
            with col3:
                country_cases = countryLstDetails.get(country_tofind)
                cases = mt.ceil(float(country_cases[Index-1]))
                st.markdown(f"Around {cases} cases in {country_tofind.title()} during the year {year}.")
                fig = px.line(x=year_list[1:],y=countryLstDetails.get(country_tofind),title="22 Years data from 2010 to 2021:",)
                fig.update_layout(height=700, width = 700,xaxis_title="years",yaxis_title="Cases")
                st.plotly_chart(fig)

# 2021 census data
nan = 0
Data = open("dat.csv")
lst = csv.reader(Data)
countryLstDetails = {}
countryLstDetails["None"] = 0 
for temp in lst:
    countryLstDetails[temp[0]] = temp[1:]

# List of Menu info
# variables
year_list = ['None',2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]

# text layout vars
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

with st.sidebar:
    selected = option_menu(
    menu_title=None,
    options=["Home", "Malaria Prevention Programmes and Committees", "Data chart representor", "Documentation"],
    icons=["house", "capsule-pill", "bar-chart", "file-earmark-bar-graph"]
)

if selected == "Data chart representor":
    with col1:
        st.header("MALARIA CASES PLOTTER: ")
        country = st.selectbox("Country",countryLstDetails.keys())
        Find_Cases(country)
# UI
elif selected == "Malaria Prevention Programmes and Committees":
    st.markdown("Many committees and programs have played crucial roles in the global effort to eradicate malaria. Some of the leading organisations have been listed below:")
    st.subheader("Roll Back Malaria Partnership (RBM):",divider="rainbow")
    st.markdown("- RBM was launched in 1998 and is a global partnership aimed at coordinating action against malaria.")
    img7 = Image.open("RBM.png")
    st.image(img7)
    st.subheader("The Global Fund:",divider="rainbow")
    st.markdown("- The Global Fund, established in 2002, is a major international financing institution that supports programs to combat HIV/AIDS, tuberculosis, and malaria. It provides funding to countries to strengthen health systems and implement interventions to control and eliminate malaria.")
    img8 = Image.open("The global fund.jpg")
    st.image(img8,width=400)
    st.subheader("World Health Organization's Global Malaria Programme:",divider="rainbow")
    st.markdown("The WHO plays a central role in coordinating global efforts to control and eliminate malaria. Its Global Malaria Programme provides technical guidance, sets norms and standards, and supports countries in their efforts to combat malaria.")
    img9 = Image.open("World-Health-Organization-WHO-Symbol.png")
    st.image(img9,width=600)
    st.subheader("UNITAID:",divider="rainbow")
    st.markdown("Unitaid is a global health initiative that works with partners to bring about innovations to prevent, diagnose and treat major diseases in low- and middle-income countries, with an emphasis on tuberculosis, malaria, and HIV/AIDS and its deadly co-infections.")
    img10 = Image.open("Unitaid.png")
    st.image(img10)
    st.subheader("Malaria Reasearches from prominent Youtubers:",divider="rainbow")
    st.markdown("Many contributions towards scientific research in favour of malaria preventions have also been made by some of the most prominent youtubers/content creators. Some of them are listed below:")
    st.subheader("Mark Rober:",divider="grey")
    st.video("MarkRoberMalaria.mp4")
    st.subheader("World Health Organisation (WHO):",divider="grey")
    st.video("MALARIA.mp4")
elif selected == "Documentation":
    st.header("PROLOGUE")
    st.markdown("Two months into the making of 'Malaria times' webapp, had enlightened us developers Praveen Thenappan and Arav Goyal about creating our own websites.")
    st.markdown("The main goal behind this website is to educate the common beings about some well known organisations and committes that have been formed for eradicating malaria and also show them about what malaria is and how it affects society, so that people can take proper prevention measures to stop it from causing a worldwide pandemic.")
    
    
    st.header("REASON")
    st.markdown("Almost 22 years, after many advancements in technology and medicine, people around the world, especially in the developing countries are affected by malaria. In 2022 alone, there were 249 million cases. This especially affects children in poverty stricken conditions causing them life long illnesses and hampering for their future.")

    st.markdown("Organisations like AMP (The Alliance for Malaria Prevention) and The Global Fund organisation, etc. have invested nearly 12 billion USD in order to eradicate malaria for good.")
elif selected == "Home":
    option = option_menu("Malaria and about it",["What is Malaria?","Where is Malaria mostly found or concentrated?","How and why is Malaria caused?"])
    with col4:
        st.header("Malaria Times")
    if option == "Where is Malaria mostly found or concentrated?":
        st.title("Where is Malaria mostly found or concentrated?")
        st.markdown("Where malaria is found depends mainly on climatic factors such as temperature, humidity, and rainfall.")
        st.markdown("In many malaria-endemic countries, malaria transmission does not occur in all parts of the country. Even within tropical and subtropical areas, transmission will not occur:")
        st.markdown("- At very high altitudes;")
        st.markdown("- During colder seasons in some areas")
        st.markdown("- In deserts (excluding the oases); and")
        st.markdown("- In some countries where transmission has been interrupted through successful control/elimination programs.")
        st.markdown("Generally, in warmer regions closer to the equator:")
        st.markdown("- Transmission will be more intense, and")
        st.markdown("- Malaria is transmitted year-round.")
        img = Image.open("MalariaEndemicity_2020.jpg")
        st.image(img)
        
        st.markdown("At cold temperatures (below 20 degree celsius) the Plasmodium falciparum (which causes severe malaria) cannot complete its growth cycle in anopheles mosquito and hence cannot be transmitted.")
        st.subheader("Plasmodium Falciparum")
        img1 = Image.open("Plasmodium_falciparum.png")
        st.image(img1)

        st.markdown("Malaria is transmitted in tropical and subtropical areas, where: ")
        st.markdown("- Anopheles mosquitoes can survive and multiply") 
        st.markdown("- and Malaria parasites can complete their growth cycle in the mosquitoes (extrinsic incubation period)")
        st.subheader("extrinsic incubation period".title())
        img2 = Image.open("Extrensic_incubation_period.jpg")
        st.image(img2)
    elif option == "What is Malaria?":
        st.title("What is Malaria?")
        st.markdown("Malaria is a disease caused by a parasite. The parasite is spread to humans through the bites of infected mosquitoes. People who have malaria usually feel very sick with a high fever and shaking chills.")
        img3 = Image.open("malaria.jpg")
        st.image(img3,width=350)
        st.markdown("Infection with malaria parasites may result in a wide variety of symptoms, ranging from absent or very mild symptoms to severe disease and even death.")
        st.markdown("While the disease is uncommon in temperate climates, malaria is still common in tropical and subtropical countries. Each year nearly 290 million people are infected with malaria, and more than 400,000 people die of the disease.")
        st.markdown("To reduce malaria infections, world health programs distribute preventive drugs and insecticide-treated bed nets to protect people from mosquito bites. The World Health Organization has recommended a malaria vaccine for use in children who live in countries with high numbers of malaria cases.")
        img4 = Image.open("AntimalarialDrugs.jpg")
        img5 = Image.open("insectisideTreatedNets.jpg")
        st.image(img4)
        st.image(img5)
    elif option == "How and why is Malaria caused?":
        st.title("How and why is Malaria caused?")
        st.markdown("Most people get malaria when bitten by a mosquito infected with the malaria parasite. Only female Anopheles mosquitoes can spread malaria. For the Anopheles mosquito to become infected, they must bite, or take a blood meal, from a person with the malaria parasites. About one week later, the mosquito will inject the parasites via her saliva into the next person she bites. And the cycle of infection continues.")
        st.subheader("Dengue feed cycle")
        img6 = Image.open("DengueCycle.jpg")
        st.image(img6)

        st.markdown("On some sitations, Malaria can spread by blood transfusion, using syringes with may have malaria infected blood,etc.")
        st.markdown("Anyone can get malaria. Most cases occur in people who live in countries with widespread malaria. People from countries with no malaria can become infected when they travel to countries with malaria.")

# myConnector.close()                 # clean up enviorment