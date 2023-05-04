# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Continue button
driver.find_element(By.ID, 'continue')

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-in link
driver.find_element(By.ID,'ap-other-signin-issues-link')

# Create your amazon account button
driver.find_element(By.ID, 'createAccountSubmit')


# Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

# Privacy notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")