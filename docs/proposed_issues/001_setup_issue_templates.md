# Issue Proposal: Setup GitHub Issue Templates

**Title:** [Chore]: Configure GitHub Issue Templates
**Labels:** chore, triage
**Assignee:** (Current Agent)

## Description
We need to standardize how issues are created in this repository to support our Agile workflow. This task involves setting up YAML-based issue forms for User Stories, Feature Requests, Bug Reports, and Chores.

## Tasks
- [ ] Create `.github/ISSUE_TEMPLATE/config.yml` to prevent blank issues.
- [ ] Create `.github/ISSUE_TEMPLATE/01_user_story.yml` with Agile fields (Role, Benefit, Acceptance Criteria).
- [ ] Create `.github/ISSUE_TEMPLATE/02_feature_request.yml`.
- [ ] Create `.github/ISSUE_TEMPLATE/03_bug_report.yml` with structured reproduction steps.
- [ ] Create `.github/ISSUE_TEMPLATE/04_chore.yml`.
- [ ] Verify templates appear correctly in the GitHub UI.

## Definition of Done
- All YAML files are present in the default branch.
- Clicking "New Issue" on GitHub presents the 4 distinct options.
