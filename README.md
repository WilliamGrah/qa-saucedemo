# Test Plan - SauceDemo E-commerce

## Objective

Validate the core functionalities of the SauceDemo e-commerce application to ensure:
- Users can successfully authenticate and manage sessions

---

## Document Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-03-25 | William Grah | Initial version - Authentication module scope defined |
| 1.1 | 2025-03-26 | William Grah | Added cross-browser testing (Chrome, Firefox, Safari) for automated tests |
| 1.2 | 2026-03-27 | William Grah | Added CI pipeline with GitHub Actions |


---

## Version

- **Version:** 1.0
- **Date:** March 24, 2025
- **Application Under Test:** SauceDemo (https://www.saucedemo.com/)
- **Test Environment:** Production

---

## Scope

### In Scope
- **Authentication Module:** Login, logout, locked users, invalid credentials, session management


### Out of Scope
- Performance testing (load/stress testing)
- Security penetration testing
- Backend API testing
- Payment gateway integration (mock only)
- Accessibility testing (WCAG compliance)
- Localization/internationalization

---

## Team

| Role | Name | Responsibilities |
|------|------|------------------|
| QA Automation Engineer | William Grah | Test Cases, Manual Testing, Test automation with Playwright/Python |

---

## Risks

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| Application downtime during testing | High | Low | Test during off-peak hours |
| Test data inconsistency | Medium | Medium | Use standardized test accounts (standard_user, locked_out_user) |
| Browser compatibility issues | Medium | Medium | Prioritize Edge, test other browsers secondary |

---

## Test Strategy

### Testing Approach
- Manual and automated testing of login flows
- Positive scenarios (valid users) and negative scenarios (invalid/locked users)
- Playwright + Python + Page Object Model for automation

### Continuous Integration
- **Platform:** GitHub Actions
- **Trigger:** On push to main branch and pull requests
- **Browsers:** Chrome, Firefox, Safari (Webkit)
- **Reports:** Test results automatically generated and stored as artifacts

### Test Execution
- **Manual Tests:** Executed on-demand using Microsoft Edge
- **Automated Tests:** Run automatically via CI pipeline on every code change
- **Cross-browser:** CI executes tests on Chrome, Firefox, and Safari

### Test Types
1. **Smoke Testing:** Verify basic login functionality works
2. **Functional Testing:** Validate all login scenarios (positive and negative)

### Test Environment

#### Manual Testing
- **Browser:** Microsoft Edge 143.0.3650.96
- **OS:** Windows 11 Pro
- **Resolution:** 1920x1080

#### Automated Testing
- **Browsers:**
  - Google Chrome (latest)
  - Mozilla Firefox (latest)
  - Safari/Webkit (latest)
- **OS:** Windows 11 Pro
- **Automation Framework:** Playwright + Python + Pytest

### Entry Criteria
- Test environment is accessible
- Test user accounts are available (standard_user, locked_out_user, etc.)
- Test cases are documented

### Exit Criteria
- All test cases executed
- No critical bugs open
- Test report completed

---

## Activities and Estimates

| Activity | Description | Duration | Deliverables |
|----------|-------------|----------|--------------|
| **Test Planning** | Create test plan document | 1 day | Test Plan (this document) |
| **Test Design** | Write test cases for authentication module | 1 days | 11 test cases in Markdown |
| **Manual Testing** | Execute test cases manually | 1 day | Test execution results |
| **Test Automation** | Develop automated tests with Playwright | 2 day | Automated test suite (Python) |
| **Test Reporting** | Document results and bugs found | 1 day | Test summary report |

**Total Estimated Effort:** 6 days

---

### Test Case Summary

| Test Scenario | Priority | Manual | Automated |
|---------------|----------|--------|-----------|
| Login with valid credentials | High | ✓ | ✓ |
| Login with invalid username | High | ✓ | ✓ |
| Login with invalid password | High | ✓ | ✓ |
| Login with empty fields | Medium | ✓ | ✓ |
| Login with locked account | High | ✓ | ✓ |
| Direct URL access without authentication | High | ✓ | ✓ |
| Logout functionality | Medium | ✓ | ✓ |
| Session persists after page refresh | Low | ✓ | ✓ |
| Session shared across browser tabs | Low | ✓ | ✓ |
| Session expires after browser close | Low | ✓ | ✓ |

- **Total Test Cases:** 11
- **Total Test Executions:** 11 manual (Edge) + 33 automated (11 cases × 3 browsers)

---

## Tools and Technologies

- **Test Planning:** Markdown files (Test Plan document)
- **Test Cases:** Markdown files (individual test case documents)
- **Bug Tracking:** Markdown files (bug reports in /bugs folder)
- **Test Reporting:** Markdown files (test execution reports)
- **Automation Framework:** Playwright + Python + Pytest
- **Design Pattern:** Page Object Model (POM)
- **Test Environment:** Microsoft Edge 143.0.3650.96, Windows 11 Pro
- **CI/CD:** GitHub Actions (continuous integration with automated testing)
- **Version Control:** Git/GitHub

---

**Last Updated:** March 2026