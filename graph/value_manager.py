import datetime
from datetime import date
from datetime import datetime, timedelta
import csv
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.dirname(file_dir)
file_name = base_path + "\dependencies\graph_values.csv"
working_file_name = base_path + "\dependencies\working_graph_values.csv"
monthly_file = base_path + "\dependencies\monthly_values.csv"
goal_file = base_path + "\dependencies\goal_values.csv"
icon_file = base_path + "\dependencies\icon.png"
today = datetime.today().strftime('%d/%m/%Y')


def check_for_today(given_date, y_value):
    """Falls das gegebene Datum in der save_file ist, rufe change_today_value() auf, fallst nicht, return True"""
    with open(file_name, 'r') as r_file:
        save_reader = csv.reader(r_file)
        for save_row in save_reader:
            try:
                if save_row[0] == given_date:
                    return True
                else:
                    pass
            except IndexError:
                pass
        return False


def change_today_value(old_y, add_y):
    """überschreibe den Wert in Working File"""

    new_y_value = int(old_y) + int(add_y)

    with open(working_file_name, 'w', newline='') as ww_file:
        #  set working file_value
        ww_writer = csv.writer(ww_file, delimiter=',')
        ww_writer.writerow([today, new_y_value])

    with open(working_file_name, 'r') as wr_file:
        #  get working_file value
        wr_reader = csv.reader(wr_file, delimiter=',')
        for row in wr_reader:
            wr_value = row[1]

    with open(file_name, 'r') as lr_file:
        #  get last row of long_file and delete it
        lr_rows = lr_file.readlines()
        ok_lines = lr_rows[:-2]
        cleaned_lines = []
        for item in ok_lines:
            if '/' in item:
                item = item.replace('\n', '')
                sep = ','
                list_inner = []
                date_c = str(item.split(sep, 1)[0])
                value_c = str(item.split(sep, 1)[1])
                list_inner.append(date_c)
                list_inner.append(value_c)

                cleaned_lines.append(list_inner)

            else:
                del item

    with open(file_name, 'w') as lw_file:
        # Append work_file to long_file
        lw_writer = csv.writer(lw_file)
        for item in cleaned_lines:
            date = str(item[0])
            value = str(item[1])
            lw_writer.writerow([date, value])

    with open(file_name, 'a')as la_file:
        la_writer = csv.writer(la_file)
        la_writer.writerow([today, wr_value])

    return wr_value


def add_new_value(y_value):

    """Give y-Value, add x-value(Date) and append it to the file"""
    checker = check_for_today(today, y_value)
    dateformat = "%d/%m/%Y"
    if not checker:
        #  if a new Date is added
        with open(file_name, 'r') as def_check_file:
            def_check = csv.reader(def_check_file)
            for row in def_check:
                try:
                    last_date = row[0]
                except IndexError:
                    pass
            try:
                last_date = datetime.strptime(last_date, dateformat)
                today_date = datetime.strptime(today, dateformat)

                delta = (today_date - last_date).days

                #Füge default Werte hinzu

                while delta > 0:
                    add_default_value(y_value)
                    delta -= 1
            except UnboundLocalError:
                with open(file_name, 'a') as first:
                    first_writer = csv.writer(first, delimiter=',')
                    first_writer.writerow([today, y_value])


    else:
        with open(working_file_name, 'r') as wr_file:
            wr_reader = csv.reader(wr_file, delimiter=',')
            for row in wr_reader:
                try:
                    wf_value = row[1]
                except IndexError:
                    pass

            change_today_value(y_value, wf_value)
        # if date is already in file


def add_default_value(y_value):

    dateformat = "%d/%m/%Y"
    with open(file_name, 'r')as last_row_file:
        last_row_reader = csv.reader(last_row_file)
        for row in last_row_reader:
            try:
                last_date = row[0]
            except IndexError:
                pass
        last_date = datetime.strptime(str(last_date)[0:10], dateformat)
        new_date = last_date + timedelta(days=1)

        new_year = str(new_date)[0:4]
        new_month = str(new_date)[5:7]
        new_day = str(new_date)[8:10]
        new_date = str(new_day) + "/" + str(new_month) + "/" + str(new_year)

        if new_date == today:
            with open(file_name, 'a') as a_file:
                a_writer = csv.writer(a_file, delimiter=',')
                a_writer.writerow([new_date, y_value])

        else:

            with open(file_name, 'a') as a_file:
                a_writer = csv.writer(a_file, delimiter=',')
                a_writer.writerow([new_date, 0])


def get_value_week():
    """Returns two lists list of lists of all dates, and a second of all values"""

    # todolist: Nur einmal den gleiche Tag zurückgeben, bei gleich Tag, werte addieren
    with open(file_name, 'r') as r_file:
        f_reader = csv.reader(r_file)
        values_week = []
        y_values = []
        date_values = []

        today_day = int(str(today).rsplit('/', 2)[0])
        today_month = int(str(today).rsplit('/', 2)[1])
        today_year = int(str(today).rsplit('/', 2)[2])
        today_date = date(today_year, today_month, today_day)

        for row in f_reader:
            try:
                then = row[0]
                then_day = int(str(then).rsplit('/', 2)[0])
                then_month = int(str(then).rsplit('/', 2)[1])
                then_year = int(str(then).rsplit('/', 2)[2])
                then_date = date(then_year, then_month, then_day)

                if (today_date - then_date).days <= 7:
                    if str(row[1]).startswith("-"):
                        str(row[1]).replace("-", "")

                        y_values.append(int(row[1]))
                        date_values.append(then)
                    else:
                        y_values.append(int(str(row[1])))
                        date_values.append(then)
            except IndexError:
                pass

        values_week.append(date_values)
        values_week.append(y_values)
        return values_week


