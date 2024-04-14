import time
status = "run"

def main(WebDri):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import random
    # ==============================================================+
    # --find folder holding all crypto bots------
    # -------------------------------------------
    try:        
        print("Locating Cryto bots folder...")
        time.sleep(3)

        title_tabs = WebDri.find_elements(By.CLASS_NAME, "Tab_inner")
        for tab in title_tabs:
            if "Crypto" in tab.text:
                # crypto_tab = title_tabs[1]
                crypto_tab = tab
        crypto_tab.click()
                
        print(f"Located crypto-bot folder.'")
        time.sleep(1)
    except Exception as e:
        print("Unable to find-click crypto bot folder,\n Chat folder may not be visible, also ensure folder name contains 'Crypto', exclusively.\n  Error message: ", e)
    # -------------------------------------------
        
    # --find target crypto mining chat (PocketFi)
    # -------------------------------------------    
    try:
        time.sleep(1)
        cryptoChat_list = WebDri.find_element(By.CSS_SELECTOR, ".chat-list.custom-scroll.Transition_slide.Transition_slide-active")
        chats = cryptoChat_list.find_elements(By.CSS_SELECTOR, ".ListItem-button")
        print(f"{len(chats)} Chats found in Crypto bot chat list, locating target Bot-chat...")

        targetCryptoMine = "PocketFi"
        for chat in chats:
            chatName = chat.find_element(By.CSS_SELECTOR, ".fullName.AS54Cntu").text
            if targetCryptoMine in chatName:
                targetChat = chat
                break       
        # PocketFi_pinned = chats[0]
        # PocketFi_pinned.click()
        targetChat.click()
        
        print(f"Located {targetCryptoMine} Bot chat")
        time.sleep(1)
    except Exception as e:
        print("Unable to find-click target crypto bot chat,\n Chat may not be visible, ensure chat is present and there are no duplicate names.\n  Error message: ", e)
    # -------------------------------------------
    
    # -------------------------------------------
    for _ in range(10):
        # -------------------------------------------  
        # --highlight messages within chat, access the minning web app
        # -------------------------------------------
        try:
            time.sleep(1)
            message_container = WebDri.find_element(By.CSS_SELECTOR, ".messages-container")
            messages = message_container.find_elements(By.CSS_SELECTOR,".Message.message-list-item.first-in-group.allow-selection.last-in-group.has-inline-buttons.open.shown")

            last_message = messages[-1]
            action_btns = last_message.find_element(By.CSS_SELECTOR, ".InlineButtons")
            mineAction_btn = action_btns.find_elements(By.CSS_SELECTOR,".Button.tiny.primary.has-ripple")[0]
            mineAction_btn.click()

            print("Entering mining app...")   
            time.sleep(3)
        except Exception as e:
            print("Error entering mine, ensure messages are visible.\n Error message : ", e)
        # -------------------------------------------

        # --handling new user dialogue---------------
        # -------------------------------------------
        try:
            time.sleep(3)
            popDialogue = WebDri.find_element(By.CSS_SELECTOR, ".modal-dialog")
            if popDialogue:
                acceptPMPT = popDialogue.find_elements(By.CSS_SELECTOR, ".Button.confirm-dialog-button.default.primary.text")[0]
                acceptPMPT.click()
                print("Accepted to share device information, proceeding...")
                time.sleep(30)
                enterMining = WebDri.find_element(By.CSS_SELECTOR, ".Button.Os96PEjQ.C8aMayAw.default.primary")
                enterMining.click()
                time.sleep(2)
            else:
                print("New user dialogue not present, proceeding to mining...")        
        except Exception as e:
            print("Error handling new user dialogue.\n Error message : ", e)
        # -------------------------------------------

        # --CLAIMING TOKENS--------------------------
        # -------------------------------------------
        try:  
            iframe = WebDri.find_element(By.XPATH, '//*[@id="portals"]/div[2]/div/div/div[2]/div[2]/iframe')
            WebDri.switch_to.frame(iframe)

            claimContainer = WebDri.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[3]/div[1]')
            if claimContainer:
                claimBTN = claimContainer.find_element(By.TAG_NAME, "button")               
                claimBTN.click()
                if "Claim SWITCH" in claimBTN.text:
                    print("Token claimed :)")
                else:
                    print("Couldnt claim token, intercepted by news")
                    # couldntClaim = True
                time.sleep(2)

                WebDri.switch_to.default_content()
                mineDialogueClose = WebDri.find_element(By.XPATH, '//*[@id="portals"]/div[2]/div/div/div[2]/div[1]/button')
                time.sleep(1)
                print("Exiting minning portal")
                mineDialogueClose.click()            
                # time.sleep(1200)
            else:
                print("Minning frame not visible, retrying...")
        except Exception as e:
            print("Error claiming tokens.\n Error message :", e)
        # -------------------------------------------

        # -------------------------------------------
        # nextClickSecs = random.randint(7200, 14400)
        nextClickSecs = 1200        
        print(f"refreshing...waiting  {nextClickSecs} seconds to reclaim tokens")    
        time.sleep(nextClickSecs)
        # -------------------------------------------
    # -------------------------------------------
    # ==============================================================+
# while true 
    '''if blah
    claimBTN
    sleep 6000yrs
    else break
'''
            