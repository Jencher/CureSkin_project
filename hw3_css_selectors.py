# Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

# Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your name input field
driver.find_element(By.ID, 'ap_customer_name')

# email field
driver.find_element(By.ID, 'ap_email')

# password field
driver.find_element(By.ID, 'ap_password')

# passwords must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, 'div.a-box.a-alert-inline.a-alert-inline-info')

# Re-enter password  input field
driver.find_element(By.ID, 'ap_password_check')

# Create your Amazon account button(Continue)
driver.find_element(By.ID, 'continue')

# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

# Sign in
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin?']")