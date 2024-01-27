import json
from pathlib import Path
import requests
from huggingface_hub import hf_hub_url
import pytest


def load_model_data(model_path):
    with open(model_path, "r") as models_file:
        return json.load(models_file)


def flatten_model_data(families):
    for family in families:
        for model in family["models"]:
            for file in model["files"]:
                yield model["repo"], file["filename"]


def check_model_availability(repo, filename):
    url = hf_hub_url(repo, filename, repo_type="model", revision="main")
    response = requests.head(url)
    return response.ok


test_dir = Path(__file__).parent
model_paths = [
    "serge-models/all/models.json",
    "serge-models/coder/models.json",
    "serge-models/finance/models.json",
    "serge-models/french/models.json",
    "serge-models/generic/models.json",
    "serge-models/german/models.json",
    "serge-models/italian/models.json",
    "serge-models/large/models.json",
    "serge-models/math/models.json",
    "serge-models/medical/models.json",
    "serge-models/medium/models.json",
    "serge-models/small/models.json",
    "serge-models/spanish/models.json",
    "serge-models/tiny/models.json"
]

@pytest.mark.parametrize("model_path", model_paths)
def test_model_available(model_path):
    model_data = load_model_data(test_dir.parent / model_path)
    checks = list(flatten_model_data(model_data))

    for repo, filename in checks:
        assert check_model_availability(repo, filename), f"Model {repo}/{filename} not available"
