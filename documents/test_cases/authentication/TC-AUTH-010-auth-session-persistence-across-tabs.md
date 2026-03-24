# Test Case: TC-AUTH-010 - Session Persistence Across Tabs

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
5. Verify successful login to inventory page
6. Open a new browser tab
7. Navigate to https://www.saucedemo.com/
8. Check if user is still logged in and on the inventory page

---

## Expected Result
- After opening a new tab, user should remain logged in
- Inventory page should still be displayed

---

## Actual Result
- Behaved as expected

---
