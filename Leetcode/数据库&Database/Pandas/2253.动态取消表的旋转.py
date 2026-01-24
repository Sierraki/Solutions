import pandas as pd


def find_valid_users(products: pd.DataFrame) -> pd.DataFrame:
    return (
        pd.melt(
            products,
            id_vars="product_id",
            value_vars=list(products.columns)[1:],
            value_name="price",
        )
        .dropna()
        .rename(columns={"variable": "store"})
    )
