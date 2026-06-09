from pydantic import BaseModel, Field


class ModerationRequest(BaseModel):
    text: str = Field(..., max_length=2000)


class ModerationResponse(BaseModel):
    status: str                       # "safe" | "blocked"
    kindness_score: int               # 1..5
    message: str | None = None        # set when safe
    reason: str | None = None         # set when blocked
    suggestions: list[str] = []       # kinder rewrites when blocked
