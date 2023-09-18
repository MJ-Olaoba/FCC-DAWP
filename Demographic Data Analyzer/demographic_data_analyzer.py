import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_array = np.array(df['race'])
    No_Each_Race = pd.Series(np.unique(race_array, return_counts=True))
    Races = No_Each_Race[0]
    No = No_Each_Race[1]
    race_count = pd.Series(No, index=Races)

    # What is the average age of men?
    Sex = df['sex'].values
    Age = df['age'].values
    Men_AgeDf = pd.DataFrame({'Sex': Sex, 'Age': Age}, index=Sex)
    Men_AgeDf_filt = Men_AgeDf.loc[Men_AgeDf.Sex == 'Male', ['Sex', 'Age']]
    Men_AgeArray = np.array(Men_AgeDf_filt['Age'])
    average_age_men = np.mean(Men_AgeArray)

    # What is the percentage of people who have a Bachelor's degree?
    Education_filt = df.loc[df['education'] == 'Bachelors', 'education']
    percentage_bachelors = round((len(Education_filt)/len(df))*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    Edu = np.array(df['education'])
    ad_deg = pd.Series(np.unique(Edu, return_counts=True))
    deg = ad_deg[0]
    deg_num = ad_deg[1]
    ad_deg2 = pd.Series(deg_num, index=deg)
    num_ad_deg = ad_deg2['Bachelors'] + ad_deg2['Masters'] +       ad_deg2['Doctorate']
    num_wout_ad_deg = len(df) - num_ad_deg
    higher_education = num_ad_deg
    lower_education = num_wout_ad_deg

    # percentage with salary >50K
    Education = df['education'].values
    Salary = df['salary'].values

    Salary_df = pd.DataFrame({'Salary': Salary, 'Education': Education})
    Salary_df2 = Salary_df[Salary_df['Education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    Salary_df3 = Salary_df2[Salary_df2['Salary'].isin(['>50K'])]
    higher_edu_rich = round(((len(Salary_df3))*100)/(num_ad_deg), 1)
    Salary_df4 = Salary_df[Salary_df['Salary'].isin(['>50K'])]
    Salary_df5 = Salary_df4[~Salary_df4['Education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu_rich = round(((len(Salary_df5))*100)/(num_wout_ad_deg), 1)
    higher_education_rich = higher_edu_rich
    lower_education_rich = lower_edu_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    work_hours = np.array(df['hours-per-week'])
    min_work_hours = np.min(work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    wk_hrs = df['hours-per-week'].values
    SalMin_df = pd.DataFrame({'Salary': Salary, 'Work Hours': wk_hrs})
    SalMin_df2 = SalMin_df[SalMin_df['Work Hours'].isin([1])]
    SalMin_df3 = SalMin_df2[SalMin_df2['Work Hours'].isin([1])]
    SalMin_df4 = SalMin_df3[SalMin_df3['Salary'].isin(['>50K'])]
    num_min_workers = SalMin_df4
    rich_percentage = round(((len(SalMin_df4)*100)/(len(SalMin_df3))), 1)

    # What country has the highest percentage of people that earn >50K?
    #Country = df['native-country'].values
    #SalCo_df = pd.DataFrame({'Salary': Salary, 'Country': Country})
    #SalCo_df2 = SalCo_df[SalCo_df['Salary'].isin(['>50K'])]
    #SalCo_Arr2 = np.array(SalCo_df2['Country'])
    #SalCo_S2 = pd.Series(np.unique(SalCo_Arr2, return_counts=True))
    #Coun = SalCo_S2[0]
    #num_coun = SalCo_S2[1]
    #SalCo_S3 = pd.Series(num_coun, index=Coun)
    #SalCo_df3 = SalCo_S3.to_frame()
    #highest_50K_Earners = SalCo_df3.max()
    #highest_50K_Country = SalCo_df3.idxmax()
    highest_earning_country = df.groupby('native-country')['salary'].value_counts(normalize=True).loc[:, ('>50K)'].idxmax()
    highest_earning_country_percentage = round(df.groupby('native-country')['salary'].value_counts(normalize=True).loc[:, ('>50K')].max()*100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    Occupation = df['occupation'].values
    sal_co_occ = {'Salary': Salary, 'Country': Country, 'Occupation': Occupation}
    Pop_OCC = pd.DataFrame(sal_co_occ)
    Pop_OCC2 = Pop_OCC[Pop_OCC['Country'].isin(['India'])]
    Pop_OCC3 = Pop_OCC2[Pop_OCC2['Salary'].isin(['>50K'])]
    Pop_OCC4 = pd.DataFrame(Pop_OCC3['Occupation'].value_counts())
    max_occ = Pop_OCC4['Occupation'].idxmax()
    top_IN_occupation = max_occ

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
