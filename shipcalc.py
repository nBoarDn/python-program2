##
# Title:  Shipping Calculator
# Author: B
# Date: 9/17/17
# Purpose: The program allows for input to be received for the shipping info and
#           calculate the total costs based on selections made

import wx


class CalculatorFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(650, 600))

        self.panel = wx.Panel(self, -1)  # add a panel

        # Create the info boxes and labels
        self.namectrl = wx.TextCtrl(self.panel, pos=(90, 30), size=(270, -1))
        self.namelabel = wx.StaticText(self.panel, label="Name", pos=(370, 30))
        self.addressctrl1 = wx.TextCtrl(self.panel, pos=(90, 65), size=(350, -1))
        self.addresslabel1 = wx.StaticText(self.panel, label="Address", pos=(450, 65))
        self.addressctrl2 = wx.TextCtrl(self.panel, pos=(90, 100), size=(300, -1))
        self.addresslabel2 = wx.StaticText(self.panel, label="City State and Zip", pos=(400, 100))

        # Create two radio groups with headings on each
        self.weight = wx.StaticText(self.panel, label="Weight", pos=(40, 170))
        self.w1 = wx.RadioButton(self.panel, -1, label='0 - 1.9 lbs. $5', pos=(30, 200), style = wx.RB_GROUP)
        self.w2 = wx.RadioButton(self.panel, -1, label='2 - 4.9 lbs. $8', pos=(30, 230))
        self.w3 = wx.RadioButton(self.panel, -1, label='5 - 10 lbs. $12.25', pos=(30, 260))

        self.speed = wx.StaticText(self.panel, label="Speed", pos=(255, 170))
        self.s1 = wx.RadioButton(self.panel, -1, label='overland $2.75', pos=(250, 200),style = wx.RB_GROUP)
        self.s2 = wx.RadioButton(self.panel, -1, label='3-day air $6.15', pos=(250, 230))
        self.s3 = wx.RadioButton(self.panel, -1, label='2-day air $10.80', pos=(250, 260))
        self.s4 = wx.RadioButton(self.panel, -1, label='overnight $15.25', pos=(250, 290))

        # Create a checkbox group with a header
        self.options = wx.StaticText(self.panel, label="Options", pos=(455, 170))
        self.o1 = wx.CheckBox(self.panel, -1, label='Extra padding $5', pos=(450, 200))
        self.o2 = wx.CheckBox(self.panel, -1, label='Gift wrapping $8', pos=(450, 230))

        # Create two buttons for calculating and clearing the form
        self.btn_calc = wx.Button(self.panel, label="Calculate Total", pos=(140, 350))
        self.btn_clear = wx.Button(self.panel, label="Clear Form", pos=(340, 350))

        # Create a header for the summary
        self.summaryText = wx.StaticText(self.panel, label="Shipping Summary", pos=(240, 400))

        # Create labels for the summary and set to empty
        self.lbl_name = wx.StaticText(self.panel, label='', pos=(150, 430))
        self.lbl_address1 = wx.StaticText(self.panel, label='', pos=(150, 455))
        self.lbl_address2 = wx.StaticText(self.panel, label='', pos=(150, 480))
        self.lbl_totalcost = wx.StaticText(self.panel, label='', pos=(150, 505))

        # Connect buttons event to an event-handler function
        self.btn_calc.Bind(wx.EVT_BUTTON, self.MoveText)
        self.btn_calc.Bind(wx.EVT_BUTTON, self.TotalCost)
        self.btn_clear.Bind(wx.EVT_BUTTON, self.clearForm)


    def MoveText(self, event):

        # Get the input values for the shipping information
        name = self.namectrl.GetValue()
        add1 = self.addressctrl1.GetValue()
        add2 = self.addressctrl2.GetValue()
        if name == "":
            name = "n/a"
        if add1 == "":
            add1 = "n/a"
        if add2 == "":
            add2 = "n/a"

        # Set the labels in the summary
        self.lbl_name.SetLabelText(name)
        self.lbl_address1.SetLabelText(add1)
        self.lbl_address2.SetLabelText(add2)


    def TotalCost(self, event):

        # Get the weight cost selected
        weightcost = 0
        if self.w1.GetValue() is True:
            weightcost = 5
        elif self.w2.GetValue() is True:
            weightcost = 8
        elif self.w3.GetValue() is True:
            weightcost = 12.25

        # Get the shipping cost selected
        shipcost = 0
        if self.s1.GetValue() is True:
            shipcost = 2.75
        elif self.s2.GetValue() is True:
            shipcost = 6.15
        elif self.s3.GetValue() is True:
            shipcost = 10.80
        elif self.s4.GetValue() is True:
            shipcost = 15.25

        # Get the option costs selected
        option1 = 0
        option2 = 0
        if self.o1.GetValue() is True:
            option1 = 5
        if self.o2.GetValue() is True:
            option2 = 8

        # Set the total costs of shipping
        self.lbl_totalcost.SetLabelText("$ %2.2f" % (weightcost + shipcost + option1 + option2))

        # Used to handle multiple widgets for a single event
        event.Skip()

    def clearForm(self, event):

        # Set all values to empty or 0
        self.namectrl.SetLabel('')
        self.addressctrl1.SetLabel('')
        self.addressctrl2.SetLabel('')
        self.o1.SetValue(0)
        self.o2.SetValue(0)
        self.lbl_name.SetLabel('')
        self.lbl_address1.SetLabel('')
        self.lbl_address2.SetLabel('')
        self.lbl_totalcost.SetLabel('')

# Execute Program
if __name__ == "__main__":
    app = wx.App()
    frame = CalculatorFrame(None, 'Shipping Calculator')
    frame.Show(True)
    app.MainLoop()
