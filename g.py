#For testing and figuring out gr
import gr

# see https://twistedthreads.org/pattern/NxyFKCzGxeFnqnvgZ
# / / / / \ \ \ \ \
# \ \ \ \ / / / \ \
#
# ///\\
# \\\\\


# For every tablet, draw one of these:
# _    _
# /    \
#
# Depending on direction of rotation. 
# Left part: color of prev. thread being rotated out
# Right part: color of new thread being rotated in.
# _________
# ///\\\///
#
# Nonrotating tablet gives a float. Drawing postponed till
# rotation happens, or the weaving ends.
#
# Re-ordering tablets: draw under-movers first, then over-movers on top.
# Much like normal, but from old column to new column!


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
