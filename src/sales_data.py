from faker import Faker
from faker.providers import internet, python
import pandas as pd
import numpy as np

faker = Faker(['en_US', 'en_AU', 'en_NZ'])
faker.add_provider(internet)
faker.add_provider(python)
# set see
Faker.seed(0)


def fake_df_from_column_definition(column_definition:dict, num_rows:int = 10):
    df = pd.DataFrame(columns = column_definition.keys())
    for i in range(num_rows):
        computed_dict = {}
        for column in column_definition.keys():
            computed_dict[column] = column_definition[column]()
        df.loc[i] = computed_dict
    return df

branch_df_column_definition  = {
    "branch_name": faker.city,
    "branch_address": faker.address,
    "manager_name": faker.name,
    "phone_number": faker.phone_number,
}

num_branches = 10

branch_df = fake_df_from_column_definition(branch_df_column_definition, num_branches)

sales_rep_df_column_definition  = {
    "sales_rep_name": faker.name,
    "sales_rep_id": faker.unique.pyint,
    "branch_name": lambda: branch_df.sample()["branch_name"].values[0],
}

num_sales_reps = 100

sales_rep_df = fake_df_from_column_definition(sales_rep_df_column_definition, num_sales_reps)


num_products = 100

product_df_column_definition  = {
    "product_id": faker.unique.pyint,
    "product_price": lambda: faker.pyfloat(left_digits=2, right_digits=2, positive=True),
    "product_expiry_date": lambda: faker.date_between(start_date='+1m', end_date='+2y'),
}

product_df = fake_df_from_column_definition(product_df_column_definition, num_products)


num_customers = 1000

customer_df_column_definition  = {
    "customer_id": faker.unique.pyint,
    "customer_name": faker.name,
    "customer_email": faker.email,
    "customer_phone_number": faker.phone_number,
}

customer_df = fake_df_from_column_definition(customer_df_column_definition, num_customers)

num_sales_data = 10000

sales_data_df_column_definition  = {
    "sales_id": faker.unique.pyint,
    "sales_rep_id": lambda: sales_rep_df.sample()["sales_rep_id"].values[0],
    "customer_id": lambda: customer_df.sample()["customer_id"].values[0],
    "product_id": lambda: product_df.sample()["product_id"].values[0],
    "quantity": lambda: faker.pyint(min_value=1, max_value=10),
    "date_of_sale": lambda: faker.date_between(start_date='-1y', end_date='today'),
}

sales_data_df = fake_df_from_column_definition(sales_data_df_column_definition, num_sales_data)

