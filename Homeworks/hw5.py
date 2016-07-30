#Kwang Su Choi & Brian Bradley
#CS 1301 B5
#Kwang Su Choi (902969968) & Brian Bradley (902955107)
#kchoi20@gatech.edu & bbradley2013@gatech.edu
#We worked on this homework assignment alone, using only this semester's course materials.





from Myro import *
init()

def makeWebPage(numberOfPictures):

    n = numberOfPictures
    myFile = open("myPage.html","w")
    html = ""
    html = html + '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">'
    robotName = str(getName())
    html = html + "<head><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' /><title>"+robotName+"'s Site!</title></head>"
    html = html + "<body>Welcome to "+robotName+"'s Webpage!<br/>"
    html = html + "By Brian Bradley and Kwang Su Choi"
    html = html + '<table border="0">'
    html = html + "<tr>"
    aList = range(0,n)
    for i in aList:
        pic = takePicture()
        light = getObstacle()
        s = "pic"+str(aList[i])+".jpg"
        savePicture(pic,s)
        if i%6 == 0 and i != 0:
            html = html + '</tr><tr><td><img src="{0}" alt="Pic"/><br/>{1}</td>'.format(s,light)
        else:
            html = html + '<td><img src="{0}" alt="Pic"/><br/>{1}</td>'.format(s,light)
        turnLeft(1,.5)
    html = html + "</tr>"
    html = html + "</table>"
    html = html + "Picture taken by "+robotName
    html = html + "</body></html>"
    myFile.write(html)
    myFile.close()
