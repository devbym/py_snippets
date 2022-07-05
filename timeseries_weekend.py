import pandas


def main():
  yr = input("year?")
  return create_timeseries_with_weekend_only(yr)



def create_timeseries_year_with_weekend_only(year:int):
    all_dates = pd.date_range(str(year),freq="D",periods=365).to_series()
    return pd.Series(all_dates.index.weekday >= 5, index=all_dates)
  
  
  
if __name__ == "__main__":
  main()
  
