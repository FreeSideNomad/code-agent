from typing import List, Optional

import yaml
from pydantic import BaseModel, Field


class Scope(BaseModel):
    in_scope: List[str] = Field(default_factory=list, description="List of specific areas to cover")
    out_of_scope: List[str] = Field(default_factory=list, description="List of areas to explicitly ignore")


class Sources(BaseModel):
    authoritative_types: List[str] = Field(
        default_factory=list, description="Types of sources to prioritize (e.g., Academic papers, Official docs)"
    )
    excluded_types: List[str] = Field(
        default_factory=list, description="Types of sources to avoid (e.g., Opinion blogs)"
    )


class ResearchProposal(BaseModel):
    topic: str
    objective: str
    scope: Scope
    target_audience: str
    sources: Sources
    success_measures: List[str]
    output_format: str = "Markdown report with citations"
    context: Optional[str] = None

    def to_yaml(self) -> str:
        return yaml.dump(self.model_dump(), sort_keys=False)

    @classmethod
    def from_yaml(cls, yaml_str: str) -> "ResearchProposal":
        data = yaml.safe_load(yaml_str)
        return cls(**data)


class ResearchStep(BaseModel):
    id: str
    title: str
    description: str
    dependencies: List[str] = Field(default_factory=list)
    scope_of_inquiry: str
    output_file: str
    tools_required: List[str] = Field(default_factory=list)


class ResearchPlan(BaseModel):
    plan_id: str
    proposal_ref: str
    steps: List[ResearchStep]

    def to_yaml(self) -> str:
        return yaml.dump(self.model_dump(), sort_keys=False)

    @classmethod
    def from_yaml(cls, yaml_str: str) -> "ResearchPlan":
        data = yaml.safe_load(yaml_str)
        return cls(**data)
