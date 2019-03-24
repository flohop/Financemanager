import wx

from Financemanager import graph
from Financemanager.graph import graph_draw, value_manager



class MainGUI(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent,  title="Finanzmanager", size=(960, 540))
                          #style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)




        self.value_to_add = 0
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.panel.SetSize(960, 540)
        top_sizer = wx.BoxSizer(wx.VERTICAL)

        # Startbar and status and icon
        top_menu = wx.MenuBar()
        file_menu = wx.Menu()
        file_item = file_menu.Append(wx.ID_EXIT, '&Quit', 'Quit application')

        self.SetMenuBar(top_menu)

        self.status_bar = self.CreateStatusBar(2)
        self.status_bar.SetStatusWidths([-1, -10])
        self.status_bar.SetStatusText("Status:", 0)

        icon_file = value_manager.get_icon_file()
        icon1 = wx.Icon(icon_file, wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon1)
        #  add money buttons

        money_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.money_1_button = wx.Button(self.panel, wx.ID_ANY, label="5€")
        self.money_1_button.myvalue = 5
        money_sizer_1.Add(self.money_1_button, 1)

        self.money_2_button = wx.Button(self.panel, wx.ID_ANY, label="10€")
        self.money_2_button.myvalue = 10

        money_sizer_1.Add(self.money_2_button, 1, )

        money_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.money_3_button = wx.Button(self.panel, wx.ID_ANY, label="20€")
        self.money_3_button.myvalue = 20

        money_sizer_2.Add(self.money_3_button, 1,)

        self.money_4_button = wx.Button(self.panel, wx.ID_ANY, label="50€")
        self.money_4_button.myvalue = 50

        money_sizer_2.Add(self.money_4_button, 1)

        money_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        self.money_5_button = wx.Button(self.panel, wx.ID_ANY, label="100€")
        self.money_5_button.myvalue = 100

        money_sizer_3.Add(self.money_5_button, 1)

        self.money_6_button = wx.Button(self.panel, wx.ID_ANY, label="200€")
        self.money_6_button.myvalue = 200
        money_sizer_3.Add(self.money_6_button, 1)

        money_sizer_4 = wx.BoxSizer(wx.HORIZONTAL)

        self.money_7_button = wx.Button(self.panel, wx.ID_ANY, label="500€")
        self.money_7_button.myvalue = 500
        money_sizer_4.Add(self.money_7_button, 1)

        self.money_input = wx.TextCtrl(self.panel, -1, size=(75, 24))
        money_sizer_4.Add(self.money_input, 1)

        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.text_money = wx.TextCtrl(self.panel, wx.ID_ANY, value="Add:", style=wx.TE_READONLY)
        text_sizer.Add(self.text_money, 1)
        self.input_button = wx.Button(self.panel, wx.ID_ANY, label="+", size=(20, 25))
        self.input_button.myvalue = 1

        self.confirm_button = wx.Button(self.panel, wx.ID_ANY, label="Confirm", size=(10, 25))
        text_sizer.Add(self.confirm_button, 1)

        change_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.change_button = wx.Button(self.panel, wx.ID_ANY, label="+/-")
        change_sizer.Add(self.change_button, 1, wx.TOP)

        self.show_graph = wx.Button(self.panel, wx.ID_ANY, label="Show Graph")
        self.show_graph.graph_shown = False
        self.show_graph.SetBackgroundColour(wx.Colour(252, 245, 37))
        #self.show_graph.SetForegroundColour(wx.Colour(252, 245, 37))
        show_graph_sizer = wx.BoxSizer(wx.HORIZONTAL)
        show_graph_sizer.Add(self.show_graph, 1)

        # Monthly subcriptions
        sub_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_static_name = wx.StaticText(self.panel, wx.ID_ANY, label=" Add monthly Transaction:")
        self.sub_price_input_text = wx.StaticText(self.panel, wx.ID_ANY, label="Name:")
        self.sub_price_input = wx.TextCtrl(self.panel, wx.ID_ANY)
        self.sub_confirm = wx.Button(self.panel, wx.ID_ANY, "Add")

        sub_sizer_1.Add(self.sub_static_name, 0, wx.RIGHT, 10)

        sub_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sub_sizer_2.Add(self.sub_price_input_text, 0, wx.RIGHT | wx.TOP, 3)
        sub_sizer_2.Add(self.sub_price_input, 1, wx.RIGHT, 25)

        self.sub_static_text_v = wx.StaticText(self.panel, wx.ID_ANY, label="Value")
        self.sub_static_value = wx.TextCtrl(self.panel, wx.ID_ANY, )

        sub_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)

        sub_sizer_3.Add(self.sub_static_text_v, 0, wx.RIGHT | wx.TOP, )
        sub_sizer_3.Add(self.sub_static_value, 0, wx.TOP, 1)
        self.sub_add_btn = wx.Button(self.panel, wx.ID_ANY, "+", size=(25, 25))
        self.sub_add_btn.type = 1
        sub_sizer_3.Add(self.sub_add_btn, 0)


        sub_sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sub_sizer_4.Add(self.sub_confirm, 1, wx.RIGHT, 30)

        # Remove subscription
        sub_sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sub_sizer_4_5 = wx.BoxSizer(wx.HORIZONTAL)
        self.remove_static = wx.StaticText(self.panel, wx.ID_ANY, "Remove monthly Transaction:")
        drop_box_values = value_manager.get_monthly_subscriptions()
        drop_box_values.append("")
        self.monthly_subscr_box = wx.ComboBox(self.panel, wx.ID_ANY, choices=drop_box_values, style=wx.CB_READONLY)

        sub_sizer_4_5.Add(self.remove_static, 0, wx.RIGHT |wx.TOP, 10)
        self.monthly_remove = wx.Button(self.panel, wx.ID_ANY, "Remove")
        sub_sizer_5.Add(self.monthly_subscr_box, 0, wx.TOP, 10)
        sub_sizer_5.Add(self.monthly_remove, 0, wx.TOP, 10)


        # Goal Widgets
        goal_value_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.value_text = wx.StaticText(self.panel, wx.ID_ANY, "Goal value:")
        self.goal_value = wx.TextCtrl(self.panel, wx.ID_ANY)

        goal_value_sizer.Add(self.value_text, 1, wx.ALIGN_BOTTOM | wx.TOP, 40)
        goal_value_sizer.Add(self.goal_value, 1, wx.ALIGN_BOTTOM)

        goal_name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.name_text = wx.StaticText(self.panel, wx.ID_ANY, "Goal name:")
        self.goal_name = wx.TextCtrl(self.panel, wx.ID_ANY)

        goal_name_sizer.Add(self.name_text, 1, wx.ALIGN_BOTTOM)
        goal_name_sizer.Add(self.goal_name, 1, wx.ALIGN_BOTTOM)

        goal_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.goal_button = wx.Button(self.panel, wx.ID_ANY, "Add Goal")

        goal_button_sizer.Add(self.goal_button, 1, wx.ALIGN_BOTTOM | wx.BOTTOM, )

        combo_items = value_manager.get_goal_names()
        combo_items.append("")
        self.remove_goal_drop = wx.ComboBox(self.panel, wx.ID_ANY, choices=combo_items, style=wx.CB_READONLY)

        self.remove_goal_check = wx.CheckBox(self.panel, wx.ID_ANY, label="Remove goal")
        goal_button_sizer.Add(self.remove_goal_drop, 1, wx.ALIGN_BOTTOM | wx.BOTTOM, 1.5 )
        goal_button_sizer.Add(self.remove_goal_check, 1, wx.ALIGN_BOTTOM | wx.BOTTOM | wx.LEFT, )

        #reached goal
        reached_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.reached_goal_check = wx.CheckBox(self.panel, wx.ID_ANY, label="Reached goal")
        reached_sizer.Add(self.reached_goal_check, 1, wx.ALIGN_BOTTOM)

        #  Bind add the buttons
        self.Bind(wx.EVT_BUTTON, self.on_money_button_pressed, self.money_1_button)
        self.Bind(wx.EVT_BUTTON, self.on_money_button_pressed, self.money_2_button)
        self.Bind(wx.EVT_BUTTON, self.on_money_button_pressed, self.money_3_button)
        self.Bind(wx.EVT_BUTTON, self.on_money_button_pressed, self.money_4_button)
        self.Bind(wx.EVT_BUTTON, self.on_money_button_pressed, self.money_5_button)
        self.Bind(wx.EVT_BUTTON, self.on_money_button_pressed, self.money_6_button)
        self.Bind(wx.EVT_BUTTON, self.on_money_button_pressed, self.money_7_button)
        self.Bind(wx.EVT_BUTTON, self.on_text_input_button, self.input_button)
        self.Bind(wx.EVT_BUTTON, self.on_confirm, self.confirm_button)
        self.Bind(wx.EVT_BUTTON, self.on_change_button, self.change_button)
        self.Bind(wx.EVT_BUTTON, self.on_add_goal, self.goal_button)
        self.Bind(wx.EVT_BUTTON, self.on_change_sub_type, self.sub_add_btn)
        self.Bind(wx.EVT_BUTTON, self.on_add_subscription, self.sub_confirm)
        self.Bind(wx.EVT_BUTTON, self.on_remove_subscription, self.monthly_remove)


        #Bind graph buttons
        self.Bind(wx.EVT_BUTTON, self.on_show_graph, self.show_graph)

        #  Bind TextCtrl
        self.Bind(wx.EVT_TEXT, self.on_enter_money, self.money_input)
        self.Bind(wx.EVT_TEXT, self.on_enter_goal_value, self.goal_value)
        self.Bind(wx.EVT_TEXT, self.on_subcr_input_value, self.sub_static_value)

        #Bind chechbox
        self.Bind(wx.EVT_CHECKBOX, self.on_remove_goal, self.remove_goal_check)
        self.Bind(wx.EVT_CHECKBOX, self.on_reached_goal, self.reached_goal_check)

        # Set Sizers
        money_sizer_4.Add(self.input_button)

        top_sizer.Add(change_sizer, 1, wx.ALIGN_RIGHT | wx.RIGHT, 40)
        top_sizer.Add(money_sizer_1, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(money_sizer_2, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(money_sizer_3, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(money_sizer_4, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(text_sizer, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(show_graph_sizer, 1, wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM, 20)

        #Subscription sizers
        top_sizer.Add(sub_sizer_1, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(sub_sizer_2, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(sub_sizer_3, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(sub_sizer_4, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(sub_sizer_4_5, 1, wx.ALIGN_RIGHT)
        top_sizer.Add(sub_sizer_5, 1, wx.ALIGN_RIGHT)

        #Goal sizers
        top_sizer.Add(goal_value_sizer, 1, wx.ALIGN_LEFT)
        top_sizer.Add(goal_name_sizer, 1, wx.ALIGN_LEFT)
        top_sizer.Add(reached_sizer, 1, wx.LEFT, 287)
        top_sizer.Add(goal_button_sizer, 1, wx.ALIGN_LEFT | wx.LEFT, 70)


        self.SetSizer(top_sizer)

    def on_change_button(self, event):
        self.money_1_button.myvalue = self.money_1_button.myvalue * -1
        self.money_1_button.SetLabel(str(self.money_1_button.myvalue) + "€")

        self.money_2_button.myvalue = self.money_2_button.myvalue * -1
        self.money_2_button.SetLabel(str(self.money_2_button.myvalue) + "€")

        self.money_3_button.myvalue = self.money_3_button.myvalue * -1
        self.money_3_button.SetLabel(str(self.money_3_button.myvalue) + "€")

        self.money_4_button.myvalue = self.money_4_button.myvalue * -1
        self.money_4_button.SetLabel(str(self.money_4_button.myvalue) + "€")

        self.money_5_button.myvalue = self.money_5_button.myvalue * -1
        self.money_5_button.SetLabel(str(self.money_5_button.myvalue) + "€")

        self.money_6_button.myvalue = self.money_6_button.myvalue * -1
        self.money_6_button.SetLabel(str(self.money_6_button.myvalue) + "€")

        self.money_7_button.myvalue = self.money_7_button.myvalue * -1
        self.money_7_button.SetLabel(str(self.money_7_button.myvalue) + "€")

        if "Add:" in str(self.text_money.GetValue()):
            self.text_money.SetValue("Remove:")
        else:
            self.text_money.SetValue("Add:")

        if self.input_button.myvalue == 1:
            self.input_button.SetLabel("-")
            self.input_button.myvalue = self.input_button.myvalue * -1
        else:
            self.input_button.SetLabel("+")
            self.input_button.myvalue = self.input_button.myvalue * -1

    def on_money_button_pressed(self, event):
        value = event.GetEventObject().myvalue
        print("Button value: ", value)
        self.value_to_add = self.value_to_add + int(value)
        static_text = "Add: " + str(self.value_to_add)
        self.text_money.SetValue(static_text)

    def on_enter_money(self, event):
        value = self.money_input.GetValue()
        try:
            test = int(value)
        except ValueError:
            print("Pls enter a valid number")
            self.money_input.SetValue("")

    def on_text_input_button(self, event):
        try:
            value = self.money_input.GetValue()
            self.value_to_add = self.value_to_add + int(value)
            static_text = "Add: " + str(self.value_to_add)
            self.text_money.SetValue(static_text)
            self.money_input.SetValue("")
        except ValueError:
            pass

    def on_confirm(self, event):
        print("Added:", self.value_to_add)
        value_manager.add_new_value(int(self.value_to_add))
        self.text_money.SetValue("Add:")
        self.status_bar.PushStatusText("Value updated", 1)

    def on_show_graph(self, event):
        if self.show_graph.graph_shown == False:
            self.show_graph.graph_shown = True
            self.status_bar.PushStatusText("Showing Graph", 1)
            graph.graph_draw.draw_graph(value_manager.get_value_week()[1], value_manager.get_value_week()[0],
                                        value_manager.goal_values_all())
            self.show_graph.graph_shown = False
        else:
            pass

    def on_enter_goal_value(self, event):
        value1 = self.goal_value.GetValue()
        try:
            test = int(value1)
        except ValueError:
            if '-' in (self.goal_value.GetValue()):
                pass
            else:
                print("Pls enter a valid number")
                self.goal_value.SetValue("")

    def on_add_goal(self, event):
        if self.goal_name.GetValue() and self.goal_value.GetValue():

            value_manager.set_goal(self.goal_value.GetValue(), self.goal_name.GetValue())
            self.goal_name.SetValue("")
            self.goal_value.SetValue("")
            self.status_bar.PushStatusText("Added goal", 1)

        else:
            pass

    def on_remove_goal(self, event):
        self.remove_goal_check.SetValue(False)
        drop_value = self.remove_goal_drop.GetValue()
        if drop_value == "":
            pass
        else:
            value_manager.remove_goal(drop_value)
            try:
                new_set = value_manager.get_goal_names()[0]
                self.remove_goal_drop.SetValue(new_set)
            except:
                self.remove_goal_drop.SetValue("")

            self.status_bar.PushStatusText("Removed goal", 1)

    def on_reached_goal(self, event):

        self.reached_goal_check.SetValue(False)
        drop_value = self.remove_goal_drop.GetValue()
        if drop_value == "":
            pass
        else:
            goal_value = int(value_manager.get_goal_value(drop_value)[0]) * -1
            value_manager.add_new_value(goal_value)
            value_manager.remove_goal(drop_value)
            try:
                new_set = value_manager.get_goal_names()[0]
                self.remove_goal_drop.SetValue(new_set)
            except:
                self.remove_goal_drop.SetValue("")
            self.status_bar.PushStatusText("Congratulations on reaching your goal, money updated", 1)

    def on_subcr_input_value(self, event):
        value = self.sub_static_value.GetValue()
        try:
            test = int(value)
        except ValueError:
            print("Please enter a valid number")
            self.sub_static_value.SetValue("")

    def on_change_sub_type(self, event):
        if self.sub_add_btn.GetLabel() == "+":
            self.sub_add_btn.SetLabel("-")
        else:
            self.sub_add_btn.SetLabel("+")
        self.sub_add_btn.type = self.sub_add_btn.type * -1

    def on_add_subscription(self, event):
        if self.sub_add_btn.type == 1:
            value = self.sub_static_value.GetValue()
            print("add")
        elif self.sub_add_btn.type == -1:
            value = int(self.sub_static_value.GetValue()) * -1
            print("ziehe ab")
        value_manager.add_monthly_subscriptions(value, self.sub_price_input.GetValue())
        self.sub_price_input.SetValue("")
        self.sub_static_value.SetValue("")

    def on_remove_subscription(self, event):
        subcrp_name = self.monthly_subscr_box.GetValue()
        if subcrp_name == "":
            pass
        else:
            index = str(subcrp_name).find(":")
            subcrp_name = subcrp_name[0:7]
            print(subcrp_name, index)
            value_manager.remove_monthly_subscription(subcrp_name)
            self.monthly_subscr_box.SetValue("")


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainGUI(None).Show()
    app.MainLoop()
