# coding: utf-8
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# Can ask which module to import depending on the change requirement?
from SNOW_Variables import *  
#Need to give list of VIP's on each seperate line
#length = count the line of vips 
#Use for loop using length variable

#File Reader Module
#*******************
browser = webdriver.Firefox()

browser.maximize_window()
browser.get('https://<prod_url>.service-now.com')
time.sleep(10)
#*********************************
	
	#
	#emailElem.send_keys(line)

#for microsoft login
emailid = browser.find_element_by_id('i0116')
emailid.send_keys('<your_SNOW_email_address>')
time.sleep(2)

linkElem = browser.find_element_by_id('idSIButton9')
linkElem.click()
time.sleep(20)
#for dxc login bypass

dxc_mailid = browser.find_element_by_id('passwordInput')
dxc_mailid.send_keys('<your_SNOW_email_password>') 

dxc_submit = browser.find_element_by_id('submitButton')
dxc_submit.click()  
	
time.sleep(50)	

#dxc_mailid = browser.find_element_by_id('sysparm_search')
#dxc_mailid.send_keys('CHG0351346') 
#dxc_submit.click()



change_Elem = browser.find_element_by_id('favorites_tab')
change_Elem.click()
#time.sleep(10)
#It works 
#change_Elem = browser.find_element_by_id('allApps_tab')
#change_Elem.click()

time.sleep(10)
#browser.find_elements_by_xpath('.//span[@class = "gbts"]')
#It Works
#create_new = browser.find_element_by_xpath('//a[@data-id = "933820acdb17af40a8d39ec6db9619a0"]')
create_new = browser.find_element_by_xpath('//html/body/div[5]/div/div/nav/div/div[3]/div/div/magellan-favorites-list/ul/li[6]/div/div[1]/a/div[2]/span')
#/html/body/div[5]/div/div/nav/div/div[3]/div/div/magellan-favorites-list/ul/li[6]/div/div[1]/a/div[2]/span
#/html/body/div[5]/div/div/nav/div/div[3]/div/div/magellan-favorites-list/ul/li[6]/div/div[1]/a/div[1]/div
create_new.click()

time.sleep(10)

##############################
# Switch to frame
#############################
iframe = browser.find_element_by_id('gsft_main')
browser.switch_to.frame(iframe)

time.sleep(10)

#normal_ch = browser.find_element_by_xpath("//div[@class='container-fluid wizard-container']/html/body/form/div[2]/a")
normal_ch = browser.find_element_by_xpath("//html/body/form/div[2]/a")
# /html/body/form/div[2]/a
normal_ch.click()
#####################################


time.sleep(3)
requestor = browser.find_element_by_xpath("//*[@id='sys_display.change_request.u_cr_requester']")
requestor.send_keys(requestor_name)
requestor.send_keys(Keys.TAB)
time.sleep(3)

req_num = browser.find_element_by_xpath("//*[@id='change_request.u_sr_number']")
req_num.send_keys(RITM)
req_num.send_keys(Keys.TAB)
time.sleep(3)

assign_group = browser.find_element_by_xpath("//*[@id='sys_display.change_request.assignment_group']")
assign_group.send_keys(agrp)
assign_group.send_keys(Keys.TAB)
time.sleep(3)

cr_group = browser.find_element_by_xpath("//*[@id='sys_display.change_request.u_cr_owner_group']")
cr_group.send_keys(cgrp)
cr_group.send_keys(Keys.TAB)
time.sleep(3)

change_cate = browser.find_element_by_xpath("//*[@id='sys_display.change_request.u_change_category']")
change_cate.send_keys(ccat)
change_cate.send_keys(Keys.TAB)
time.sleep(2)

configci = browser.find_element_by_xpath("//*[@id='sys_display.change_request.cmdb_ci']")
configci.send_keys(config_item)
configci.send_keys(Keys.TAB)
time.sleep(2)

implementor = browser.find_element_by_xpath("//*[@id='sys_display.change_request.assigned_to']")
implementor.send_keys(imple)
implementor.send_keys(Keys.TAB)
time.sleep(2)

