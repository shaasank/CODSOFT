import pandas as pd

data = pd.read_csv("D:\\content filtering\\merge_dataset.csv")

def get_best_movie_by_year_interactive(df: pd.DataFrame) -> None:
    #get best movie of the year
    while True:
        try:
            year = int(input("Enter the year <=2005 to find the best movie (or Enter 'exit' to quit): "))
        except ValueError:
            print("Invalid!.Please enter a valid year.")
            continue

        if year == 'exit':
            break

        # Filter the DataFrame for the specified year
        year_df = df[df['Year'] == year]

        if year_df.empty:
            print(f"No movies found for the year {year}.")
            continue

        # Find the best movie based on ratings
        best_movie = year_df.loc[year_df['Rating'].idxmax()]

        print(f"\nThe best movie of {year} based on ratings:\n", best_movie[['Movie_Name', 'Rating']])
        
#calling the function
get_best_movie_by_year_interactive(data)
