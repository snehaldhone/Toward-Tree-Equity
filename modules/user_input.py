#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:32:52 2023

@author: kalliann
"""

from pygris.geocode import geocode

district_ids = {'allston brighton': 1, 'back bay': 2, 'beacon hill': 3, 
                'charlestown': 4, 'central': 5, 'dorchester': 6, 
                'east boston': 7, 'fenway': 8, 'longwood': 8, 
                'hyde park': 10, 'jamaica plain': 11, 'mattapan': 12, 
                'mission hill': 13, 'roslindale': 14, 'roxbury': 15, 
                'south boston':16, 'south end': 17, 'west roxbury': 18
                }

def area_of_interest():
    
    districts = ['allston brighton', 'back bay', 'beacon hill', 
                 'charlestown', 'central', 'dorchester',
                 'east boston', 'fenway', 'longwood', 
                 'hyde park', 'jamaica plain', 'mattapan',
                 'mission hill', 'roslindale', 'roxbury',
                 'south boston', 'south end', 'west roxbury'
        ]
    
    r = input("Type the name of the neighborhood you're interested in: ")
    
    while r.lower() not in districts:
        print()
        for d in districts:
            print(d)
        print()
        r = input("Please choose from one of the above: ")
    
    print()
    print("Got it, thanks!")
    
    return r.lower()

def species():
    
    species = ['littleleaf linden', 'norway maple', 'crabapple spp',
               'hedge maple', 'red maple', 'green ash', 'japanese zelkova', 
               'norther red oak', 'japanese tree lilac', 'american sycamore',
               'honeylocust', 'pin oak', 'sweetgum', 'london planetree', 
               'ginko', 'american elm', 'kwanzan cherry', 'accolade elm',
               'other', 'not sure'
               ]
    
    s = input("What species are you interested in? ")
    
    while s.lower() not in species:
        print()
        for x in species:
            print(x)
        print()
        s = input("Please choose from one of the above: ")
        
    print("Got it, thanks!")
        
    return s.lower()

def maturation():
    
    maturation = ['seedling', 'young', 'establishing', 'maturing', 'mature']
    
    print("Identify the maturation of your tree:")
    print()
    print("seedling - just planted")
    print("young - less than 6 years old")
    print("establishing - less than 18 years old")
    print("maturing - less than 24 years old")
    print("mature - 25 years or older")
    print()
    
    m = input("How old is your tree? ")
    
    while m.lower() not in maturation:
        print()
        for x in maturation:
            print(x)
        print()
        m = input("Type one of the above: ")
        
    print()
    print("Got it, thanks!")
        
    return m.lower()

def health():
    
    health = ['good', 'poor']
    
    print("Tree Health:")
    print()
    print("Unless your tree is on the decline, indicate 'good' for good health.")
    print("If your tree is clearly declining, indicate 'poor.'")
    print()
    
    h = input("Is your tree's health good or poor? ")
    
    while h.lower() not in health:
        print()
        for h in health:
            print(h)
        print()
        h = input("Type one of the above: ")
        
    print()
    print("Got it, thanks!")
    
    return h

def address():
    
    for attempt in range(4):
        
        print('Where are you planting this tree?')
        a = input('Enter address: ')
    
        try:
            geocode(a)
            return a
        
        except Exception as e:
            print()
            print(f"Geocoding failed for address '{address}': {e}")
            print()
        
            print('Please format addresses accordingly:')
            print("100 Wilmer Ave, Boston, MA")
            print('Make sure to include commas; do not include unit numbers.')
            print()
            
            if attempt < 2:
                print("Please try again.")
                print()
            elif attempt == 2:
                print("This is your last attempt.")
                print()
            else:
                print('Geocoding is not possible at this address.')
                print('Some features of analysis may not be available.')
                print(f"The address you've entered is: {a}.")
                return a
            