#environ = browser.find_element_by_xpath("//*[@id='sys_select.change_request.u_environment']")
#environ.send_keys(short_des)
#environ.send_keys(Keys.TAB)
cert_value="7ca14a886f9fbd00c423884f8e3ee4cb"
selecta = Select(browser.find_element_by_xpath("//*[@id='sys_select.change_request.u_environment']"))
selecta.select_by_value(cert_value)
time.sleep(2)

short_ch = browser.find_element_by_xpath("//*[@id='change_request.short_description']")
short_ch.send_keys(short_des)
short_ch.send_keys(Keys.TAB)
time.sleep(2)

des_ch = browser.find_element_by_xpath("//*[@id='change_request.description']")
des_ch.send_keys(short_des)
des_ch.send_keys(description)
des_ch.send_keys(Keys.TAB)
time.sleep(5)

####################
#Implementation TAB :
####################


implementation_tab = browser.find_element_by_xpath("//html/body/div[2]/form/div[1]/span[2]/span/span[2]")
implementation_tab.click()

business_ch = browser.find_element_by_xpath("//*[@id='change_request.u_business_driver']")
business_ch.send_keys(business_driver)
#business_ch.send_keys(Keys.TAB)
time.sleep(2)

detail_imp = browser.find_element_by_xpath("//*[@id='change_request.change_plan']")
detail_imp.send_keys(DIP)
time.sleep(2)

final_val_ch = browser.find_element_by_xpath("//*[@id='change_request.u_final_validation']")
final_val_ch.send_keys(final_validation)
time.sleep(2)

no_lower_env_tick = browser.find_element_by_xpath("//*[@id='label.ni.change_request.u_no_low_env']")
no_lower_env_tick.click()
time.sleep(2)

pre_imp_test_ch = browser.find_element_by_xpath("//*[@id='change_request.u_pre_imp_testing']")
pre_imp_test_ch.send_keys(pre_imp_testing)
time.sleep(2)

pot_cust_ch = browser.find_element_by_xpath("//*[@id='change_request.u_potential_customer_impact']")
pot_cust_ch.send_keys(pot_cust_imp)
time.sleep(2)

risk_ch = browser.find_element_by_xpath("//*[@id='change_request.u_risk_and_mitigation']")
risk_ch.send_keys(risk_miti)
time.sleep(2)

com_plan_ch = browser.find_element_by_xpath("//*[@id='change_request.u_communication_plan']")
com_plan_ch.send_keys(comm_plan)
time.sleep(2)

r_leader = browser.find_element_by_xpath("//*[@id='sys_display.change_request.u_responsible_leader']")
r_leader.send_keys(leader)
r_leader.send_keys(Keys.TAB)
time.sleep(2)

capacity_ch = browser.find_element_by_xpath("//*[@id='change_request.u_capacity']")
capacity_ch.send_keys(capacity)
time.sleep(5)

####################
#Backout TAB :
####################

backout_tab = browser.find_element_by_xpath("/html/body/div[2]/form/div[1]/span[6]/span/span[2]")
backout_tab.click()
time.sleep(3)

backout_ch = browser.find_element_by_xpath("//*[@id='change_request.backout_plan']")
backout_ch.send_keys(back_out)
time.sleep(2)

backout_time = browser.find_element_by_xpath("//*[@id='ni.change_request.u_back_out_durationdur_min']")
backout_time.clear()
time.sleep(1)
backout_time.send_keys("30")
time.sleep(2)

req_testing = browser.find_element_by_xpath("//*[@id='change_request.u_required_testing']")
req_testing.send_keys("No")
time.sleep(2)

backimpact_ch = browser.find_element_by_xpath("//*[@id='change_request.u_back_out_impact']")
backimpact_ch.send_keys(back_out_impact)
time.sleep(2)

backval_ch = browser.find_element_by_xpath("//*[@id='change_request.u_back_out_validation']")
backval_ch.send_keys(back_out_val)
time.sleep(10)

#working submit button
submit_butn = browser.find_element_by_xpath("//*[@id='sysverb_insert_bottom']")
submit_butn.click()

#Submit button
#//*[@id="sysverb_insert_bottom"]
