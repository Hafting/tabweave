#For testing and figuring out gr
import gr


#gr.clearws()
#gr.setviewport(0, 1, 0, 1)
gr.setwindow(-5,5,-5,5)
#gr.setfillstyle(1)   #0:HOLLOW, 1:SOLID, 2:PATTERN, 3:HATCH 0==1 ?
gr.setfillintstyle(1)#0:HOLLOW, 1:SOLID, 2:PATTERN, 3:HATCH 0==1 ?
gr.setfillcolorind(2) #0:WHITE 1:BLACK 2:RED 
#The attributes that control the appearance of fill areas are fill area interior style, fill area style index and fill area color index.

gr.fillarea([1,2,2],[1,2,1])
gr.setfillintstyle(0)
gr.setfillcolorind(1)
gr.fillarea([1,2,2],[1,2,1])

gr.updatews()
input("enter")
gr.clearws()
gr.setwindow(0.9,2.1,0.9,2.1)
gr.fillarea([1,2,2],[1,2,1])
gr.updatews()
input("e")
