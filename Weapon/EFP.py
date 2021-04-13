
metals = ['Gold']
metalsFP = []
metalsSP = []
metalsTotal_Ounces = []
EFP = []

for i in metals:
    Future_Price = float(input('Enter FUTURES price for' + ' ' + i + ':'))
    Spot_Price = float(input('Enter Spot price for' + ' ' + i +':'))
    Total_ounces = float(input('Enter total ounces' + ' ' + i + ':'))
    metalsFP.append(Future_Price)
    metalsSP.append(Spot_Price)
    metalsTotal_Ounces.append(Total_ounces)
    EFP = (metalsFP - Spot_Price) * metalsTotal_Ounces
    EFP.append(EFP)

# EFP = (metalsFP[1] - Spot_price[1]) * metalsTotal_Ounces

print(EFP)
