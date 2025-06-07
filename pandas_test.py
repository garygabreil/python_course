# Pandas can read csv, excel, json
# basic dataFrame opertaions
# head - First 5 rows
# tail - last 5 rows
# shape - (rows, colums)
# colums - just tells the column names
# dtypes - data type
# info - overall summary

import pandas as pd
data = {
    'name' : ['Ram','Jos','Bob', 'Kumar', 'Sagar', 'Adhi', 'John', 'Rachin','ABD', 'Hendrick','Vijay'],
    'age': [24,20,19,8,11,44,8,10,21,16,55]
}
df = pd.DataFrame(data)
# print(df.columns)

# print(df[['age','name']])


# print(df['age'] > 10)
print(df[df['age'] < 10])


print()


#data resides in snowflake
#python used for visulization


#oralce
# 100 tables - do you need the 100 tables?

#timeSeries DB (TSDB) - InfluxDB, Prometheus, 
# timestamped data: metric, logs, sensor
# high-volume inserts, time based queries
# performance - High

#RDBMS, Oracle, SQL, - Structured
# transactional data - row
# DML - Data manipulation
# performance - Low


#No Structuted - MongoDB, Cassandanra


