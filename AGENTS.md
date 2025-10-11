# Project Instruction

## Testing and Coverage

When adding or removing code it is essential that every functional edit to the codebase have corresponding tests. These tests, when possible should use the testing frameworks of the platform, for example in python it should be pytest.  

## Validation Script

There should be a run_checks.sh that runs all automated tests, static checks, style linting, test coverage or automation that run in the github actions.  If the repository contains multiple languages or platforms ALL of their checks must be run from this validation script.


# Task Instruction
All work and changes to the repository should be part of a task.  A task has a distinct starting point and measurable end goal.  If you feel like you are not presently in a task, ask for more detailed instructions or clarity on any underdeveloped parts of the problem.  Once the problem is well understood and appropriately broken down it will be tracked in a Github Issue.

When Starting a distinct task that has a clear starting point and end goal, create an Issue in the github issue tracker via the github MCP (configured via Cursor MCPs) and start a branch named after a 5 digit issue's ID left padded with 0s and suffixed with a snake case identifier transformation of the issue title.  You should check into this branch often and check github action statuses on your checkins fixing any problems that arise with them.  When the task is complete, create a PR against main for me to review and merge.


Issue tracking should take the place of status markdowns in the repository.

