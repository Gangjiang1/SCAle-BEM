# 📄 SCAle-BEM: Self- and Cross-Consistent Agentic-LLM-Based Framework for Multimodal Automated Building Energy Modeling

**Gang Jiang**, **Jianli Chen**

This repository provides a multi-modal framework for interpreting users' multimodal inputs and converting them into corresponding building energy models. 

Different from text-only automated building energy modeling (ABEM) workflows, this repository focuses on extracting building geometry and user design intent from images, sketches, floor plans, real drawings, 3D models/pictures, and visual materials.

The framework combines vision-language models (VLMs), large language models (LLMs), prompt-based reasoning, with the proposed self-, cross-consistency, and reflection verification mechanisms to support robust building information (especially vision information) extraction. 

![High-level illustration of SCAle-BEM framework](/figs/graphic.jpg)

## 🖇 Key Contributions

- **Multimodal input support for ABEM**

- **Robust building model generation through self-consistency- and cross-consistency-enhanced inference**

- **Reflection-based LLM verification for automated building model checking**

- **Agentic collaboration workflow between LLMs and VLMs for scalable scenario generation**

## 📍 Framework Overview

The workflow includes four major stages:

1. **Vision Interpreter**
   - Takes visual building inputs (e.g., pictures and drawings) as input.
   - Uses VLMs to identify building shape and extract dimensional information.
   - Supports baseline, self-consistency, and cross-consistency modes.
   - Produces structured user prompts containing interpreted building geometry information.

2. **Intent Abstractor**
   - Takes the interpreted visual information as input.
   - Uses LLMs and predefined system prompts to abstract design intent.
   - Generates structured descriptions - intermediate representation (IR) (geometry, constructions, space types, setpoints, equipment, HVAC systems, etc.) for different building modeling components.
   - Saves the generated results into JSON files for downstream building model generation (in Building Modeler).

3. **Physics Reviewer**
   - Checks the IR based on physical rules and modeling constraints.
   - Verifies whether the interpreted geometry, dimensions, and components are reasonable.
   - Provides reflection-based feedback to correct inconsistent or physically invalid outputs.
   - Improves the reliability of automated building model generation.

4. **Building Modeler**
   - Takes the IR descriptions as input.
   - Generates the building model components.
   - Supports robust and scalable scenario generation for ABEM.

![Overall pipeline of the proposed consistent LLM multi-agent system](/figs/agent_pipeline.jpg)

## 🚀 Quick Start

This repository includes one-click-run codes, system prompts, utilities, and benchmark datasets.

## 📂 Repository Structure

```text
├── README.md
├── utility_pdf2image.ipynb              # Convert PDF files into high-resolution images
├── main_vision_interpreter.ipynb        # Main notebook for vision-based geometry interpretation
├── main_intent_abstractor.ipynb         # Main notebook for intent abstraction and description generation
├── utility_system_prompts.py            # System prompts for different LLM agents
├── utility_descriptions.py              # Template functions for building description generation
│
├── Real_Drawing/                        # Real-world building drawing inputs
├── Standard_Test_rec/                   # Standard rectangular building test cases
├── Standard_Test_yard/                  # Standard courtyard-style building test cases
├── Standard_Test_L/                     # Standard L-shaped building test cases
├── Standard_Test_T/                     # Standard T-shaped building test cases
├── Standard_Test_U/                     # Standard U-shaped building test cases
├── Hand_Sketch/                         # Hand-drawn building sketch inputs
├── Floor_Plan/                          # Floor plan image inputs
├── 3D_Picture/                          # 3D pictures and PDF-converted images
└── Standard_Test/                       # General standard test cases
```

## 🔑 API Configuration

The framework supports API-based calls to several VLM and LLM providers, including:

- Gemini
- OpenAI
- Qwen
- Claude

Before running the notebooks, configure your API keys in the corresponding sections.

## ▶️ Running the Workflow

### Step 1: Prepare visual inputs

Place the input images into one of the input folders, such as:

