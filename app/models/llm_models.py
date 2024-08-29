from typing import Any, Optional

from pydantic import BaseModel, Field


class LlamaCppCompletionOptions(BaseModel):
    prompt: str | list[str | int] = Field(
        ..., description="Prompt as a string or array of strings/numbers."
    )
    temperature: float = Field(0.8, description="Randomness of generated text.")
    dynatemp_range: float = Field(0.0, description="Dynamic temperature range.")
    dynatemp_exponent: float = Field(1.0, description="Dynamic temperature exponent.")
    top_k: int = Field(
        40, description="Limit next token selection to K most probable tokens."
    )
    top_p: float = Field(
        0.95,
        description="Limit token selection to a subset with cumulative probability above P.",
    )
    min_p: float = Field(
        0.05, description="Minimum probability for a token to be considered."
    )
    n_predict: int = Field(-1, description="Max number of tokens to predict.")
    n_keep: int = Field(
        0,
        description="Number of tokens from prompt to retain when context size is exceeded.",
    )
    stream: bool = Field(False, description="Receive predicted tokens in real-time.")
    stop: list[str] = Field(default_factory=list, description="Stopping strings.")
    tfs_z: float = Field(1.0, description="Tail free sampling parameter z.")
    typical_p: float = Field(1.0, description="Locally typical sampling parameter p.")
    repeat_penalty: float = Field(
        1.1, description="Control repetition of token sequences."
    )
    repeat_last_n: int = Field(
        64, description="Last n tokens to consider for penalizing repetition."
    )
    penalize_nl: bool = Field(
        True, description="Penalize newline tokens when applying repeat penalty."
    )
    presence_penalty: float = Field(0.0, description="Repeat alpha presence penalty.")
    frequency_penalty: float = Field(0.0, description="Repeat alpha frequency penalty.")
    penalty_prompt: Optional[str | list[int]] = Field(
        None, description="Prompt used for penalty evaluation."
    )
    mirostat: int = Field(
        0, description="Enable Mirostat sampling, controlling perplexity."
    )
    mirostat_tau: float = Field(
        5.0, description="Mirostat target entropy, parameter tau."
    )
    mirostat_eta: float = Field(
        0.1, description="Mirostat learning rate, parameter eta."
    )
    grammar: Optional[str] = Field(
        None, description="Grammar for grammar-based sampling."
    )
    json_schema: Optional[Any] = Field(
        None, description="JSON schema for grammar-based sampling."
    )
    seed: int = Field(-1, description="Random number generator seed.")
    ignore_eos: bool = Field(
        False, description="Ignore end of stream token and continue generating."
    )
    logit_bias: list[list[int | float | str]] = Field(
        default_factory=list, description="Modify likelihood of token appearance."
    )
    n_probs: int = Field(
        0, description="Return probabilities of top N tokens for each generated token."
    )
    min_keep: int = Field(
        0, description="Force samplers to return N possible tokens at minimum."
    )
    image_data: Optional[list[dict]] = Field(
        None,
        description="Array of objects holding base64-encoded image data and its ids.",
    )
    id_slot: int = Field(-1, description="Assign completion task to a specific slot.")
    cache_prompt: bool = Field(
        False, description="Re-use KV cache from previous request if possible."
    )
    system_prompt: Optional[str] = Field(
        None, description="Change the system prompt (initial prompt of all slots)."
    )
    samplers: list[str] = Field(
        default_factory=lambda: [
            "top_k",
            "tfs_z",
            "typical_p",
            "top_p",
            "min_p",
            "temperature",
        ],
        description="Order of samplers to be applied.",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "prompt": "Once upon a time...",
                "temperature": 0.8,
                "top_k": 40,
                "n_predict": 100,
                "stream": True,
                "stop": ["\n"],
            }
        }
