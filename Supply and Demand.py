import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

    # on both tables 
    #   x = quantity
    #   y = price
    #   (x,y) table points

####################################################
# Input your imperical data into the variables;    #
# quantity/priceDemanded, and quantity/priceSupply #
#                                                  #
#                     #Below#                      #
####################################################


###Input META data here###
quantityDemanded = [82, 423]
priceDemanded = [1100, 875]

quantitySupplied = [0, 423]
priceSupply = [340, 875]


    #predicted values
predictedDemandQuantity = []
predictedDemandPrice = []

predictedSupplyQuantity = []
predictedSupplyPrice = []


    #Linear equation for supply and demand lines,
    #Key:Value = {y-intercept: b, slope: m}
demandLine = {}
supplyLine = {}



"""
#Demand by location/Type
amsterdam_demand_rec = 6830
rio_demand_rec = 4978

total_rec_demand = amsterdam_demand_rec + rio_demand_rec
#print(total_rec_demand)

amsterdam_demand_speed = 4415
rio_demand_speed = 2304

total_speed_demand = amsterdam_demand_speed + rio_demand_rec
#print(total_speed_demand)
"""



    #linear equation (y = mx + b)
    #
def linearEquation(x,y):
    #find slope (m)
    m = (y[1]-y[0])/(x[1]-x[0])

    #find y-intercept (b)
    b = y[0] - (m*x[0])

    #create line dictionary Keys: y-intercept, slope
    line = {}
    line["intercept"] = round(b,4)
    line["slope"] = round(m,4)

    return line




    #Predict (x,y) values given the slope and y-intercept.
    #
def predictValues(lineDictionary, num_values):
    
    #Predict x values for a range of random y values.

    #:param slope: demandLine/supplyLine "slope": value.
    #:param y_intercept: demandLine/supplyLine "intercept": value.
    #:param num_values: The number of x values to predict.
    #:return: A list of predicted x values for random y values.
    
    predictedQuantity = []
    predictedPrice = []
    slope = lineDictionary["slope"]
    y_intercept = lineDictionary["intercept"]

    i = 0
    while i < num_values:
            #Generate a random y value in the range [0, 1500]
        randomY = random.randint(0, 1800)
    
            #Predict the x value for the given y value, 
            #and return to list predictedQuantity.
        x_value = round((randomY - y_intercept) / slope)
        
        if x_value >= 0:
                #append (x,y)
            predictedPrice.append(randomY)
            predictedQuantity.append(x_value)

            i += 1
        
        else:
            continue

            #Return Predicted (x,y) values lists
    return predictedQuantity, predictedPrice




    #Create a dictionary for a supply/demand dataframe
    #
def dataDict(x, xN, y, yN):
    
    dataDictionary = {}
    dataDictionary[yN] = y
    dataDictionary[xN] = x

    return dataDictionary




    #Creates the supply & demand graph
def create_sd_graph(demandDF, supplyDF):
    demandDF = demandDF
    supplyDF = supplyDF

    fig, ax = plt.subplots()

    ax.plot(demandDF["quantityD"], demandDF["priceD"], label = 'Demand')
    ax.plot(supplyDF["quantityS"], supplyDF["priceS"], label = 'Supply')

    ax.set_xlabel('Quantity')
    ax.set_ylabel('Price')
    ax.set_title('Supply and Demand Graph')
    ax.legend()

    plt.grid()
    plt.show()



###########################################################


    #create Linear equations for supply/demand
demandLine = linearEquation(quantityDemanded, priceDemanded)
supplyLine = linearEquation(quantitySupplied, priceSupply)

print(f"The demand line is: {demandLine}")
print(f"The supply line is: {supplyLine}")



    #predict values with the given lines
predictedDemandQuantity, predictedDemandPrice = predictValues(demandLine, 4)
predictedSupplyQuantity, predictedSupplyPrice = predictValues(supplyLine, 4)



    #new supply and demand data points predicted with actual represented by linear equation
newQuantityDemanded = quantityDemanded + predictedDemandQuantity
newQuantityDemanded.sort()

newPriceDemanded = priceDemanded + predictedDemandPrice
newPriceDemanded.sort(reverse=True)

newQuantitySupplied = quantitySupplied + predictedSupplyQuantity
newQuantitySupplied.sort()

newPriceSupplied = priceSupply + predictedSupplyPrice
newPriceSupplied.sort()


    #create dictionaries of supply and demand lists
demandDict = dataDict(newQuantityDemanded, "quantityD", newPriceDemanded, "priceD")
supplyDict = dataDict(newQuantitySupplied, "quantityS", newPriceSupplied, "priceS")


    #create DataFrames from dictionaries
demandDF = pd.DataFrame(demandDict)
supplyDF = pd.DataFrame(supplyDict)
print(f"Demand DataFrame:\n{demandDF}")
print(f"Supply DataFrame:\n{supplyDF}")

    #Completed Product!!!!
finalProduct = create_sd_graph(demandDF, supplyDF)