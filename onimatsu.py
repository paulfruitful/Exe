costprice=float(input("How Much Is The Commodity? "))
sellingprice=int(input("How Much Was The Commodity Sold For? "))
profitOrLoss = (sellingprice - costprice)
profitOrLossPercentage = (profitOrLoss/costprice) * 100
if costprice > sellingprice:
    print('You made loss')
    print(f'You lost {(-1*profitOrLossPercentage)}% of your original capital')
else:
    print('You made profit')    
    print(f'You made {profitOrLossPercentage}% of your original capital')