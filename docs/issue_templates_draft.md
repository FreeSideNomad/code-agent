# Proposed GitHub Issue Templates

This document drafts the YAML-based issue templates to be placed in `.github/ISSUE_TEMPLATE/`.

## 1. User Story (`01_user_story.yml`)

```yaml
name: User Story
description: Agile user story for new functionality
title: "[User Story]: "
labels: ["user-story", "triage"]
body:
  - type: textarea
    id: story
    attributes:
      label: User Story
      description: "Format: As a [role], I want [feature], so that [benefit]."
      placeholder: "As a developer, I want to use the CLI to initialize a project, so that I don't have to write boilerplate code."
    validations:
      required: true
  - type: textarea
    id: acceptance-criteria
    attributes:
      label: Acceptance Criteria
      description: List specific conditions that must be met.
      placeholder: |
        - [ ] The CLI accepts the `init` command.
        - [ ] A `pyproject.toml` is created.
        - [ ] The user receives a success message.
    validations:
      required: true
  - type: textarea
    id: tasks
    attributes:
      label: Technical Tasks (Optional)
      description: Breakdown of engineering tasks if known.
      placeholder: |
        - Create `init` command in Typer.
        - Add template generation logic.
  - type: dropdown
    id: priority
    attributes:
      label: Priority
      options:
        - High
        - Medium
        - Low
    validations:
      required: true
```

## 2. Feature Request (`02_feature_request.yml`)

```yaml
name: Feature Request
description: Suggest an idea or enhancement
title: "[Feature]: "
labels: ["enhancement", "triage"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Is your feature request related to a problem?
      description: A clear and concise description of what the problem is.
      placeholder: "I'm always frustrated when..."
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: Describe the solution you'd like
      description: A clear and concise description of what you want to happen.
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Describe alternatives you've considered
      description: A clear and concise description of any alternative solutions or features you've considered.
  - type: textarea
    id: context
    attributes:
      label: Additional Context
      description: Add any other context or screenshots about the feature request here.
```

## 3. Bug Report (`03_bug_report.yml`)

```yaml
name: Bug Report
description: Create a report to help us improve
title: "[Bug]: "
labels: ["bug", "triage"]
body:
  - type: textarea
    id: description
    attributes:
      label: Description
      description: A clear and concise description of the bug.
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to Reproduce
      description: Steps to reproduce the behavior.
      placeholder: |
        1. Run command '...'
        2. Select option '...'
        3. See error '...'
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected Behavior
      description: A clear and concise description of what you expected to happen.
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Version
      description: What version of the project are you running?
      placeholder: "v0.1.0"
  - type: textarea
    id: logs
    attributes:
      label: Logs / Screenshots
      description: Paste any relevant logs or attach screenshots.
      render: shell
```

## 4. Chore (`04_chore.yml`)

```yaml
name: Chore
description: Maintenance, refactoring, or documentation
title: "[Chore]: "
labels: ["chore", "triage"]
body:
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Describe the maintenance task.
    validations:
      required: true
  - type: textarea
    id: benefits
    attributes:
      label: Benefits
      description: Why is this chore necessary? (e.g., reduces tech debt, improves security)
```

## Configuration (`config.yml`)

```yaml
blank_issues_enabled: false
contact_links:
  - name: Ask a question
    url: https://github.com/FreeSideNomad/code-agent/discussions/new?category=q-a
    about: Ask the community for help
```
