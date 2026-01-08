# Use Case: Research Assistant Agent

**Status:** Draft
**Last Updated:** 2026-01-08

## 1. Overview
The Research Assistant Agent is an autonomous system designed to execute deep, multi-step research tasks. It interacts with the user to define the research scope (`research-proposal.yaml`), generates a structured execution plan (`research-plan.yaml`), and executes the plan concurrently, producing a final summarized report.

## 2. Workflow

### Phase 1: Interactive Proposal Definition
1.  **User Initiation**: User starts the agent (CLI/Web).
2.  **Initial Prompt**: Agent asks: "What topic would you like to research today?"
3.  **Refinement Loop**: Agent analyzes the initial input and asks clarifying questions to populate the `research-proposal.yaml` schema.
    *   *System Prompt*: "You are an expert Research Director. Your goal is to scope a research project. Ask clarifying questions to ensure the proposal is specific, actionable, and has clear success metrics."
4.  **Finalization**: Agent presents the drafted `research-proposal.yaml` for user confirmation.
5.  **Commit**: Upon approval, `research-proposal.yaml` is saved and committed to the git repo.

### Phase 2: Plan Generation
1.  **Input**: `research-proposal.yaml`.
2.  **Process**: Agent uses the `create-research-plan.md` prompt to generate a detailed execution strategy.
3.  **Output**: `research-plan.yaml` containing a list of 10-20 granular steps.
4.  **Commit**: `research-plan.yaml` is committed.

### Phase 3: Execution
1.  **Orchestration**: The main agent reads `research-plan.yaml`.
2.  **Concurrency**: Independent steps are executed in parallel (up to a configurable limit).
3.  **Step Execution**:
    *   Each step uses the "Scope of Inquiry" from the plan as a prompt.
    *   Agent searches the web, reads docs, or analyzes data.
    *   **Output**: A Markdown file (e.g., `step_01_background.md`) is generated and committed.
4.  **Dependency Management**: Steps waiting on others (e.g., "Summarize findings") block until predecessors are complete.

### Phase 4: Summarization
1.  **Input**: All generated `step_*.md` files.
2.  **Process**: Agent synthesizes the information into a cohesive final report.
3.  **Output**: `research-output.md`.

## 3. Data Structures

### 3.1 Research Proposal Schema (`research-proposal.yaml`)

```yaml
topic: "The topic of research"
objective: "Primary goal of this research (e.g., 'Compare frameworks', 'Market analysis')"
scope:
  in_scope:
    - "List of specific areas to cover"
  out_of_scope:
    - "List of areas to explicitly ignore"
target_audience: "Who is this research for? (e.g., CTO, Developer, Investor)"
sources:
  authoritative_types:
    - "Academic papers (arXiv, IEEE)"
    - "Official documentation"
    - "Trusted industry reports (Gartner, Forrester)"
  excluded_types:
    - "Opinion blogs"
    - "Social media threads (unless specified)"
    - "Marketing landing pages"
success_measures:
  - "Key metrics or deliverables (e.g., 'Provide a comparison table', 'Cite at least 5 papers')"
output_format: "Markdown report with citations"
context: "Additional background information provided by the user"
```

### 3.2 Research Plan Schema (`research-plan.yaml`)

```yaml
plan_id: "unique-plan-id"
proposal_ref: "hash-of-proposal"
steps:
  - id: "step_01"
    title: "Gather Background Information"
    description: "Search for definitions and history of the topic."
    dependencies: [] # No dependencies, can run immediately
    scope_of_inquiry: >
      Search for 'Topic History' and 'Topic Definitions'. 
      Focus on authoritative sources defined in the proposal.
      Summarize the evolution of the technology.
    output_file: "research/step_01_background.md"
    tools_required: ["web_search", "read_page"]

  - id: "step_02"
    title: "Analyze Competitor A"
    description: "Deep dive into Competitor A features."
    dependencies: []
    scope_of_inquiry: "..."
    output_file: "research/step_02_competitor_a.md"

  - id: "step_N"
    title: "Final Summarization"
    description: "Synthesize all findings."
    dependencies: ["step_01", "step_02", ...] # Waits for all
    scope_of_inquiry: >
      Read all generated step files. 
      Create a final report addressing the original objective. 
      Ensure all success measures are met.
    output_file: "research-output.md"
```

## 4. Prompts Strategy

*   **`prompts/research/clarify_requirements.md`**: Used in Phase 1 to interview the user.
*   **`prompts/research/create_plan.md`**: Used in Phase 2 to convert the proposal into the YAML plan.
*   **`prompts/research/execute_step.md`**: Used in Phase 3 for individual workers.
*   **`prompts/research/summarize.md`**: Used in Phase 4 for the final report.

## 5. Technical Requirements
*   **Git Integration**: Each artifact generation triggers a git commit.
*   **Concurrency**: Use `asyncio` to manage parallel step execution.
*   **State Management**: Track step status (PENDING, RUNNING, COMPLETED, FAILED) in a local database or simple file state to allow resuming.