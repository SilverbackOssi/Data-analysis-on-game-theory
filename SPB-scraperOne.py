# import relevant modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time
import pandas as pd

#initialize webdriver on private browsing mode
options = Options()
''' options.headless= True
 options.add_argument('window-size=1600x900')'''
options.add_argument("inprivate")
web_driver = webdriver.Edge(options = options)

# get result page URL
url = 'https://virtual-games.virtustec.com/desktop-v4/default/?checkScroll=true&containerId=golden-race-desktop-app&profile=sportybet-dark&hwId=49690d2f-0517-46ff-bd66-6aedd9958826&showHeader=true#/scheduled/league/history'
web_driver.get(url) 
# wait for page to load (10sec)
time.sleep(10)
web_driver.maximize_window()


# =======================================================================================================================================+
# --------------------------------------------------------------------------------------------------------------------------------------+
leagueTitles = {
    1 : 'Germany',
    'Germany' : 'German',
    2 : 'Italy',
    'Italy' : 'Italian',
    3 : 'England',
    'England' : 'English',
    4 : 'France',
    'France' : 'French',
    5 : 'Spain',
    'Spain': 'Spanish'
}
# define select_league() function
def select_league(league : str):
    time.sleep(5)
 
    titleMenu_list_length = 0
    while titleMenu_list_length == 0 :
        title_menu = WebDriverWait(web_driver,300).until(EC.element_to_be_clickable((By.CLASS_NAME,"menu")))
        time.sleep(1) 
        titles = title_menu.find_elements(By.CSS_SELECTOR,".item.ng-star-inserted")
        titleMenu_list_length = len(titles)
        time.sleep(1)

    for title in titles:
        league_title = title.text
        if league in league_title:
            title.click()

# define function to navigate page to specific date
def filter_to_date(webDriver, date):
    time.sleep(1)
    web_driver.execute_script("arguments[0].scrollTop = 0 ", web_driver.find_element(By.CLASS_NAME, "html-normal"))
    # reference calender
    ref_cal = {
        '01': 'january',
        '02': 'february',
        '03': 'march',
        '04': 'april',
        '05':'may',
        '06': 'june',
        '07': 'july',
        '08': 'august',
        '09': 'september',
        '10':'october',
        '11': 'november',
        '12': 'december'
    }
    # ------------------------------------------------------------+
    # read date in parameter,   format '28/03/2024 20:46'
    # -> separate into time and date
    dateItems = date.split(' ')
    Date = dateItems[0]
    Time = dateItems[1]
    # -> separate time to hours and minutes
    timeItems = Time.split(':')
    hours = timeItems[0]
    minutes = timeItems[1]
    # -> separate date to day and month
    # DateItems
    day, month, year= Date.split('/')
    #  = DateItems[0]
    #  = DateItems[1]
    month = ref_cal.get(month)
    month = month.upper()
    # ---------------------------------------------------------------+
    # navigate to month
    monthDisplay_present = webDriver.find_element(By.CSS_SELECTOR,'.ui-datepicker-month.ng-tns-c4-1.ng-star-inserted').text
    while month not in monthDisplay_present:
        # one step back (never a need to step forward)
        monthNav_back = webDriver.find_element(By.CSS_SELECTOR,".ui-datepicker-prev.ui-corner-all.ng-tns-c4-1.ng-star-inserted")
        monthNav_forward = webDriver.find_element(By.CSS_SELECTOR,".ui-datepicker-next.ui-corner-all.ng-tns-c4-1.ng-star-inserted")
        monthNav_back.click()
        time.sleep(3)
        # re-read display
        monthDisplay_present = webDriver.find_element(By.CSS_SELECTOR,'.ui-datepicker-month.ng-tns-c4-1.ng-star-inserted').text
    # ---------------------------------------------------------------+
    # navigate to day 
    calender_table = webDriver.find_element(By.CSS_SELECTOR,".ui-datepicker-calendar")
    day_containers = calender_table.find_elements(By.CSS_SELECTOR,".ui-state-default.ng-tns-c4-1.ng-star-inserted")
    # ->loop through calender
    print(f"navigating to {date} as date...")
    print(f"navigating to {day}th...")
    for item in day_containers:
        dayHighlighted = item.text
        if dayHighlighted == day:
            item.click() 
    # ---------------------------------------------------------------+   
    # navigate to hour. read-> compare -> navigate -> re-read
    hours_picker = webDriver.find_element(By.CSS_SELECTOR,".ui-hour-picker")
    hour_elements = hours_picker.find_elements(By.CSS_SELECTOR,".ng-tns-c4-1")
    hoursDisplay_present = hour_elements[2].text
    print(f"navigating to {hours} hours...")
    while int(hoursDisplay_present) != int(hours):
        # print(f"displayed : {hoursDisplay_present} VS ref-hour : {hours} \n")
        hour_elements = hours_picker.find_elements(By.CSS_SELECTOR,".ng-tns-c4-1")
        hoursNav_increase = hour_elements[0]
        hoursNav_decrease = hour_elements[3]
        # -----------------------------------------------
        # print(f"current hour displayed: {hoursDisplay_present}, navigating to {hours}... condition as int -> {int(hoursDisplay_present)} VS {int(hours)}")
        if (int(hoursDisplay_present)) > (int(hours)):
            hoursNav_decrease.click()
        elif (int(hoursDisplay_present)) < (int(hours)):
            hoursNav_increase.click()
        time.sleep(1)
        hoursDisplay_present = hour_elements[2].text
        # -----------------------------------------------
    # ---------------------------------------------------------------+
    # navigate to minutes
    minutes_picker = webDriver.find_element(By.CSS_SELECTOR,".ui-minute-picker")
    minute_elements = minutes_picker.find_elements(By.CSS_SELECTOR,".ng-tns-c4-1")
    minutesDisplay_present = minute_elements[2].text
    print(f"navigating to {minutes} minutes...")
    while int(minutesDisplay_present) != int(minutes):
        minute_elements = minutes_picker.find_elements(By.CSS_SELECTOR,".ng-tns-c4-1")
        minutesNav_increase = minute_elements[0]
        minutesNav_decrease = minute_elements[3]
        # -------------------------------------------------
        # print(f"current minute displayed: {minutesDisplay_present}, navigating to {minutes}... condition as int -> {int(minutesDisplay_present)} VS {int(minutes)}")
        if (int(minutesDisplay_present)) > (int(minutes)):
            minutesNav_decrease.click()
        elif (int(minutesDisplay_present)) < (int(minutes)):
            minutesNav_increase.click()
        time.sleep(1)
        minutesDisplay_present = minute_elements[2].text
        # ------------------------------------------------
    # -----------------------------------------------------------------+
    # click filter
    time.sleep(1)
    filter_action_btn = webDriver.find_element(By.CSS_SELECTOR,".btn.btn-lg.btn-block.search-calendar")
    filter_action_btn.click()
    # ------------------------------------------------------------------+
    # scroll into content
    web_driver.execute_script("arguments[0].scrollTop += 200", web_driver.find_element(By.CLASS_NAME, "html-normal"))
    time.sleep(1)           

