"""
You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.
"""
# import pandas and numpy
#  define a dataset
import pandas as pd,numpy as np
def dataset(dataset1,dataset2):
    # merge both csv files with a key common to both (NAME)
    # Filter the LEG_LENGTH & STRIDE_LENGTH and store them as arrays using the numpy function np.array()
    # calculate the speed with the formula given
    Merged_Data=dataset1.merge(dataset2,on='NAME')
    LEG_LENGTH=np.array(Merged_Data['LEG_LENGTH'])
    STRIDE_LENGTH=np.array(Merged_Data['STRIDE_LENGTH'])
    g=9.8
    speed =((STRIDE_LENGTH/LEG_LENGTH)-1) * np.sqrt(LEG_LENGTH * g)

    # create an empty dictionary(Speed_Dict) with a key 'SPEED' and assign all values of speed to it
    # call the pandas DataFrame ()function to create a dataframe from the dictionary
    Speed_Dict=pd.DataFrame({})
    Speed_Dict['SPEED']=speed

    #use the pandas concatenate() function to concatenate(merged_data and Speed_Dict) into Final_Data
    # call the sort function to sort Final_data in descending order by passing column key(speed)
    Final_Data=pd.concat([Merged_Data,Speed_Dict],axis=1).reindex(Speed_Dict.index)
    Final_Data.sort_values(['SPEED'],ascending=False, inplace=True)

    # loop through the rows of the Final_Data
    # if bipedal exist for column key(STANCE)
    # print names of dinasaurs with bipedal in the stance column
    print('\n NAMES OF BIPEDAL DINASAURS FROM FASTEST TO SLOWEST')
    for index,column in Final_Data.iterrows():
        if column['STANCE']=='bipedal':
            print('{}'.format(column['NAME']))
 
# read the csv files with pandas read_csv() function
# call the function dataset on the csv files to execute the code.
dataset(pd.read_csv('dataset1.csv'),pd.read_csv('dataset2.csv'))


