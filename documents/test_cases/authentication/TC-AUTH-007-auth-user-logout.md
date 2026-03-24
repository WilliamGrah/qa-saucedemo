# Test Case: TC-AUTH-007 - User Log Out

## Test Information
- **Test Suite:** Authentication
- **Test Environment:** Production (Edge 143.0.3650.96, Windows 11 Pro)
- **Status:** Passed

---

## Preconditions
- User does exist in the system
- User has a valid username: standard_user,
- User has a valid password: secret_sauce
- Browser is open and on the login page

---

## Steps
1. Navigate to https://www.saucedemo.com/
2. Enter "standard_user" in the username field
3. Enter "secret_sauce" in the password field
4. Click the "Login" button
5. Verify successful login to inventory page
6. Click on the hamburger menu (☰) to open navigation
7. Click the logout button
8. Verify redirection to login page

---

## Expected Result
- Logout option found in hamburger menu
- User can click logout to terminate session
- User is redirected to login page after logout

---

## Actual Result
- Behaved as expected

---
