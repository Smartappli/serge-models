[![LLM Healthcheck](https://github.com/Smartappli/serge-models/actions/workflows/model-check.yml/badge.svg)](https://github.com/Smartappli/serge-models/actions/workflows/model-check.yml)

# Models for 🦙 Serge 🦙

[Serge](https://github.com/serge-chat/serge) is a chat interface crafted with [llama.cpp](https://github.com/ggerganov/llama.cpp) for running GGUF models. No API keys, entirely self-hosted!

- 🌐 **SvelteKit** frontend
- 💾 **[Redis](https://github.com/redis/redis)** for storing chat history & parameters
- ⚙️ **FastAPI + LangChain** for the API, wrapping calls to [llama.cpp](https://github.com/ggerganov/llama.cpp) using the [python bindings](https://github.com/abetlen/llama-cpp-python)

## ⚡️ How to replace serge's models.json file with a thematic models.json file

Select and retrieve a models.json file.
Then replace the models.json file located in /usr/src/app/api/src/serge/data/ of the docker container.

## 🧠 Supported Models

| Directory    | Description    | Models    |
|:------------:|:--------------------------------:|:---------:|
| **All** | All models | AlBfred 40B-1023; Asclepius 13B; BioMistral 7B; Code 13B, 33B; CodeLLaMA 7B, 7B-Instruct, 7B-Python, 13B, 13B-Instruct, 13B-Python, 34B, 34B-Instruct, 34B-Python? 70B, 70B-Instruct, 70B-Python; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Gemma 2B, 2B-Instruct, 7B, 7B-Instruct; Finance Chat, LLM, LLM-13B; LLaMA 2 7B, 7B-Chat, 7B-Coder, 13B, 13B-Chat, 70B, 70B-Chat, 70B-OASST; LLamA Pro 8B, 8B-Instruct; Med42 70B; Medalpaca 13B; Medicine: Chat, LLM, LLM 13B; Meditron 7B, 7B-Chat, 70B; Mistral 7B-v0.1, 7B-Instruct-v0.2, 7B-OpenOrca; MistralLite 7B; Mixtral 8x7B-v0.1, 8x7B-Dolphin-2.7, 8x7B-Instruct-v0.1, SlimOrca 8x7B; Neural-Chat 7B-v3.3; Notus 7B-v1; Notux 8x7b-v1; Nous-Hermes-2 Mistral-7B-DPO, Mixtral-8x7B-DPO, Mistral-8x7B-SFT; OpenChat 7B-v3.5-0106; OpenLLaMA 3B-v2, 7B-v2, 13B-v2; Orca 2 7B, 13B; Phi 2 2.7B; Python Code 13B, 33B; PsyMedRP 13B-v1, 20B-v1; SlimOrca 13B; Sqlcoder 2 15B; Starling LM 7B-Alpha; Tinyllama 1.1B Chat v1.0, 1.1B Chat Medical; Vicuna 7B-v1.5, 13B-v1.5, 33B-v1.3, 33B-Coder; Vigogne 2 7B-Chat, 7B-Instruct, 13B-Instruct, 70B-Chat; Wizard Coder-33B-v1.1; LM-7B-v1.0, LM-13B-v1.2, LM-70B-v1.0, Math-7B-v1.1, 13B-v1.0, 70B-v1.0; Zephyr 3B, 7B-Alpha, 7B-Beta |

| Directory    | Description    | Models    |
|:------------:|:--------------------------------:|:---------:|
| **Generic** | Models trained for english language | CodeLLaMA 7B, 7B-Instruct, 7B-Python, 13B, 13B-Instruct, 13B-Python, 34B, 34B-Instruct, 34B-Python, 70B, 70B-Instruct; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Gemma 2B, 2B-Instruct, 7B, 7B-Instruct; LLaMA 2 7B, 7B-Chat, 7B-Coder, 13B, 13B-Chat, 70B, 70B-Chat; LLamA Pro 8B, 8B-Instruct; Mistral 7B-v0.1, 7B-Instruct-v0.2, 7B-OpenOrca; MistralLite 7B; Mixtral 8x7B-v0.1, 8x7B-Dolphin-2.7, 8x7B-Instruct-v0.1, SlimOrca 8x7B; Neural-Chat 7B-v3.3; Notus 7B-v1; Notux 8x7b-v1; Nous-Hermes-2 Mistral-7B-DPO, Mixtral-8x7B-DPO, Mistral-8x7B-SFT; OpenChat 7B-v3.5-0106; OpenLLaMA 3B-v2, 7B-v2, 13B-v2; Orca 2 7B, 13B; Phi 2 2.7B; SlimOrca 13B; Starling LM 7B-Alpha; Tinyllama 1.1B Chat v1.0; Vicuna 7B-v1.5, 13B-v1.5, 33B-v1.3, 33B-Coder; Vigogne 2 7B-Chat, 7B-Instruct, 13B-Instruct, 70B-Chat; WizardL LM-7B-v1.0, LM-13B-v1.2, LM-70B-v1.0; Zephyr 3B, 7B-Alpha, 7B-Beta |

| Directory    | Description    | Models    |
|:------------:|:--------------------------------:|:---------:|
| **Tiny** | Models <= 7B params | CodeLLaMA 7B, 7B-Instruct; Falcon 7B, 7B-Instruct; Gemma 2B, 2B-Instruct, 7B, 7B-Instruct; LLaMA 2 7B, 7B-Chat; Meditron 7B, 7B-Chat; Mistral 7B-v0.1, 7B-Instruct-v0.2; MistralLite 7B; Neural-Chat 7B-v3.3; Notus 7B-v1; Nous-Hermes-2 Mistral-7B-DPO, Mixtral-8x7B-DPO, Mistral-8x7B-SFT; OpenChat 7B-v3.5-0106; OpenLLaMA 3B-v2, 7B-v2; Orca 2 7B; Phi 2 2.7B; Starling LM 7B-Alpha; Tinyllama 1.1B Chat v1.0; Vicuna 7B-v1.5; Vigogne 2 7B-Chat, 7B-Instruct; Wizard LM-7B-v1.0; Zephyr 3B, 7B-Alpha, 7B-Beta |
| **Small** | Models with 7B and <= 13B params | CodeLLaMA 13B, 13B-Instruct; LLaMA 2 13B, 13B-Chat; LLamA Pro 8B, 8B-Instruct; OpenLLaMA 13B-v2; Orca 2 13B; SlimOrca 13B; Vicuna 13B-v1.5; Vigogne 2 13B-Instruct; WizardLM 13B-v1.2 |
| **Medium** | Models with > 13B abd <=40B params | Alfred 40B-1023; CodeLLaMA 34B, 34B-Instruct; Falcon 40B, 40B-Instruct |
| **Large** | Models with >40B and <=80B params | CodeLLaMA 70B, 70B-Instruct; LLaMA 2 70B, 70B-Chat; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1; Notux 8x7b-v1, Wizard LM-70B-v1.0 |  

| Directory    | Description    | Models    |
|:------------:|:--------------------------------:|:---------:|
| **Coder** | Models trained for coding | Code 13B, 33B; CodeLLaMA 7B-Python, 13B-Python, 34B-Python, 70B-Python; LLaMA 2 7B-Coder; Sqlcoder 2 15B; Vicuna 33B-Coder; Wizard Coder-33B-v1.1 |
| **Finance** | Models trained for finance domain | Finance Chat, LLM, LLM-13B |
| **Math** | Models trained for math domain | Wizard Math-7B-v1.1, 13B-v1.0, 70B-v1.0 |
| **Medical** | Models trained for medical domain | Asclepius 13B; BioMistral 7B; Med42 70B; Medalpaca 13B; Medicine Chat, LLM, LLM 13B; Meditron 7B, 7B-Chat, 70B; PsyMedRP 13B-v1, 20B-v1; TinyLlama 1.1B Chat Medical |

| Directory    | Description    | Models    |
|:------------:|:--------------------------------:|:---------:|
| **French** | Models trained for french language | Alfred 40B-1023; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Mistral 7B-v0.1, 7B-Instruct-v0.2; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1; Vigogne 2 7B-Chat, 7B-Instruct, 13B-Instruct, 70B-Chat |
| **German** | Models trained for german language | Alfred 40B-1023; Em_German 7B, 13B, 70B; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Mistral 7B-V0.1, 7B-Instruct-v0.2; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1 |
| **Italian** | Models trained for italian language | Alfred 40B-1023; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Mistral 7B-v0.1, 7B-Instruct-v0.2; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1 |
| **Spanish** | Models trained for Spanish language |Alfred 40B-1023; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Mistral 7B-v0.1, 7B-Instruct-v0.2; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1; Spanish-FT |

