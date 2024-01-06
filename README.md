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
| **All** | All models | Alfred 40B-1023; Asclepius 13B; Code 13B, 33B; CodeLLaMA 7B, 7B-Instruct, 7B-Python, 13B, 13B-Instruct, 13B-Python, 34B, 34B-Instruct, 34B-Python; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; LLaMA 2 7B, 7B-Chat, 7B-Coder, 13B, 13B-Chat, 70B, 70B-Chat, 70B-OASST; Med42  70B; Medalpaca 13B; Medicine-LLM 13B; Meditron 7B, 7B-Chat, 70B; Mistral 7B-V0.1, 7B-Instruct-v0.2, 7B-OpenOrca; MistralLite 7B; Mixtral 8x7B-v0.1, 8x7B-Dolphin-2.7, 8x7B-Instruct-v0.1; Neural-Chat 7B-v3.3; Notus 7B-v1; Notux 8x7b-v1; OpenChat 7B-v3.5-1210; OpenLLaMA 3B-v2, 7B-v2, 13B-v2; Orca 2 7B, 13B; Phi 2 2.7B; Python Code 13B, 33B; PsyMedRP 13B-v1, 20B-v1; SlimOrca 13B; Sqlcoder 2 15B; Starling LM 7B-Alpha; Tinyllama 1.1B Chat v1.0; Vicuna 7B-v1.5, 13B-v1.5, 33B-v1.3, 33B-Coder; Vigogne 2 7B-Chat, 7B-Instruct, 13B-Instruct, 70B-Chat; WizardLM 7B-v1.0, 13B-v1.2, 70B-v1.0; Zephyr 3B, 7B-Alpha, 7B-Beta |
|              |                                  |           |
| **Tiny** | Models <= 7B params | CodeLLaMA 7B, 7B-Instruct; Falcon 7B, 7B-Instruct; LLaMA 2 7B, 7B-Chat; Meditron 7B, 7B-Chat; Mistral 7B-V0.1, 7B-Instruct-v0.2; MistralLite 7B; Neural-Chat 7B-v3.3; Notus 7B-v1 OpenChat 7B-v3.5-1210; OpenLLaMA 3B-v2, 7B-v2; Orca 2 7B; Phi 2 2.7B; Starling LM 7B-Alpha; Tinyllama 1.1B Chat v1.0; Vicuna 7B-v1.5; Vigogne 2 7B-Chat, 7B-Instruct; WizardLM 7B-v1.0; Zephyr 3B, 7B-Alpha, 7B-Beta |
| **Small** | Models with 7B and <= 13B params | CodeLLaMA 13B, 13B-Instruct; LLaMA 2 13B, 13B-Chat; OpenLLaMA 13B-v2; Orca 2 13B; SlimOrca 13B; Vicuna 13B-v1.5; Vigogne 2 13B-Instruct; WizardLM 13B-v1.2 |
| **Medium** | Models with > 13B abd <=40B params | Alfred 40B-1023; CodeLLaMA 34B, 34B-Instruct; Falcon 40B, 40B-Instruct |
| **Large** | Models with >40B and <=80B params | LLaMA 2 70B, 70B-Chat; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1; Notux 8x7b-v1, WizardLM 70B-v1.0 |  
|              |                                  |           |  
| **Coder** | Models for coders | Code 13B, 33B; CodeLLaMA 7B-Python, 13B-Python, 34B-Python; LLaMA 2 7B-Coder; Sqlcoder 2 15B; Vicuna 33B-Coder |
| **Medical** | Models for medical domain | Asclepius 13B; Med42 70B; Medalpaca 13B; Medicine-LLM 13B; Meditron 7B, 7B-Chat, 70B; PsyMedRP 13B-v1, 20B-v1 |
|              |                                  |           |
| **French** | Models trained for french language | Alfred 40B-1023; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Mistral 7B-V0.1, 7B-Instruct-v0.2; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1; Vigogne 2 7B-Chat, 7B-Instruct, 13B-Instruct, 70B-Chat |
| **Generic** | Models trained for english language | CodeLLaMA 7B, 7B-Instruct, 7B-Python, 13B, 13B-Instruct, 13B-Python, 34B, 34B-Instruct, 34B-Python; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; LLaMA 2 7B, 7B-Chat, 7B-Coder, 13B, 13B-Chat, 70B, 70B-Chat; Mistral 7B-V0.1, 7B-Instruct-v0.2, 7B-OpenOrca; MistralLite 7B; Mixtral 8x7B-v0.1, 8x7B-Dolphin-2.7, 8x7B-Instruct-v0.1; Neural-Chat 7B-v3.3; Notus 7B-v1; Notux 8x7b-v1; OpenChat 7B-v3.5-1210; OpenLLaMA 3B-v2, 7B-v2, 13B-v2; Orca 2 7B, 13B; Phi 2 2.7B; SlimOrca 13B; Starling LM 7B-Alpha; Tinyllama 1.1B Chat v1.0; Vicuna 7B-v1.5, 13B-v1.5, 33B-v1.3, 33B-Coder; Vigogne 2 7B-Chat, 7B-Instruct, 13B-Instruct, 70B-Chat; WizardLM 7B-v1.0, 13B-v1.2, 70B-v1.0; Zephyr 3B, 7B-Alpha, 7B-Beta |
| **German** | Models trained for german language | Alfred 40B-1023; Em_German 7B, 13B, 70B; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Mistral 7B-V0.1, 7B-Instruct-v0.2; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1 |
| **Italian** | Models trained for italian language | Alfred 40B-1023; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Mistral 7B-V0.1, 7B-Instruct-v0.2; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1 |
| **Spanish** | Models trained for Spanish language |Alfred 40B-1023; Falcon 7B, 7B-Instruct, 40B, 40B-Instruct; Mistral 7B-V0.1, 7B-Instruct-v0.2; Mixtral 8x7B-v0.1, 8x7B-Instruct-v0.1; Spanish-FT |

