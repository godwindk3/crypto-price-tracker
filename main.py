from src.extract.coingecko_api import run_extract, save_raw_data
from src.load.load_raw_data import load_raw_data
from src.transform.transform_data import transform_data, save_processed_data

def main():
    #1 Extract
    run_extract()

    #2 Load
    df = load_raw_data()

    #3 Transform

    df_transformed = transform_data(df)
    save_processed_data(df_transformed)

if __name__ == "__main__":
    main()


