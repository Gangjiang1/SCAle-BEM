# 📄 SCAle-BEM: Self- and Cross-Consistent Agentic-LLM-Based Framework for Multimodal Automated Building Energy Modeling

**Gang Jiang**, **Jianli Chen**

This repository provides a multi-modal framework for interpreting users' multimodal inputs and converting them into corresponding building energy models. 

Different from text-only automated building energy modeling (ABEM) workflows, this repository focuses on extracting building geometry and user design intent from images, sketches, floor plans, real drawings, 3D models/pictures, and visual materials.

The framework combines vision-language models (VLMs), large language models (LLMs), prompt-based reasoning, with the proposed self-, cross-consistency, and reflection verification mechanisms to support robust building information (especially vision information) extraction. 

<p align="center">
  <img src="/figs/graphic.png" alt="High-level illustration of SCAle-BEM framework" width="800">
</p>

<p align="center">
  <em>High-level illustration of the SCAle-BEM framework.</em>
</p>

## 🖇 Key Contributions

- **Multimodal input support for ABEM**

- **Robust building model generation through self-consistency- and cross-consistency-enhanced inference**

- **Reflection-based LLM verification for automated building model checking**

- **Agentic collaboration workflow between LLMs and VLMs for scalable scenario generation**

## 📊 Supported Features and Scenarios

The SCAle framework can generate building models for the following building modeling components with robustness and scalability:

### Geometry

- Rectangular buildings
- L-shaped buildings
- T-shaped buildings
- U-shaped buildings
- Hollow-square (courtyard) buildings
- Single-story buildings
- Multi-story buildings
- Flat roofs
- Gable roofs
- Hip roofs
- Window-to-wall ratials

### Building Information

- Constructions and materials
- Space types
- Thermal zones
- Thermostat setpoints
- Internal loads
- Schedules
- Air-side HVAC systems
- Water-side HVAC systems

### HVAC Systems

Supported air-side system descriptions include:

- Fan coil unit systems
- Variable refrigerant flow systems
- Variable air volume systems
- Packaged DX electric systems
- DOAS with fan coil unit systems
- Hybrid systems

Supported water-side system descriptions include:

- Chilled water systems
- Hot water systems
- Condenser water systems

<p align="center">
  <img src="/figs/scenarios.png" alt="Supported ABEM Scenarios" width="800">
</p>

<p align="center">
  <em>Supported ABEM Scenarios.</em>
</p>

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

<p align="center">
  <img src="/figs/agent_pipeline.png" alt="Overall pipeline of the proposed consistent LLM multi-agent system" width="600">
</p>

<p align="center">
  <em>Overall pipeline of the proposed consistent LLM multi-agent system.</em>
</p>

## 📂 Repository Structure

```text
├── README.md
├── utility_pdf2image.ipynb              # Convert PDF files into high-resolution images for VLMs
├── main_vision_interpreter.ipynb        # Main code for vision interpreter
├── main_intent_abstractor.ipynb         # Main code for intent abstractor
├── utility_system_prompts.py            # System prompts for LLM/VLM agents
├── utility_descriptions.py              # Template functions for building description generation
│
├── Standard_Test/                       # General standard benchmark dataset
├── Real_Drawing/                        # Real-world building drawing benchmark dataset
├── Hand_Sketch/                         # Hand-drawn building sketch benchmark dataset
├── Floor_Plan/                          # Floor plan image benchmark dataset
└── 3D_Picture/                          # 3D pictures/models benchmark dataset
```

## 🚀 Quick Start

This repository includes one-click-run codes, system prompts, utilities, and benchmark datasets.

### 🔑 API Configuration

The framework supports API-based calls to several VLM and LLM providers, including:

- Gemini
- OpenAI
- Qwen
- Claude

Before running the notebooks, configure your API keys in the corresponding sections.

### ▶️ Running the Workflow

Place the input images into one of the input folders, such as:

```text
Standard_Test/
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

This code converts PDF files into high-resolution PNG images.

### 📏 Selecting Self- and Cross-Consistency Strageties

| Mode | Description |
|---|---|
| `vanilla` | Single-model inference baseline. |
| `self_consistency` | Multi-inference using one selected VLM, followed by self-consistency aggregation. |
| `cross_consistency` | Multi-inference across different VLM providers, followed by cross-consistency aggregation. |

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

### 📌 Notes

- The shared code is designed for research and experimental ABEM workflows.
- Model outputs may vary depending on the selected LLMs and VLMs, image quality, prompt design, and inference mode. Users are encouraged to strictly follow the provided code examples to ensure reproducibility.
- Cross-consistency mode is generally more robust but requires more API calls and may lead to higher costs. Please check your API usage and billing information regularly.

### 📝 Citation

- Paper coming soon.

### 📄 License

- Apache License 2.0