# managing date inconsistency
def date_hourCleaner(dateDisplayed, targetDate):
    # ----------------------------------------
    # parsing dates
    Displayed_date, Displayed_time = dateDisplayed.split(" ")
    Displayed_hour, Displayed_minute = Displayed_time.split(":")
    Displayed_day, Displayed_month, Displayed_year = Displayed_date.split("/")    
    targetDate, target_time = targetDate.split(" ")
    target_hour, target_minute = target_time.split(":")
    target_day, target_month, target_year = targetDate.split("/")
    # --------------------------------------------------
    target_hour = int(target_hour)
    target_day = int(target_day)
    Displayed_hour = int(Displayed_hour)
    # ------------------------------------------------       
    # diff = absDisplayed_hour - int(target_hour))
    # diffD =  abs(int(Displayed_day) - int(target_day))
    # print(f"difference in hours: {diff}")
    # print(f"difference in days: {diffD}")
    # ------------------------------------------------
    if target_hour == 0 or target_hour == 23:
        if target_hour == 0 and Displayed_hour== 1:
            target_hour = 23
            target_day += 1
        elif target_hour == 0 and Displayed_hour== 23:
            target_hour += 1

        if target_hour == 23 and Displayed_hour== 0:
            target_hour -= 1
        elif target_hour == 23 and Displayed_hour== 22:
            target_hour = 0
            target_day += 1   
    else:
        target_hour = target_hour + 1 if (target_hour > Displayed_hour) else target_hour - 1
    # -----------------------------------------------
    # pass back into string for ref_date   
    print(target_hour, target_day)
    target_hour = f"{int(target_hour):02d}" 
    target_day = f"{int(target_day):02d}"
    target_time = ":".join([target_hour,target_minute])
    targetDate = "/".join([target_day, target_month, target_year])
    new_date = " ".join([targetDate,target_time])
    # ==============================================
    return new_date

# =======================================================================================================================================+

# ---M A I N------------------------------------------+
# ----------------------------------------------------+
with open("SPBscrape_sessions.txt", "r") as file:
    sessionID = file.read()
    if not sessionID:
        sessionID = 0
    currentSession = int(sessionID) + 1
with open("SPBscrape_sessions.txt", "w") as file:
    file.write(str(currentSession))
# --------------------------------------------------
all_Weeks = {
            'league_Name' : [],
            'Week_number' : [],
            'Week_date' : []
        }
