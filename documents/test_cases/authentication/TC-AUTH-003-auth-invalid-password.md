# Test Case: TC-AUTH-003 - User Login with Invalid Password

## Test Information
- **Test Suite:** Authentication
- **Test Environment:** Production (Edge 143.0.3650.96, Windows 11 Pro)
- **Status:** Passed

---

## Preconditions
- User does exist in the system
- User has a valid username: standard_user,
- User has an invalid password: 12345
- Browser is open and on the login page

---

## Steps
1. Navigate to https://www.saucedemo.com/
2. Enter "standard_user" in the username field
3. Enter "12345" in the password field
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
