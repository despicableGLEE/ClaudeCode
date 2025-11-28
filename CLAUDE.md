# CLAUDE.md - AI Assistant Guide

> **Last Updated:** 2025-11-23
> **Repository:** despicableGLEE/ClaudeCode
> **Status:** New Repository - Initial Setup Phase

---

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Development Workflows](#development-workflows)
- [Git Conventions](#git-conventions)
- [Code Conventions](#code-conventions)
- [Testing Guidelines](#testing-guidelines)
- [AI Assistant Best Practices](#ai-assistant-best-practices)
- [Common Tasks](#common-tasks)

---

## Overview

### Current State
This is a newly initialized repository with minimal structure. The project is in the initial setup phase.

### Repository Information
- **Owner:** despicableGLEE
- **License:** MIT License (see LICENSE file)
- **Primary Branch:** TBD (currently on feature branch)

### Project Purpose
*To be documented as the project develops*

---

## Repository Structure

### Current Structure
```
ClaudeCode/
├── .git/              # Git repository metadata
├── LICENSE            # MIT License
└── CLAUDE.md          # This file
```

### Planned Structure
*This section should be updated as the project structure evolves. Common patterns include:*

```
ClaudeCode/
├── src/               # Source code
├── tests/             # Test files
├── docs/              # Documentation
├── config/            # Configuration files
├── scripts/           # Build and utility scripts
├── .github/           # GitHub workflows and templates
├── LICENSE            # MIT License
├── README.md          # Project documentation
├── CLAUDE.md          # AI assistant guide
└── package.json       # Node.js dependencies (if applicable)
```

---

## Development Workflows

### Setting Up Development Environment

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd ClaudeCode
   ```

2. **Install Dependencies**
   *To be documented when dependencies are added*

3. **Verify Setup**
   *To be documented when build/test processes are established*

### Making Changes

1. **Create/Switch to Feature Branch**
   - Use the designated branch naming convention (see Git Conventions)
   - Branch name format: `claude/claude-md-<identifier>-<session-id>`

2. **Make Your Changes**
   - Follow code conventions (see Code Conventions section)
   - Write tests for new functionality
   - Update documentation as needed

3. **Test Your Changes**
   - Run all tests before committing
   - Verify no regressions

4. **Commit and Push**
   - Write clear, descriptive commit messages
   - Push to the designated feature branch
   - Use `git push -u origin <branch-name>` for first push

---

## Git Conventions

### Branch Naming

**AI Assistant Branches:**
- Format: `claude/claude-md-<identifier>-<session-id>`
- Example: `claude/claude-md-miazhw0rnwo1llay-01JYv2vFQLsTyz8C7tvUuUVf`
- **CRITICAL:** Branch must start with `claude/` and end with matching session ID
- Failure to follow this convention will result in 403 errors on push

**Human Developer Branches:**
- Feature branches: `feature/<feature-name>`
- Bug fixes: `fix/<bug-name>`
- Hotfixes: `hotfix/<issue-name>`

### Commit Messages

Follow conventional commit format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(auth): add user authentication system

Implement JWT-based authentication with refresh tokens.
Includes login, logout, and token validation endpoints.

Closes #123
```

### Push/Pull Best Practices

**Push Operations:**
- Always use: `git push -u origin <branch-name>`
- Retry on network errors: up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
- Never force push to main/master without explicit permission

**Fetch/Pull Operations:**
- Prefer specific branches: `git fetch origin <branch-name>`
- Retry on network failures: up to 4 times with exponential backoff
- Use: `git pull origin <branch-name>`

---

## Code Conventions

### General Principles

1. **Keep It Simple**
   - Avoid over-engineering
   - Only make changes that are directly requested or clearly necessary
   - Don't add features beyond what was asked

2. **No Premature Optimization**
   - Don't create abstractions for one-time operations
   - Don't design for hypothetical future requirements
   - Three similar lines are better than a premature abstraction

3. **Security First**
   - Avoid command injection, XSS, SQL injection
   - Follow OWASP Top 10 security practices
   - Validate input at system boundaries

4. **Clean Code**
   - Self-documenting code is preferred over comments
   - Only comment where logic isn't self-evident
   - Remove unused code completely (no commented-out code)

### Language-Specific Conventions

*To be documented based on the primary programming language(s) used*

#### JavaScript/TypeScript
- TBD

#### Python
- TBD

#### Other Languages
- TBD

---

## Testing Guidelines

### Test Structure
*To be documented when testing framework is established*

### Running Tests
*To be documented*

### Writing Tests
*To be documented*

### Coverage Requirements
*To be documented*

---

## AI Assistant Best Practices

### Before Starting Work

1. **Read First, Code Later**
   - NEVER propose changes to code you haven't read
   - Always read relevant files before making modifications
   - Understand existing code before suggesting changes

2. **Plan Complex Tasks**
   - Use TodoWrite tool for multi-step tasks
   - Break down complex work into manageable steps
   - Track progress and update todos in real-time

3. **Check for Existing Documentation**
   - Read README.md, CONTRIBUTING.md, and this file
   - Check for project-specific conventions
   - Look for existing patterns in the codebase

### During Development

1. **Use Appropriate Tools**
   - Use specialized tools (Read, Edit, Write) instead of bash commands for file operations
   - Prefer Task tool with Explore agent for codebase exploration
   - Run independent operations in parallel when possible

2. **Follow Project Patterns**
   - Match existing code style and conventions
   - Use the same libraries and patterns already in the project
   - Don't introduce new dependencies without good reason

3. **Commit Practices**
   - Only commit when explicitly requested or when the task is complete
   - Write descriptive commit messages following the convention
   - Run tests before committing
   - Don't skip git hooks unless explicitly requested

4. **Error Handling**
   - Only add error handling at system boundaries
   - Trust internal code and framework guarantees
   - Don't add validation for scenarios that can't happen

### After Completing Work

1. **Verify Changes**
   - Run all relevant tests
   - Check that no regressions were introduced
   - Verify the original request was fully addressed

2. **Clean Up**
   - Mark todos as completed
   - Remove any debug code or console logs
   - Delete unused code (don't comment it out)

3. **Document Changes**
   - Update relevant documentation
   - Add comments only where necessary
   - Update this CLAUDE.md if project structure changed significantly

---

## Common Tasks

### Adding a New Feature

1. Read relevant existing code
2. Plan the implementation using TodoWrite
3. Implement the feature following code conventions
4. Write tests for the new functionality
5. Update documentation
6. Commit with descriptive message
7. Push to feature branch

### Fixing a Bug

1. Reproduce the bug if possible
2. Locate the problematic code
3. Understand the root cause
4. Implement the fix (no extra refactoring)
5. Add/update tests to prevent regression
6. Commit and push

### Refactoring Code

1. Only refactor when explicitly requested
2. Ensure comprehensive test coverage exists
3. Make incremental changes
4. Run tests after each change
5. Commit frequently with clear messages

### Updating Dependencies

*To be documented when dependency management is established*

---

## Project-Specific Notes

### Dependencies
*None currently - to be documented as they are added*

### External APIs
*To be documented if the project integrates with external services*

### Environment Variables
*To be documented if environment configuration is needed*

### Deployment
*To be documented when deployment process is established*

---

## Questions or Issues?

For questions about this guide or the project:
- Check the README.md (when available)
- Review existing issues and pull requests
- Ask the repository owner or maintainers

---

## Maintenance

This document should be updated whenever:
- Project structure changes significantly
- New conventions are established
- New development workflows are introduced
- New dependencies or tools are added
- Common patterns or anti-patterns are identified

**Note to AI Assistants:** When you make significant structural or workflow changes, please update this document accordingly. Keep it current and accurate to help future development sessions.
