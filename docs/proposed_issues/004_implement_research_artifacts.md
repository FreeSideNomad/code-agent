# Issue Proposal: Implement Research Agent Schemas and Prompts

**Title:** [Feature]: Implement Research Agent Schemas and Prompts
**Labels:** feature, research-agent
**Assignee:** (Current Agent)

## Description
Based on the requirements defined in `docs/use-case-research.md`, we need to implement the core data structures (Pydantic models) and the prompt templates required for the Research Assistant Agent.

## Tasks
- [ ] Create `src/code_agent/schemas/research.py`:
    - Implement `ResearchProposal` model matching the YAML schema.
    - Implement `ResearchPlan` and `ResearchStep` models.
    - Ensure models support serialization/deserialization to YAML.
- [ ] Create Prompt Templates in `src/code_agent/prompts/research/`:
    - `clarify_requirements.md`: System prompt for the interactive refinement phase.
    - `create_plan.md`: Instruction to generate the 20-step research plan.
    - `execute_step.md`: Template for executing individual research steps.
    - `summarize.md`: Template for the final report generation.

## Definition of Done
- Pydantic models exist and are tested with sample YAML.
- Prompt files exist and contain the required instructions/context.
- A test ensures the Pydantic models can parse the example YAML from the docs.