```text
Standard_Test/
Standard_Test_L/
Standard_Test_T/
Standard_Test_U/
Hand_Sketch/
Floor_Plan/
Real_Drawing/
3D_Picture/
```

Supported image formats include:

```text
.png
.jpg
.jpeg
.webp
```

If your input is a PDF file, first run:

```text
utility_pdf2image.ipynb
```

This notebook converts PDF files into high-resolution PNG images.

### Step 2: Run the vision interpreter

Open:

```text
main_vision_interpreter.ipynb
```

Set the input folder:

```python
picture_path = "./Standard_Test"
```

Choose the inference mode:

```python
RUN_MODE = "baseline"
```

Available inference modes include:

| Mode | Description |
|---|---|
| `baseline` | Single-model inference. This mode is fast and economical. |
| `self_consistency` | Repeated inference using one selected model, followed by consistency-based aggregation. |
| `cross_consistency` | Multi-model inference across different VLM providers, followed by cross-model aggregation. |

If using baseline or self-consistency mode, choose a model provider:

```python
candidate = "gemini"
```

Available candidates include:

```text
gemini
openai
qwen
claude
```

The vision interpreter will generate Python files containing extracted user prompts, such as:

```text
user_prompts_3_baseline_gemini.py
user_prompts_3_self_consistency_qwen.py
user_prompts_3_cross_consistency.py
```

### Step 3: Run the intent abstractor

Open:

```text
main_intent_abstractor.ipynb
```

Import the generated user prompts:

```python
from user_prompts import USER_PROMPTS
```

Run the notebook to generate structured building descriptions.

The output will be saved as a JSON file, for example:

```text
multi-modal_to_specific_description_Mar19.json
```

## 📊 Supported Building Information

The framework can generate descriptions for the following building modeling components:

### Geometry

- Rectangular buildings
- L-shaped buildings
- T-shaped buildings
- U-shaped buildings
- Courtyard or hollow-square buildings
- Single-story buildings
- Multi-story buildings
- Flat roofs
- Gable roofs
- Hip roofs

### Building Information

- Construction information
- Space information
- Thermal setpoint information
- Air-side HVAC systems
- Water-side HVAC systems

### HVAC Systems

Supported air-side system descriptions include:

- Fan coil unit systems
- Variable refrigerant flow systems
- Variable air volume systems
- Packaged DX electric systems
- DOAS with fan coil unit systems

Supported water-side system descriptions include:

- Chilled water systems
- Hot water systems
- Condenser water systems

## 📁 Main Files

### `main_vision_interpreter.ipynb`

This notebook implements the visual interpretation pipeline. It reads building images, calls selected VLMs, extracts shape-specific geometry information, and generates structured user prompts for downstream processing.

### `main_intent_abstractor.ipynb`

This notebook implements the intent abstraction stage. It converts interpreted visual information into standardized building descriptions using LLMs, system prompts, and description templates.

### `utility_system_prompts.py`

This file stores system prompts for different agents, including geometry abstraction, building information abstraction, air system abstraction, water system abstraction, and reflective verification.

### `utility_descriptions.py`

This file contains template-based description-generation functions for geometry, construction, space information, setpoints, air systems, and water systems.

### `utility_pdf2image.ipynb`

This notebook converts PDF-based visual inputs into high-resolution PNG images for use in the vision interpreter.

## 📌 Notes

- The notebooks are designed for research and experimental ABEM workflows.
- Model outputs may vary depending on the selected model, image quality, prompt design, and inference mode.
- Cross-consistency mode is generally more robust but requires more API calls.
- Users should manually inspect generated results before using them in downstream building energy simulation workflows.
- Do not commit real API keys to GitHub.

## 📝 Citation

If you find this work useful, please cite the associated paper or project:

```bibtex
@misc{jiang2026multimodal_abem,
  author       = {Gang Jiang and Zhihao Ma and Liang Zhang and Jianli Chen},
  title        = {Multi-Modal Building Design Interpretation for Automated Building Energy Modeling},
  year         = {2026},
  note         = {GitHub repository}
}
```

## 📄 License

- Apache License 2.0

