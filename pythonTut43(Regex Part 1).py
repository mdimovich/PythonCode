import re

if re.search("ape", "The ape was at the place"):
    print("There is an ape")
else:
    print("There is no ape")
allApes = re.findall("ape.", "The ape was at the apex")
for i in allApes:
    print(i)
theStr = "The ape was at the apex"

# Returns location the they start and end and stores them in tuple
for i in re.finditer("ape.", theStr):
    locTuple = i.span()

    print(locTuple)
    print(theStr[locTuple[0]:locTuple[1]])

animalStr = "Cat rat mat pat"
allAnimals = re.findall("[Crmfp]at", animalStr)
someAnimals = re.findall("[c-mC-M]at", animalStr)
for i in someAnimals:
    print(i)