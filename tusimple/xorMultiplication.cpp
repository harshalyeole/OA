import pandas as pd
from bokeh.plotting import figure,show,output_notebook,output_file
from bokeh.models import ColumnDataSource, Label, LabelSet
from math import pi
from bokeh.layouts import row,column,gridplot

output_file("HarshalDashboard.html")

hars=pd.read_csv("./adult.data",header=None)

def get_labl_counts_ags(hars,dgt):
   agrnge=[]
   case=[]
   for q in range(20,110,10):
       if q==20:
           bottom=0
       else:
           bottom=q-10
          
       top=q
       aglabl=str(bottom) +"-"+str(top)+" Years"
       hars_x=hars[(hars[0]>=bottom) & (hars[0]<top)]
       w=hars_x[dgt].value_counts()
       tag=w.index.tolist()
       poll=w.tolist()
       dip=dict(zip(tag,poll))
      
       agrnge.append(aglabl)
       case.append(dip)
  
   return (agrnge,case)
def get_alll_lbbls(hars,dgt):
   return (hars[dgt].unique())
def create__figr(albles,d,t,i=0):
   x=[]
   y=[]
   for l in albles:
       x.append(l)
       if l in d:
           y.append(d[l])
       else:
           y.append(0)
   if i == 0:
     texxxt = ""
   elif i == 1:
     texxxt = "Marital Status"
   elif i == 2:
     texxxt = "Income"
   elif i == 3:
     texxxt = "Education"
   elif i == 4:
     texxxt = "Working Class"
   yw=figure(x_range=x,plot_width=250,plot_height=250,toolbar_location=None,title=texxxt)
   yw.vbar(x=x,top=y,width=0.05*len(x),color='gray')
   yw.xgrid.grid_line_color=None
   yw.yaxis.minor_tick_line_color=None
   yw.xaxis.visible=False
   yw.yaxis.axis_line_color=None

   return yw
def create_x_lbl_figr(hars,dgt,h):
   albles=get_alll_lbbls(hars,dgt)
   hy=figure(x_range=albles,plot_width=250,plot_height=h,toolbar_location=None)
   hy.vbar(x=albles,top=0,color=None)
   hy.xgrid.grid_line_color=None
   hy.ygrid.grid_line_color=None
   hy.yaxis.minor_tick_line_color=None
   hy.yaxis.visible=False
   hy.xaxis.axis_line_color=None
   hy.xaxis.major_label_orientation = pi/2
   hy.outline_line_color = None
   return hy
def create_agegrup_lblcol(hars):
   agrnge=[]
   for j in range(20,110,10):
       if j==20:
           bottom=0
       else:
           bottom=j-10
          
       top=j
       aglabl=str(bottom) +"-"+str(top)+" Years"
       agrnge.append(aglabl)
   hs=[]
   for j in agrnge:
       tn=figure(x_range=agrnge,plot_width=250,plot_height=250,toolbar_location=None)
       tn.vbar(x=agrnge,top=0,color=None,legend_label=j)
       tn.legend.location='top_right'
       tn.yaxis.visible=False
       tn.xaxis.visible=False
       tn.xgrid.grid_line_color=None
       tn.ygrid.grid_line_color=None
       tn.outline_line_color = None

       hs.append(tn)
   return hs
def createfigre_col(hars,dgt,w,i):
   cnum_labls=get_alll_lbbls(hars,dgt)
   a,d = get_labl_counts_ags(hars,dgt)
   hs=[]
   for ol in range(len(a)):
     if ol == 0:
       q=create__figr(cnum_labls,d[ol],a[ol],i)
      
     else:
       q=create__figr(cnum_labls,d[ol],a[ol])
     hs.append(q)   
   q= create_x_lbl_figr(hars,dgt,w)
   hs.append(q)
  
   return hs
def get_alll_lbbls(hars,dgt):
   return(hars[dgt].unique())
labelhy=create_agegrup_lblcol(hars)
plott1=createfigre_col(hars,5,145,1)
plott2=createfigre_col(hars,14,55,2)
plott3=createfigre_col(hars,3,95,3)
plott4=createfigre_col(hars,1,110,4)
show(row(column(labelhy),column(plott1),column(plott2),column(plott3),column(plott4)))
