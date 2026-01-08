from code_agent.schemas.research import ResearchPlan, ResearchProposal


def test_research_proposal_schema():
    yaml_data = """
    topic: "AI Agents"
    objective: "Compare frameworks"
    scope:
      in_scope: ["LangChain", "AutoGPT"]
      out_of_scope: ["Robotics"]
    target_audience: "CTO"
    sources:
      authoritative_types: ["Docs"]
      excluded_types: ["Twitter"]
    success_measures: ["Table of comparison"]
    output_format: "Markdown"
    context: "Client wants to build a chatbot."
    """

    proposal = ResearchProposal.from_yaml(yaml_data)

    assert proposal.topic == "AI Agents"
    assert "LangChain" in proposal.scope.in_scope
    assert proposal.context == "Client wants to build a chatbot."

    # Test round-trip
    dumped = proposal.to_yaml()
    loaded = ResearchProposal.from_yaml(dumped)
    assert loaded.objective == proposal.objective


def test_research_plan_schema():
    yaml_data = """
    plan_id: "plan-123"
    proposal_ref: "proposal-abc"
    steps:
      - id: "step_1"
        title: "Background"
        description: "Get history"
        dependencies: []
        scope_of_inquiry: "Search history"
        output_file: "step_1.md"
        tools_required: ["search"]
      - id: "step_2"
        title: "Summary"
        description: "Summarize"
        dependencies: ["step_1"]
        scope_of_inquiry: "Synthesize"
        output_file: "final.md"
    """

    plan = ResearchPlan.from_yaml(yaml_data)

    assert plan.plan_id == "plan-123"
    assert len(plan.steps) == 2
    assert plan.steps[1].dependencies == ["step_1"]

    # Test round-trip
    dumped = plan.to_yaml()
    loaded = ResearchPlan.from_yaml(dumped)
    assert loaded.steps[0].title == "Background"
