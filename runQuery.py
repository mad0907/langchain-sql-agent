from testquery import run_query_df, run_query_json

# q = "Top 5 cities with highest revenue last month"
# q = "Top 5 product categories with highest sales"
# q = "Top 10 customers who spent the most in the last 3 months"
q = "Cities with the highest number of orders"

df = run_query_df(q)
print(df)

json_data = run_query_json(q)
print(json_data)
