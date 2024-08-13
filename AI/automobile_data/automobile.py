import pandas as pd

df = pd.read_csv('Automobile_data.csv')

max_val = df.loc[df['average-mileage'].idxmax()]
print( "The company with max average mileage is : ",max_val['company'], " having mileage of : ", df['average-mileage'].max())

#print("Max avg. mileage : ",df['average-mileage'].max())
#print(df.shape)
