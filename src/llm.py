from langchain_groq import ChatGroq
from langchain_cerebras import ChatCerebras


# =========================================================
# Primary LLM
# =========================================================

primary_llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


# =========================================================
# Fallback LLM
# =========================================================

fallback_llm = ChatCerebras(
    model="llama-4-scout-17b-16e-instruct",
    temperature=0
)


# =========================================================
# LLM with fallback
# =========================================================

llm = primary_llm.with_fallbacks(
    [fallback_llm]
)