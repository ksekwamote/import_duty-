# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:10:14 2020

@author: Kabelo
"""

import pandas as pd

countries = pd.read_csv('general1.csv')
general = list(countries['Country'])

country = input("Type your country: ")
category = int(input("Type and enter the number corresponding to the category of your product:\n"+
                 "\n1. Arms & Ammunition\n2. Audio/Video\n3. Bags & Luggage\n4. Books\n5. Beauty & Cosmetics\n6. Cameras\n7. Carpets/Floor Covers\n8. Computer/Laptop\n9. Fashion/Clothing\n10. "+
                 "Gaming Consoles\n11. Home Decor\n12. Jewellery\n13. Jewellery (Precious metals/pearls)\n14. Kitchen (Glassware)\n15. Mobile Phones\n16. Musical Instruments\n17. Pet Accessory\n18. "+
                 "Shoes\n19. Sports & Leisure\n20. Toys\n21. Watches"
                 +"\n\nCategory number: "))
price = int(input("Price of your product (ZAR/USD): "))

def duty_calculator(country, category, price):
    SADC_countries = ['Angola', 'Botswana', 'Congo DRC', 'Lesotho', 'Malawi', 'Madagascar', 'Mauritius', 'Mozambique', 'Namibia',
                      'Seychelles', 'South Africa', 'Swaziland', 'Tanzania', 'Zambia', 'Zimbabwe']
    EU_countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece',
                     'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia',
                     'Spain', 'Sweden', 'United Kingdom']
    EFTA_countries = ['Iceland', 'Liechtenstein', 'Norway', 'Switzerland']
    MERCOSUR_countries = ['Argentina', 'Brazil', 'Paraguay', 'Uruguay']

    if country in SADC_countries:
        print("\nSADC Trade Agreement")
        if category == 1: duty = 0.
        if category == 2: duty = 0.
        if category == 3: duty = 0.
        if category == 4: duty = 0.
        if category == 5: duty = 0.
        if category == 6: duty = 0.
        if category == 7: duty = 0.
        if category == 8: duty = 0.
        if category == 9: duty = 0.
        if category == 10: duty = 0.
        if category == 11: duty = 0.
        if category == 12: duty = 0.
        if category == 13: duty = 0.
        if category == 14: duty = 0.
        if category == 15: duty = 0.
        if category == 16: duty = 0.
        if category == 17: duty = 0.
        if category == 18: duty = 0.
        if category == 19: duty = 0.
        if category == 20: duty = 0.
        if category == 21: duty = 0.


    elif country in EU_countries:
        print("\nEU Trade Agreement")
        if category == 1: duty = 0.
        if category == 2: duty = 0.
        if category == 3: duty = 0.2
        if category == 4: duty = 0.
        if category == 5: duty = 0.
        if category == 6: duty = 0.
        if category == 7: duty = 0.03
        if category == 8: duty = 0.
        if category == 9: duty = 0.27
        if category == 10: duty = 0.
        if category == 11: duty = 0.18
        if category == 12: duty = 0.
        if category == 13: duty = 0.
        if category == 14: duty = 0.
        if category == 15: duty = 0.
        if category == 16: duty = 0.
        if category == 17: duty = 0.05
        if category == 18: duty = 0.2
        if category == 19: duty = 0.
        if category == 20: duty = 0.
        if category == 21: duty = 0.

    elif country in EFTA_countries:
        print("\nEFTA Trade Agreement")
        if category == 1: duty = 0.15
        if category == 2: duty = 0.
        if category == 3: duty = 0.2
        if category == 4: duty = 0.
        if category == 5: duty = 0.
        if category == 6: duty = 0.
        if category == 7: duty = 0.03
        if category == 8: duty = 0.
        if category == 9: duty = 0.2
        if category == 10: duty = 0.
        if category == 11: duty = 0.15
        if category == 12: duty = 0.
        if category == 13: duty = 0.
        if category == 14: duty = 0.
        if category == 15: duty = 0.
        if category == 16: duty = 0.
        if category == 17: duty = 0.05
        if category == 18: duty = 0.2
        if category == 19: duty = 0.
        if category == 20: duty = 0.
        if category == 21: duty = 0.


    elif country in MERCOSUR_countries:
        print("\nMERCOSUR Trade Agreement")
        if category == 1: duty = 0.15
        if category == 2: duty = 0.
        if category == 3: duty = 0.3
        if category == 4: duty = 0.
        if category == 5: duty = 0.2
        if category == 6: duty = 0.
        if category == 7: duty = 0.05
        if category == 8: duty = 0.
        if category == 9: duty = 0.45
        if category == 10: duty = 0.
        if category == 11: duty = 0.3
        if category == 12: duty = 0.
        if category == 13: duty = 0.2
        if category == 14: duty = 0.15
        if category == 15: duty = 0.
        if category == 16: duty = 0.
        if category == 17: duty = 0.05
        if category == 18: duty = 0.3
        if category == 19: duty = 0.
        if category == 20: duty = 0.
        if category == 21: duty = 0.


    elif country in general:
        print("\nRegion: General")
        if category == 1: duty = 0.15
        if category == 2: duty = 0.
        if category == 3: duty = 0.3
        if category == 4: duty = 0.
        if category == 5: duty = 0.2
        if category == 6: duty = 0.
        if category == 7: duty = 0.05
        if category == 8: duty = 0.
        if category == 9: duty = 0.45
        if category == 10: duty = 0.
        if category == 11: duty = 0.3
        if category == 12: duty = 0.
        if category == 13: duty = 0.2
        if category == 14: duty = 0.15
        if category == 15: duty = 0.
        if category == 16: duty = 0.
        if category == 17: duty = 0.05
        if category == 18: duty = 0.3
        if category == 19: duty = 0.
        if category == 20: duty = 0.
        if category == 21: duty = 0.

    tax = 0.15*price
    import_duty = duty*price
    total_cost = price+tax+import_duty

    print("15.0% tax on your product value: {} ZAR/USD".format(tax)+
          "\n{0:}% import duties on your product value: {1:} ZAR/USD".format(duty*100, import_duty)+
          "\nThe estimated total cost excluding shipping (price + tax + import duty) will be: {} ZAR/USD".format(total_cost))

duty_calculator(country, category, price)