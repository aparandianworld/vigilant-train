#!/usr/bin/env python3

import dspy
import os
from dotenv import load_dotenv

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")
load_dotenv()

model_name = "openai/gpt-4o-mini"

lm = dspy.LM(model_name)
dspy.configure(lm=lm)

class SimpleQAModule(dspy.Module):
    def forward(self, question: str) -> str:
        return lm(question)

def simple_qa(question: str) -> str:
    qa_model = SimpleQAModule()
    return qa_model.forward(question)