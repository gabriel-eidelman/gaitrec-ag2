import os
from autogen import LLMConfig

llm_config = LLMConfig(
    config_list=[
        {
            "api_type": "azure",
            "api_key": os.environ["AZURE_OAI_API_KEY"],
            "api_version": "2024-12-01-preview",
            "base_url": "https://gabriel-azure-oai.openai.azure.com/",
            "model": "gpt-4o-mini",  # Must match the model your deployment refers to
        }
    ],
    temperature=0.7
)