# ------------------------------------------------
r = 1
# --------------------------------------------------
while True:
    # wait till presence of league data-> 6mins
    league_is_visible = WebDriverWait(web_driver,360).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".event-block-game"),'Football League:'))
    if not league_is_visible:
        print("LOC1 : Data not visible, exiting...")
        break
    else:
        # access previously scrapped info
        with open("last-date.txt", "r") as file:
            last_info = file.read()
            last_info = last_info.split('-')
            recent_date = last_info[0]
            recent_league = last_info[1]
        ref_date = recent_date
        ref_date = "30/03/2024 00:01"
        # ref_date = "30/03/2024 23:10"

        # select league to scrape
        leagueName = leagueTitles.get(recent_league)
        print(f'We are scraping the {leagueName} League...')
        select_league(recent_league)
        # --------------------------------------------------------
        # scrape data
        while True:
            # navigate to reference date
            filter_to_date(web_driver, ref_date)

            # ensure visibility
            league_is_visible = WebDriverWait(web_driver,360).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".event-block-game"),'Football League:'))
            if not league_is_visible:
                if r < 3:
                    print("Data not visible, retrying...")
                    web_driver.refresh()
                    r += 1
                else:
                    print("LOC2 : Data not visible, exiting...")
                break
            else:
                # confirm page data corresponds to ref_date
                topMost_week = web_driver.find_element(By.XPATH,'//*[@id="main-content"]/app-event-results-history/div/div[2]/div[2]/div[1]/div/div[1]/span[5]').text
                while topMost_week != ref_date:
                    print("Attempting to manage date inconsistency...")
                    print(f"Target date: {ref_date}")
                    # ---------------------------------------------------------------------                    
                    ADJref_date = date_hourCleaner(topMost_week, ref_date)
                    print(f"navigating to new date as: {ADJref_date}")
                    filter_to_date(web_driver, ADJref_date)
                    # ensure visibility
                    league_is_visible = WebDriverWait(web_driver,360).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".event-block-game"),'Football League:'))
                    if not league_is_visible:
                        print("LOC3 : Data not visible, exiting...")
                        break    
                    topMost_week = web_driver.find_element(By.XPATH,'//*[@id="main-content"]/app-event-results-history/div/div[2]/div[2]/div[1]/div/div[1]/span[5]').text               
                # 5 weeks per page
                week_cards = web_driver.find_elements(By.CSS_SELECTOR,".history-container.ng-star-inserted")
                for i,week in enumerate(week_cards):
                    if i == 0:
                        continue                    
                    else:
                        week_title = week.find_element(By.CSS_SELECTOR,".panel-heading")
                        slotScore_items = week.find_elements(By.CSS_SELECTOR,".football-event-block.clearfix.text-center")
                        # ---------------------------------------------------------------
                        L_Name = week_title.find_element(By.CSS_SELECTOR,".event-block-name.ml-1").text
                        L_Name_p = L_Name.split(' ')
                        W_Number= week_title.find_element(By.CSS_SELECTOR,".event-block-id.ng-star-inserted")
                        W_Number= W_Number.find_element(By.CSS_SELECTOR,".event-block-id.ng-star-inserted").text
                        W_date = week_title.find_element(By.CSS_SELECTOR,".event-block-date").text
                        # ---------------------------------------------------------------
                        all_Weeks['league_Name'].append(L_Name)
                        all_Weeks['Week_number'].append(W_Number)
                        all_Weeks['Week_date'].append(W_date)
                        # --------------------------------------------------------------
                        for i,item in enumerate(slotScore_items):
                            i += 1
                            slot_score_text = item.find_element(By.CSS_SELECTOR,".flex-col.match-result-score.p-1").text
                            home,away = map(int, slot_score_text.split(':'))
                            slot_score = home + away
                            # ------------------------------------------------------------
                            key = f"slot{i}_score"
                            if key not in all_Weeks:
                                all_Weeks[key] = [slot_score]
                            else:
                                all_Weeks[key].append(slot_score)
                            web_driver.execute_script("arguments[0].scrollTop += 100 ", web_driver.find_element(By.CLASS_NAME, "html-normal"))
                            "arguments[0].scrollHeight"
                        # ---------------------------------------------------------------
                        ref_date = W_date
                        # update last-date.txt, format ; 28/03/2024 20:46-England
                        date_stamp = '-'.join([W_date,L_Name_p[0]])
                        with open("last-date.txt", "w") as file:
                            file.write(date_stamp)
                        # ----------------------------------------------------------------
                        df = pd.DataFrame(all_Weeks)
                        df.to_csv(f'{L_Name_p[0]}League_session_day29.csv', sep='\t', index=False)                        
#=============================================================================================================================================================+    
print('Exiting program in 30s...')
time.sleep(30)
web_driver.quit()

# TEST appending data-frame to file as file line