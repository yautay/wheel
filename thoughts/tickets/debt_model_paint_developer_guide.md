---
type: debt
priority: medium
created: 2026-04-23T16:53:59Z
status: created
tags: [documentation, developer, setup, operations, testing]
keywords: [developer guide, local setup, migrations, seed data, test commands, build commands, troubleshooting]
patterns: [developer onboarding guide, command reference, local environment setup, migration workflow documentation, troubleshooting checklist]
---

# DEBT-005: Write the developer setup and operations guide

## Description
Create a dedicated developer guide covering local setup, environment configuration, migrations, seed data, build commands, tests, and routine development operations.

## Context
The user asked for developer documentation as its own stream. While the scaffold ticket includes the minimum README needed to start the project, this ticket provides the fuller day-to-day guide for contributors.

## Requirements
Write a developer-focused operational guide for the MVP.

### Functional Requirements
- Document backend and frontend installation steps.
- Document environment variable setup and local configuration.
- Document how to run the backend and frontend locally.
- Document migration and seed workflows.
- Document test, lint, and build commands.
- Document common troubleshooting steps for the MVP stack.
- Document the recommended implementation order or contribution flow if useful.

### Non-Functional Requirements
- Keep the guide actionable and command-focused.
- Avoid duplicating business or end-user documentation.
- Align command examples with the actual scaffolded project structure.
- Keep the guide maintainable as the MVP evolves.

## Current State
Only the minimal setup information from the scaffolding work is expected to exist.

## Desired State
The repository contains a practical developer guide that supports onboarding and routine contribution workflows.

## Research Context
This ticket should reduce future friction in local development and verification.

### Keywords to Search
- `developer setup` - onboarding instructions
- `migration commands` - persistence workflow reference
- `seed data` - bootstrap dataset usage
- `test commands` - verification steps
- `troubleshooting` - common failure handling

### Patterns to Investigate
- `developer handbook` - command-oriented internal guide
- `setup + operations split` - startup versus daily workflow documentation
- `known issues section` - capture practical troubleshooting points

### Key Decisions Made
- Developer documentation should be separate from the minimal scaffold README.
- The guide should emphasize real commands and operational workflows.
- The scope includes setup, testing, migrations, seed data, and troubleshooting.

## Success Criteria
This ticket is complete when a new contributor can get productive using the guide instead of tribal knowledge.

### Automated Verification
- [ ] A developer-guide markdown document is added in the agreed documentation location.
- [ ] Commands and paths referenced in the guide match the implemented project structure.

### Manual Verification
- [ ] A developer can follow the guide to install, run, migrate, seed, and test the project locally.
- [ ] The guide covers the most common MVP development tasks without requiring source-code archaeology.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/debt_model_paint_technical_architecture_docs.md`
- Planned next ticket: `thoughts/tickets/debt_model_paint_user_guide.md`

## Notes
- Keep the guide implementation-specific and practical.
- Do not repeat product rationale that belongs in the business document.
