def convert_heights_nested(hghts):
    hg=[]
    for hs in hghts:
        cm=hs * 2.54
        hg.append(round(cm, 3))
    return hg


     
ml=input("enter the heights of the persons:")
hghts= list(map(int, ml.split()))
interactiveloopheightconvert=convert_heights_nested(hghts)
print("heights in inches:",hghts)
print("heights in centimeters:",interactiveloopheightconvert)

