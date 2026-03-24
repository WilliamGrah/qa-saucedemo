# Test Case: TC-AUTH-008 - URL Access Without Authentication

## Test Information
- **Test Suite:** Authentication
- **Test Environment:** Production (Edge 143.0.3650.96, Windows 11 Pro)
- **Status:** Passed

---

## Preconditions
- No user is logged in
- Browser is open and on the login page

---

## Steps
1. Navigate to https://www.saucedemo.com/inventory.html
2. You should be redirected to the login page
3. It should show an error message in red.

---

## Expected Result
- User is redirected to login page
-  Error message is displayed in red text below the login form: "Epic sadface: You can only access '/inventory.html' when you are logged in."

---

## Actual Result
- Behaved as expected

---
