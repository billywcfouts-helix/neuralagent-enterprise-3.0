# NeuralAgent Enterprise Automation 3.0

**Grok-Powered Local Desktop AI Agent System**

> Full source code available in the Google Drive folder:
> https://drive.google.com/drive/folders/1l6DUqxxWHSAu0rK8irrj_NdD47406Ugf

A local-first AI that **sees your screen**, controls mouse & keyboard, plans complex multi-step workflows, records successful tasks as reusable **Fast Replays** (with OCR visual anchoring), supports specialized sub-agents, and provides a beautiful modern Streamlit dashboard.

### Key Features

- **Auto .env creation** on first run
- **OCR-powered visual anchoring** in replays (robust to UI changes)
- **Full Watch & Learn recording** using real pynput mouse/keyboard listeners
- **Specialized Agents**: Research, Code, Growth, Browser (Playwright hybrid)
- **Live Real ↔ Simulated mode switching** with prominent warning banner
- Modern beautiful Streamlit GUI with KPIs, live logs, replay library
- Enterprise-grade safety, audit logging, and Fast Replays
- LLM brain: Grok primary → OpenRouter Owl Alpha fallback → optional local Ollama + Dolphin

### Quick Start

1. Download the full project ZIP from Google Drive
2. Unzip
3. ```bash
   cd neuralagent-enterprise-automation
   pip install -r requirements.txt
   streamlit run gui/app.py
   ```

On first run, the `.env` file is created automatically for you.

### Build Standalone Executable

```bash
python build_executable.py
```

The executable will be created in `dist/`.

### Repository
This repo contains the core structure and documentation. The complete Python source is in the Google Drive ZIP linked above.