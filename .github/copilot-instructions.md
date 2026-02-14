# Copilot Instructions for CampaignCanon Workspace

## Project Overview
This workspace manages canonical campaign text files and scenario logic for AI-driven simulation and reporting. Major components:
- `canon/`: Canonical text files (one per item/scene/entry)
- `ManhattanRepublic/3.0/campaign.json`: Hard-spec scenario contract, rules, and report formats
- `tools/transfer.py`: Bundles canon/ into a ZIP for transfer

## Key Workflows
- **Bundle Canon Files:**
	- Run: `python tools/transfer.py canon mycanon.zip`
	- No external dependencies required for transfer.py (see requirements.txt)
- **Build/Run Engine:**
	- Build: `npm run build` (TypeScript)
	- Start: `npm start` (runs dist/initialize_novaroma_engine.js)
	- Task: `npm run init` (see .vscode/tasks.json)

## Scenario/Report Conventions (campaign.json)
- **Do NOT invent or infer rules/logic not explicitly specified in scenario files.**
- **Milestone IDs:** Format `<year>-<serial>`, e.g., `1-1`. No 'Y' prefix.
- **Initiative IDs:** Always use combined INIT+ID, e.g., `AGEX-1-2`. Never split code/ID into separate fields.
- **Date Format:** `MMM D, YYYY` (e.g., Mar 1, 509 BCE)
- **UGRID Map:** All cell IDs must be unique 4-char codes. Only generate per scenario JSON rules.
- **Report Contracts:**
	- All report outputs must match referenced contract columns/sections exactly.
	- Proof line required: `PROOF: contract={contract_path} ...`
	- Regenerate output if any contract check fails.
- **No Unapproved Content:** Only generate content types listed in scenario JSON. Narrative responses are allowed; see `no_unapproved_content_exceptions` in campaign.json.
- **Templates:** Never edit template files in place. Copy to runtime folder before use.

## Data Flow & Integration
- **Scenario Load:** Engine must load scenario ZIP at startup and keep it open for the session.
- **Authoritative Data:**
	- `state.json` (starting state)
	- `event_log.jsonl` (event log)
	- `canon/` (domain knowledge)
- **Map/Report Rendering:** Use only scenario/canon rules for rendering, formatting, and gating (e.g., trade, tech, materials).

## Project-Specific Patterns
- **Strict Validation:**
	- All report generation must validate against contract formats before output.
	- Failures are fatal; output only error if validation fails.
- **Audit/Replay:**
	- Audit logs and replay are supported (see campaign.json: audit, replay)
- **Naming:**
	- Bundles: `NRCore_v<major>_<minor>_<patch>.zip`
	- Canon versioning: see `canon_version_expected` in campaign.json

## References
- See `README.md` for quickstart and structure
- See `ManhattanRepublic/3.0/campaign.json` for scenario rules, contracts, and invariants
- See `CHANGELOG.md` for scenario changes

## AI Agent Guidance
- Always check scenario JSON for explicit rules before generating logic or content
- Never invent new report types, fields, or logic unless listed in scenario files
- Use only the formats, IDs, and conventions specified in scenario JSON and canon/
- Regenerate outputs if contract validation fails
- When in doubt, prefer strictness and explicitness over flexibility
- [ ] Verify that the copilot-instructions.md file in the .github directory is created.

- [ ] Clarify Project Requirements
	<!-- Ask for project type, language, and frameworks if not specified. Skip if already provided. -->

- [ ] Scaffold the Project
	<!--
	Ensure that the previous step has been marked as completed.
	Call project setup tool with projectType parameter.
	Run scaffolding command to create project files and folders.
	Use '.' as the working directory.
	If no appropriate projectType is available, search documentation using available tools.
	Otherwise, create the project structure manually using available file creation tools.
	-->

- [ ] Customize the Project
	<!--
	Verify that all previous steps have been completed successfully and you have marked the step as completed.
	Develop a plan to modify codebase according to user requirements.
	Apply modifications using appropriate tools and user-provided references.
	Skip this step for "Hello World" projects.
	-->

- [ ] Install Required Extensions
	<!-- ONLY install extensions provided mentioned in the get_project_setup_info. Skip this step otherwise and mark as completed. -->

- [ ] Compile the Project
	<!--
	Verify that all previous steps have been completed.
	Install any missing dependencies.
	Run diagnostics and resolve any issues.
	Check for markdown files in project folder for relevant instructions on how to do this.
	-->

- [ ] Create and Run Task
	<!--
	Verify that all previous steps have been completed.
	Check https://code.visualstudio.com/docs/debugtest/tasks to determine if the project needs a task. If so, use the create_and_run_task to create and launch a task based on package.json, README.md, and project structure.
	Skip this step otherwise.
	 -->

- [ ] Launch the Project
	<!--
	Verify that all previous steps have been completed.
	Prompt user for debug mode, launch only if confirmed.
	 -->

- [ ] Ensure Documentation is Complete
	<!--
	Verify that all previous steps have been completed.
	Verify that README.md and the copilot-instructions.md file in the .github directory exists and contains current project information.
	Clean up the copilot-instructions.md file in the .github directory by removing all HTML comments.
	 -->

<!--
## Execution Guidelines
PROGRESS TRACKING:
- If any tools are available to manage the above todo list, use it to track progress through this checklist.
- After completing each step, mark it complete and add a summary.
- Read current todo list status before starting each new step.

COMMUNICATION RULES:
- Avoid verbose explanations or printing full command outputs.
- If a step is skipped, state that briefly (e.g. "No extensions needed").
- Do not explain project structure unless asked.
- Keep explanations concise and focused.

DEVELOPMENT RULES:
- Use '.' as the working directory unless user specifies otherwise.
- Avoid adding media or external links unless explicitly requested.
- Use placeholders only with a note that they should be replaced.
- Use VS Code API tool only for VS Code extension projects.
- Once the project is created, it is already opened in Visual Studio Code—do not suggest commands to open this project in Visual Studio again.
- If the project setup information has additional rules, follow them strictly.

FOLDER CREATION RULES:
- Always use the current directory as the project root.
- If you are running any terminal commands, use the '.' argument to ensure that the current working directory is used ALWAYS.
- Do not create a new folder unless the user explicitly requests it besides a .vscode folder for a tasks.json file.
- If any of the scaffolding commands mention that the folder name is not correct, let the user know to create a new folder with the correct name and then reopen it again in vscode.

EXTENSION INSTALLATION RULES:
- Only install extension specified by the get_project_setup_info tool. DO NOT INSTALL any other extensions.

PROJECT CONTENT RULES:
- If the user has not specified project details, assume they want a "Hello World" project as a starting point.
- Avoid adding links of any type (URLs, files, folders, etc.) or integrations that are not explicitly required.
- Avoid generating images, videos, or any other media files unless explicitly requested.
- If you need to use any media assets as placeholders, let the user know that these are placeholders and should be replaced with the actual assets later.
- Ensure all generated components serve a clear purpose within the user's requested workflow.
- If a feature is assumed but not confirmed, prompt the user for clarification before including it.
- If you are working on a VS Code extension, use the VS Code API tool with a query to find relevant VS Code API references and samples related to that query.

TASK COMPLETION RULES:
- Your task is complete when:
  - Project is successfully scaffolded and compiled without errors
  - copilot-instructions.md file in the .github directory exists in the project
  - README.md file exists and is up to date
  - User is provided with clear instructions to debug/launch the project

Before starting a new task in the above plan, update progress in the plan.
-->
- Work through each checklist item systematically.
- Keep communication concise and focused.
- Follow development best practices.
