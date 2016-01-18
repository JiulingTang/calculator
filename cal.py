import wx
import ln
import po
import cos
import sin
import pipo
import sqrt
import cosh
#This function calculate a expression in the calculator
def cal(s):
    f={			#f map funtion name to funtion
        "cos":cos.cos,
        "sin":sin.sin,
        "pi^":pipo.pipo,
        "10^":po.po,
        "sqrt":sqrt.sqrt,
        #"x^x":xx.xx,
        "Cosh":cosh.cosh}
    for h in f:
        if s.find(h)>=0:	
            return f.get(h)(float(s[len(h)+1:len(s)-1]))#if function name exist in the expression, call the funtion to the count expression
    o=['+','-','*','/'] #o is an array contain +-*/ 
    pos=-1
    for i in range(0,4):
        if s.find(o[i])>=0:
            pos=s.find(o[i]) #if one arithmetic symbol in the expression, pos is its place in the expression
            break
    if pos==-1:
        return s
    else:
        s1=0  #s1 is the first number in the expression
        if pos>0:
            s1=float(s[0:pos])
        s2=float(s[pos+1:len(s)]) #s2 is the second number in the expression
        if i==0:
            return s1+s2
        elif i==1:
            return s1-s2
        elif i==2:
            return s1*s2
        elif i==3:
            return s1/s2
