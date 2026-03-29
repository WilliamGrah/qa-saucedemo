# Test Case: TC-INV-003 - Remove from Cart Button

## Test Information
- **Test Suite:** Inventory
- **Test Environment:** Production (Edge 143.0.3650.96, Windows 11 Pro)
- **Status:** Passed

---

## Preconditions
- User logged in with valid credentials (standard_user/secret_sauce)
- Browser is open and on the products page

---

## Steps
1. Navigate to https://www.saucedemo.com/inventory.html
2. Click the "Add to cart" button for any product (e.g., Sauce Labs Backpack)
3. It should add the product to the cart and update the cart icon with the number of items
4. Click the "Remove" button for the same product
5. It should update the cart icon with the number of items
6. Click the cart icon to navigate to the cart page
7. Verify the product is no longer listed in the cart

---

## Expected Result
- User is on the products page
- When "Add to cart" is clicked, the product is added to the cart
- Cart icon updates with the number of items added
- When "Remove" is clicked, the product is removed from the cart
- Cart icon updates with the number of items remaining
- When the cart icon is clicked, user is navigated to the cart page
- The product removed from the cart is no longer listed on the cart page

---

## Actual Result
- Behaved as expected

---
