# Test Case: TC-AUTH-002 - User Login with Invalid Username

## Test Information
- **Test Suite:** Authentication
- **Test Environment:** Production (Edge 143.0.3650.96, Windows 11 Pro)
- **Status:** Passed

---

## Preconditions
- User does exist in the system
- User has an invalid username: invalid_username,
- User has a valid password: secret_sauce
- Browser is open and on the login page

---

## Steps
1. Navigate to https://www.saucedemo.com/
2. Enter "invalid_username" in the username field
3. Enter "secret_sauce" in the password field
4. Click the "Login" button

---

## Expected Result
- User stay on the login page
- It should highlight the username and password fields with red border
- Error message is displayed: "Epic sadface: Username and password do not match any user in this service"

---

## Actual Result
- Behaved as expected

---
