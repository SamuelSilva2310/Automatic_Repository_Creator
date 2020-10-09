from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#LOGIN TO GITHUB
def login():
   
    USERNAME = "" #INSERIR USERNAME <-----------------------------------------------------------------------------
    PASSWORD = "" #INSERIR PASSWORD <-----------------------------------------------------------------------------

    sign_In_page = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
    sign_In_page.click()
    
   
    try:
        ##GET EVERY ELEMENT
        username_fill = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )

        password_fill = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        
        log_in_Button = driver.find_element_by_name("commit")

        username_fill.clear()
        password_fill.clear()

        username_fill.send_keys(USERNAME)
        password_fill.send_keys(PASSWORD)

        log_in_Button.click()
    
    except:
        print("Failed in LOGIN function!!!")
        

#NAVIGATE THE MAIN MENU
def mainMenu():

    try:
        dropMenu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[7]/details/summary/span[2]"))
        )
        dropMenu.click()

        Repositories_Button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[7]/details/details-menu/a[2]"))
        )
        Repositories_Button.click()
    except:
        print("Failed in MAInMENU")

#NAVIGATE THE REPOSITORY PAGE
def RepositoryPage():
     
    try:
        new_Button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[1]/form/div[2]/a'))
        )
        new_Button.click()
    except:
        print("Failed IN REPOSITORY PAGE")


#CREATE THE NEW REPOSITORY
def newRepository(name, desc):
    
    try:

        ##GET EVERY ELEMENT

        name_Field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'repository_name'))
        )

        description_Field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'repository_description'))
        )

        visibility = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'repository_visibility_public'))
        )

        create_button = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')

        ##PERFORM ACTIONS

        name_Field.clear()
        description_Field.clear()

        name_Field.send_keys(name)
        description_Field.send_keys(desc)

       
        visibility.click()

       

        create_Action = ActionChains(driver)
        create_Action.move_to_element(create_button)
        create_Action.click()
        create_Action.perform()
        
    except:
        print("Failed in CREATE REPOSITORY")
 


   
##RUN CODE

#ASK FOR THE NAME AND DESCRIPTION

name_Repository = input("\tName of Repository: ")
print("\n")
desc_repository = input("\tDescription of Repository: ")

#Create Driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#GET WEBPAGE
driver.get("https://github.com/")
driver.maximize_window()

if __name__ == "__main__":
    
    login()
    mainMenu()
    RepositoryPage()
    newRepository(name_Repository,desc_repository)
 
 