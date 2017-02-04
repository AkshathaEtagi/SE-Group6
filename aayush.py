import pymongo
from pymongo import MongoClient

client=MongoClient('localhost',27017)

def disp(q):
    client=MongoClient()
    db=client["admin"]
    collection=db["details"]
    meddet=db.details.find_one({"SNo":q})
    print meddet



def altermed(ingli,b):                                #ingli--ingredients, b--sno
    client=MongoClient()
    db=client["admin"]
    #print(ingli)
    collection=db["ingredients"]
    #curser=db.ingredients.find({"Ingredients":ingli[0]})
    print db.ingredients.find({"Ingredients":ingli[0]}).count()
    for med in db.ingredients.find({"Ingredients":ingli[0]}):
        print(med)
        #if (record['Ingredients']==ingli[0]):
        e=med['SNo']
        print(e)
        if (b!=e):
            print med['SNo']
            disp(x)                     


def findin(n):                                         #n holds the SNo of the medicine entered
    client=MongoClient()
    db=client["admin"]
    collection=db["ingredients"]                       #in table--ingredients
    ing=db.ingredients.find_one({"SNo":n})             #find the ingredients corresponding to that SNo
    #print("The Ingredients are:")
    #print ing['Ingredients']
    inglist=[]                                         #save it in a list inglist
    inglist.insert(0, ing['Ingredients'])
    print("Displaying the List of ingredients\n")
    print(inglist)
    #print("test1")
    altermed(inglist,n)                                 #call altermed(pass n--SNo of entered medicine, inglist--ingredients of entered medicine)





client=MongoClient()
db=client["admin"]
collection=db["details"]
s=raw_input('Enter Name=')
a="  "
s=s+a                                  #enter the name of the medicine to search
print("\nDetails about the entered medicine are:\n")
cursor=db.details.find_one({"Name":s})                      #find an entry with the same name as entered
print(cursor)                                               #print the details of that medicine
x=cursor['SNo']
print("\n")
findin(x)                                                   #x holds the SNo of the medicine entered

