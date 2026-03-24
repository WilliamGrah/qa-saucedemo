# Test Case: TC-AUTH-001 - User Login with Valid Credentials

## Test Information
- **Test Suite:** Authentication
- **Test Environment:** Production (Edge 143.0.3650.96, Windows 11 Pro)
- **Status:** Passed

---

## Preconditions
- User account exists in the system
- User has an valid username: standard_user,
- User has a valid password: secret_sauce
- Browser is open and on the login page

---

## Steps
1. Navigate to https://www.saucedemo.com/
2. Enter "standard_user" in the username field
3. Enter "secret_sauce" in the password field
4. Click the "Login" button

---

## Expected Result
- User is redirected to the products page
- Products inventory is displayed
- URL changes to /inventory.html

---

## Actual Result
- Behaved as expected

---
