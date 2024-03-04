import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt
sns.set(style='dark')

# Membaca data
st.subheader("DataSet")
day_df = pd.read_csv("all_data_1.csv")
day_df


# # Mengganti nama kolom
# day_df.rename(columns={
#     'dteday': 'dateday',
#     'yr': 'year',
#     'mnth': 'month',
#     'weathersit': 'weather_situation',
#     'cnt': 'count'
# }, inplace=True)

# # Membuat dictionary untuk membaca nilai season
# season_dict = {
#     '1': 'spring',
#     '2': 'summer',
#     '3': 'autumn',
#     '4': 'winter'
# }
# day_df['season'] = day_df['season'].astype(str).map(season_dict)

# # Membuat dictionary untuk membaca nilai weather situation
# weather_situation_dict = {
#     '1': 'Clear',
#     '2': 'Broken clouds',
#     '3': 'Scattered clouds',
# }
# day_df['weather_situation'] = day_df['weather_situation'].astype(str).map(weather_situation_dict)

# # Membuat dictionary untuk membaca nilai month
# month_dict = {
#     '1': 'January',
#     '2': 'February',
#     '3': 'March',
#     '4': 'April',
#     '5': 'May',
#     '6': 'June',
#     '7': 'July',
#     '8': 'August',
#     '9': 'September',
#     '10': 'October',
#     '11': 'November',
#     '12': 'December'
# }
# day_df['month'] = day_df['month'].astype(str).map(month_dict)

# # Membuat dictionary untuk membaca nilai weekday
# weekday_dict = {
#     '0': 'Sunday',
#     '1': 'Monday',
#     '2': 'Tuesday',
#     '3': 'Wednesday',
#     '4': 'Thursday',
#     '5': 'Friday',
#     '6': 'Saturday'
# }
# day_df['weekday'] = day_df['weekday'].astype(str).map(weekday_dict)




with st.sidebar:
    st.title("Panji Nugraha Adhi")
    st.image('pasfoto.jpg')
    st.subheader("Email     : panji.na19@gmail.com")
    st.subheader("GitHub    : https://github.com/NJYY99")
    st.subheader("Linkedn   : https://www.linkedin.com/in/panji-nugraha-adhi-0b00b422b/")


def load_data():
    data_df = pd.read_csv("all_data_1.csv")
    return data_df



def main():
    # Load data
    weekly_data = load_data()

    # Univariate visualization
    avg_cnt_by_season = weekly_data.groupby('season')['cnt'].mean().reset_index()
    chart = alt.Chart(avg_cnt_by_season).mark_bar().encode(
        x=alt.X('season:N', title='', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('cnt:Q', title='Average Weekly Demand'),
    ).properties(
        width=600,
        height=400
    )

    st.subheader('Average Rentals by Season')
    st.write(chart)

    # Tambahkan pemanggilan fungsi total_rides_per_month di sini
    st.subheader('Total Rides in Month/Year')
    total_rides_per_month()
    # Multivariate Visualization
    st.subheader('Average Rentals by Weekday and Working Day')
    analyze_rental_pattern(weekly_data)
    
    st.subheader('Average Rentals by Season and Working Day')
    multivariate_visualizations1(weekly_data)

    st.subheader('Average Rentals by Weather Situation and Working Day')
    multivariate_visualizations2(weekly_data)

    
    multivariate_visualizations3(weekly_data)
    
    # CONCLUSION
    #1
    st.subheader('CONCLUSION')
    st.write('Question 1: In what month did bike riding get the most orders during the first year?')
    st.write('The month where bike sharing received the most orders in the first years was September')
    #2
    st.write('Question 2: What are the seasonal patterns in bicycle rentals?')
    st.write('from the data we get, starting from spring season until autumn season(peak) more and more people do bike sharing until finally it decreases starting in winter')
    #3
    st.write('Question 3: Is there a pattern for renting bicycles based on days of the week or holidays?')
    st.write('From the data we can see that, on holidays including weekends, Wednesday is the day where most people do bike sharing, while on weekdays, the data shows a fairly stable value of around 4000-5000 people from Monday to Friday')
    
    
    
    
    
def total_rides_per_month():
    day_df = load_data()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='mnth', y='cnt', data=day_df, hue='yr', ax=ax)
    plt.xlabel("Month")
    plt.ylabel("Total Rides")
    plt.title("Total of bikeshare rides per Month")
    st.pyplot(fig)

def analyze_rental_pattern(day_df):
    avg_rentals = day_df.groupby(['weekday', 'workingday'])['cnt'].mean().reset_index()
    avg_rentals['weekday'] = avg_rentals['weekday'].map({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'})

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weekday', y='cnt', hue='workingday', data=avg_rentals, estimator='mean', ax=ax)
    ax.set_title('Average Rentals by Weekday and Working Day')
    ax.set_xlabel('')
    ax.set_ylabel('Average Count of Rentals')
    ax.legend(title='Working Day', labels=['Holiday', 'Working Day'])
    ax.set_xticklabels(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], rotation=45)

    st.pyplot(fig)

def multivariate_visualizations1(day_df):
    # Multivariate Visualization 1
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', hue='workingday', data=day_df, ax=ax)
    ax.set_title('Average Rentals by Season and Working Day')
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Count of Rentals')
    ax.legend(title='Working Day', labels=['No', 'Yes'])
    st.pyplot(fig)

def multivariate_visualizations2(day_df):
    # Multivariate Visualization 2
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', hue='workingday', data=day_df, ax=ax)
    ax.set_title('Average Rentals by Weather Situation and Working Day')
    ax.set_xlabel('Weather Situation')
    ax.set_ylabel('Average Count of Rentals')
    ax.legend(title='Working Day', labels=['No', 'Yes'])
    st.pyplot(fig)

def multivariate_visualizations3(day_df):
    # Multivariate Visualization 3
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', hue='weathersit', data=day_df, ax=ax)
    ax.set_title('Average Rentals by Season and Weather Situation')
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Count of Rentals')
    ax.legend(title='Weather Situation')
    st.pyplot(fig)
    

if __name__ == "__main__":
    main()