def add_monthly_subscriptions(sub_value, sub_name):
    """positive Value: Add money, negative value: remove money"""
    with open(monthly_file, 'a') as month_file:
        month_writer = csv.writer(month_file, delimiter=',')
        try:
            month_writer.writerow([today, int(sub_value), str(sub_name)])

        except ValueError:
            print("Add monthly subscription: Wrong datetype at writerow")

def remove_monthly_subscription(remove_name):
    to_add_lines = []
    with open(monthly_file, 'r') as monthly:
        monthly_reader = csv.reader(monthly)
        for line in monthly_reader:
            try:
                monthly_date = line[0]
                monthly_value = line[1]
                monthly_name = line[2]

                if monthly_name == remove_name:
                    pass
                else:
                    pair = []
                    pair.append(monthly_date)
                    pair.append(monthly_value)
                    pair.append(monthly_name)
                    to_add_lines.append(pair)
            except IndexError:
                del line

    with open(monthly_file, 'w') as monthly2:
        monthly_writer = csv.writer(monthly2)

        item_number = 0
        for value in to_add_lines:
            try:
                monthly_add_date = value[0]
                monthly_add_value = value[1]
                monthly_add_name = value[2]
                monthly_writer.writerow([monthly_add_date, monthly_add_value, monthly_add_name])

                item_number += 1

            except IndexError:
                pass


def check_monthly_subscriptions():

    with open(monthly_file, 'r')as month_file:
        with open(working_file_name, 'r') as w_file:
            month_reader = csv.reader(month_file)
            working_reader = csv.reader(w_file)

            for mrow in month_reader:
                for wrow in working_reader:
                    try:
                        if mrow[0] == wrow[0]:
                            new_value = int(wrow[1]) + int(mrow[1])
                            with open(working_file_name, 'w') as in_w:
                                ww_writer = csv.writer(in_w)
                                ww_writer.writerow([today, new_value ])
                                print("Month baby")
                    except IndexError:
                        pass


def get_monthly_subscriptions():
    """Return the name of all subcriptions"""
    with open(monthly_file, 'r') as get_month:
        check_reader = csv.reader(get_month)
        return_names = []
        for row in check_reader:
            try:
                value = str(row[2]) + ": " + str(row[1])
                return_names.append(value)
            except IndexError:
                pass
        return return_names


def set_goal(money_goal, goal_name):
    """Add a goal to the csv-file"""
    with open(goal_file, 'a')as goal_f:
        goal_writer = csv.writer(goal_f, delimiter=',')
        goal_writer.writerow([today, money_goal, goal_name])


def remove_goal(remove_name):
    """Remove a goal from the csv-list"""
    to_add_lines = []
    with open(goal_file, 'r') as r_goal:
        goal_reader = csv.reader(r_goal)
        for line in goal_reader:
            try:
                goal_date = line[0]
                goal_value = line[1]
                goal_name = line[2]

                if goal_name == remove_name:
                    pass
                else:
                    pair = []
                    pair.append(goal_date)
                    pair.append(goal_value)
                    pair.append(goal_name)
                    to_add_lines.append(pair)
            except IndexError:
                del line

    with open(goal_file, 'w') as w_goal:
        goal_writer = csv.writer(w_goal)

        item_number = 0
        for value in to_add_lines:
            try:
                goal_add_date = value[0]
                goal_add_value = value[1]
                goal_add_name = value[2]
                goal_writer.writerow([goal_add_date, goal_add_value, goal_add_name])

                item_number +=1

            except IndexError:
                pass


def goal_values_all():
    """Returns a list of the goal-values"""
    return_value = []
    with open(goal_file, 'r') as get_goal:
        get_reader = csv.reader(get_goal)
        for line in get_reader:
            try:
                inner = []
                value = line[1]
                name = line[2]
                inner.append(name)
                inner.append(value)
                return_value.append(inner)

            except IndexError:
                pass

        return return_value


def get_goal_values():
    """Returns a list of the goal-values"""
    return_value = []
    with open(goal_file, 'r') as get_goal:
        get_reader = csv.reader(get_goal)
        for line in get_reader:
            try:
                value = line[1]
                return_value.append(value)

            except IndexError:
                pass

        return return_value


def get_goal_value(goal_name):
    """Returns a list of the goal-values"""
    return_value = []
    with open(goal_file, 'r') as get_goal:
        get_reader = csv.reader(get_goal)
        for line in get_reader:
            try:
                if line[2] == goal_name:
                    value = line[1]
                    return_value.append(value)
                else:
                    pass

            except IndexError:
                pass
        return return_value


def get_goal_names():
    return_name = []
    with open(goal_file, 'r') as get_goal:
        get_reader = csv.reader(get_goal)
        for line in get_reader:
            try:
                name = line[2]
                return_name.append(name)

            except IndexError:
                pass

        return return_name


def get_icon_file():
    return icon_file