class helpwindow(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(helpwindow,self).__init__(*args,**kwargs)
        hbox=wx.BoxSizer(wx.VERTICAL)
        hpanel=wx.Panel(self, -1)
        demiliter=''
        doc=["Help\r",
            "cos:"]
        self.text=wx.TextCtrl(hpanel,-1,value=demiliter.join(doc),style=wx.TE_READONLY|wx.TE_MULTILINE,size=(360,50))
        hbox.Add(self.text,flag=wx.EXPAND|wx.ALL)
        hpanel.SetSizer(hbox)
class Calframe(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(Calframe,self).__init__(*args,**kwargs)
        self.initui()
    def hel(self,e):
        self.hw=helpwindow(None,size=(500,500))
        self.hw.Show(True)
    def initui(self):
        menub=wx.MenuBar();
        mn=wx.Menu(); #create munu
        xuan=mn.Append(101,"exit","exit"); #create exit menu item
        self.Bind(wx.EVT_MENU,self.qui,xuan)
        #xuan=mn.Append(102,"help","help");
        #self.Bind(wx.EVT_MENU,self.hel,xuan)
        menub.Append(mn,"menu"); 
        self.SetMenuBar(menub);
        panel=wx.Panel(self, -1)
        box=wx.FlexGridSizer(4,3,vgap=0,hgap=0) 
        panel4=wx.Panel(panel)
        panel2=wx.Panel(panel4)
        self.text=wx.TextCtrl(panel,-1,value='0',style=wx.TE_READONLY,size=(360,50)) #create display window 
        self.text.SetBackgroundColour("wheat")
        mbox=wx.BoxSizer(wx.VERTICAL)
        mbox.Add(self.text,flag=wx.EXPAND|wx.ALL)
        gw=60;
        gh=60;
        #create the button for 1 to 10
        for i in range(1,10):
            button=wx.Button( panel2, i, str(i),size=(gw,gh))
            box.Add( button ,1,wx.EXPAND|wx.ALL)
            self.Bind(wx.EVT_BUTTON, self.cnum,button )
        button=wx.Button(panel2,0,'0',size=(gw,gh)) 
        box.Add(button,3,wx.EXPAND|wx.ALL)
        self.Bind(wx.EVT_BUTTON, self.cnum,button )
        button=wx.Button(panel2,10,'.',size=(gw,gh))
        box.Add(button,3,wx.EXPAND|wx.ALL)
        self.Bind(wx.EVT_BUTTON, self.cnum,button )
        button=wx.Button(panel2,17,"AC",size=(gw,gh))
        box.Add(button,3,wx.EXPAND|wx.ALL)
        self.Bind(wx.EVT_BUTTON, self.cnum,button )
                   
        panel2.SetSizer(box)
        panel5=wx.Panel(panel4)
        panel3=wx.Panel(panel5)
        rbox=wx.GridBagSizer(vgap=0,hgap=0)
        button=wx.Button(panel3,11,"cos",size=(gw,gh))
        rbox.Add(button,pos=(0,0))
        self.Bind(wx.EVT_BUTTON, self.count,button )
        button=wx.Button(panel3,12,"sin",size=(gw,gh))
        rbox.Add(button,pos=(0,1))
        self.Bind(wx.EVT_BUTTON, self.count,button )
        button=wx.Button(panel3,13,"pi^x",size=(gw,gh))
        rbox.Add(button,(0,2))
        self.Bind(wx.EVT_BUTTON, self.count,button )
        button=wx.Button(panel3,14,"10^x",size=(gw,gh))
        rbox.Add(button,(1,0))
        self.Bind(wx.EVT_BUTTON, self.count,button )  
        button=wx.Button(panel3,15,"sqrt(x)",size=(gw,gh))
        rbox.Add(button,(1,1))
        self.Bind(wx.EVT_BUTTON, self.count,button )
    
        button=wx.Button(panel3,18,"cosh",size=(gw,gh))
        rbox.Add(button,(1,2))
        self.Bind(wx.EVT_BUTTON, self.count,button )
        button=wx.Button(panel3,19,"-",size=(gw,gh))
        rbox.Add(button,(2,0))
        self.Bind(wx.EVT_BUTTON, self.cnum,button )
        button=wx.Button(panel3,20,"+",size=(gw,gh))
        rbox.Add(button,(2,1))
        self.Bind(wx.EVT_BUTTON, self.cnum,button )
        button=wx.Button(panel3,21,"*",size=(gw,gh))
        rbox.Add(button,(2,2))
        self.Bind(wx.EVT_BUTTON, self.cnum,button )
        button=wx.Button(panel3,22,"/",size=(gw,gh))
        rbox.Add(button,(3,0))
        self.Bind(wx.EVT_BUTTON, self.cnum,button ) 
        button=wx.Button(panel3,23,"=",size=(2*gw,gh))
        rbox.Add(button,(3,1),span=(1,2))
        self.Bind(wx.EVT_BUTTON, self.count,button )
        panel3.SetSizer(rbox)
        rbox2=wx.BoxSizer(wx.VERTICAL)
        rbox2.Add(panel3)
        panel5.SetSizer(rbox2)
        abox=wx.BoxSizer(wx.HORIZONTAL)
        abox.Add(panel2,flag=wx.EXPAND|wx.ALL)
        abox.Add(panel5,flag=wx.EXPAND|wx.ALL)
        panel4.SetSizer(abox)
        mbox.Add(panel4,flag=wx.EXPAND|wx.ALL)
        panel.SetSizer(mbox)
        self.Show(True);
        self.Center()
    # this function close the calculator
    def qui(self,e):
        self.Close()
    # this function is called after click some buttons    
    def cnum(self,e):
        s=self.text.GetValue()
        if s!="error" or e.GetId()==17:
            if e.GetId()<10:
                if s[0]!='0'or len(s)!=1:
                    s=s+str(e.GetId())
                else:
                    s=str(e.GetId())
            else:
                if e.GetId()==10:
                    s=s+'.'
                else:
                    if e.GetId()==17:
                        s='0'
                    else:
                        result=cal(self.text.GetValue())
                        s=str(result)
                        if e.GetId()==19:
                            s=s+'-'
                        elif e.GetId()==20:
                            s=s+'+'
                        elif e.GetId()==21:
                            s=s+'*'
                        elif e.GetId()==22:
                            s=s+'/'
        self.text.SetValue(s)
    # this function is called after click some buttons   
    def count(self,e):
        if self.text.GetValue()=="error":
            result="error"
        else:
            self.text.SetValue(str(cal(self.text.GetValue())))
            if (e.GetId()==23):
                return
            op={            #op map the id of the funtion button to the name of function
                11:"cos",
                12:"sin",
                13:"pi^",
                14:"10^",
                15:"sqrt",
                #16:"x^x",
                18:"Cosh"}
            result=op[e.GetId()]+'('+self.text.GetValue()+')'
        self.text.SetValue(str(result))
if __name__=='__main__':
    a=wx.App()
    Calframe(None,size=(390,360))
    a.MainLoop()
