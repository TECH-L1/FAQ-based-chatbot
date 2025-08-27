# FAQ-based-chatbot
This project is an **FAQ-based chatbot** designed to support HCP (HashiCorp Cloud Platform) technical inquiries. It leverages **LangChain** and **local LLMs via Ollama** to retrieve answers from FAQ documents and delivers responses through an intuitive **Streamlit web interface**


## 🎯 Overview
This project is an **FAQ-based chatbot** designed to support HCP (HashiCorp Cloud Platform) technical inquiries. It leverages **LangChain** and **local LLMs via Ollama** to retrieve answers from FAQ documents and delivers responses through an intuitive **Streamlit web interface**.

### ✨ Key Features
1. **🏠 Local LLM Support** - Run completely offline using Ollama with DeepSeek-R1-Distill-Qwen-14B
2. **📚 Multi-Format FAQ Processing** - Support for Excel, PDF, Word, Text, and CSV files
3. **🔍 Intelligent Search** - Vector-based similarity search with FAISS
4. **💬 Interactive Web UI** - Clean Streamlit interface with conversation history
5. **🔧 Flexible Configuration** - Support both local (Ollama) and cloud (OpenAI) LLMs
6. **📊 Performance Optimized** - Local embeddings and efficient document processing

---

## 🚀 Quick Start

### Option A: Local Setup with Ollama (Recommended)
```bash
# 1. Install Ollama and pull the model
ollama pull deepseek-r1:14b

# 2. Setup the project
git clone <this-repo>
cd HCP_master
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure (default uses Ollama)
cp .env.example .env

# 4. Run the chatbot
python run.py --start
```

### Option B: OpenAI API Setup
```bash
# Follow steps 2-4 above, but edit .env file:
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here
```

---

## ⚙️ Tech Stack

### 🧠 LLM & AI
- **Ollama** (Primary) - Local LLM serving with DeepSeek-R1-Distill-Qwen-14B
- **OpenAI API** (Alternative) - Cloud-based LLM access
- **LangChain** - LLM application framework and retrieval pipeline
- **Sentence Transformers** - Local embedding generation

### 🗄️ Data & Search
- **FAISS** - Vector similarity search engine
- **ChromaDB** - Alternative vector database option
- **Pandas** - Structured data processing

### 🖥️ Interface & Processing
- **Streamlit** - Interactive web UI framework
- **PyPDF, python-docx, openpyxl** - Multi-format document processing

---

## 📁 Project Structure
```
HCP_master/
├── app.py                      # Main Streamlit application
├── run.py                      # Project runner with utilities
├── requirements.txt            # Python dependencies
├── .env.example               # Environment configuration template
├── src/
│   ├── core/
│   │   └── chatbot.py         # Main chatbot logic with Ollama support
│   ├── data/
│   │   └── faq_processor.py   # Multi-format FAQ processing
│   └── utils/
│       ├── config.py          # Configuration management
│       └── logger.py          # Logging utilities
├── data/
│   ├── faqs/                  # Your FAQ documents go here
│   └── embeddings/            # Vector store cache
├── docs/
│   ├── OLLAMA_SETUP.md        # Detailed Ollama installation guide
│   ├── SETUP.md               # General setup instructions
│   ├── USAGE.md               # User guide
│   └── SYSTEM_DOCUMENTATION.md # Complete technical documentation
└── tests/                     # Unit tests
```

---

## 🔧 Configuration Options

### LLM Provider Settings
```bash
# Local Ollama (No API costs)
LLM_PROVIDER=ollama
OLLAMA_MODEL=deepseek-r1:14b
OLLAMA_BASE_URL=http://localhost:11434

# OpenAI API (Requires API key)
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4
```

### Performance Tuning
```bash
TEMPERATURE=0.1          # Response creativity (0.0-1.0)
MAX_TOKENS=1000         # Maximum response length
CHUNK_SIZE=1000         # Document processing chunk size
RETRIEVAL_K=5           # Number of relevant chunks to retrieve
```

---

## 📚 FAQ Document Formats

### Excel Files (.xlsx)
```
Required columns: question, answer
Optional: category, tags
```

### CSV Files
```
Headers: question,answer,category,tags
Example: "How to create HCP project?","Step 1: Login to console...","Getting Started","project,setup"
```

### Text Files (.txt)
```
Q: How do I create an HCP project?
A: To create a new HCP project, follow these steps...

Q: What is HCP Consul?
A: HCP Consul is a fully managed service...
```

### PDF/Word Documents
- Automatically processed as continuous text
- Use clear Q&A formatting for best results

---

## 🏃‍♂️ Running the Application

### Using the Runner Script
```bash
# First-time setup
python run.py --setup

# Check configuration and dependencies
python run.py --check

# Start the application
python run.py --start

# Start with custom port
python run.py --start --port 8502
```

### Direct Streamlit
```bash
streamlit run app.py
```

### Using the Application
1. **Load FAQ Database**: Click "🔄 Load FAQ Database" in the sidebar
2. **Ask Questions**: Type HCP-related questions in the chat input
3. **View Responses**: Get contextual answers based on your FAQ content
4. **Manage Conversation**: Use "🗑️ Clear Conversation" to reset

---

## 🔍 Advanced Features

### Local vs Cloud LLMs
- **Ollama (Local)**: No API costs, complete privacy, requires good hardware
- **OpenAI (Cloud)**: Fastest responses, latest models, API costs apply

### Model Options
```bash
# DeepSeek models (Recommended)
ollama pull deepseek-r1:14b     # Best quality, requires 16GB+ RAM
ollama pull deepseek-r1:7b      # Good balance, requires 8GB+ RAM

# Alternative models
ollama pull llama3.1:8b         # Meta's Llama 3.1
ollama pull mistral:7b          # Mistral AI model
ollama pull phi3:mini           # Microsoft's lightweight model
```

### Performance Optimization
- **Memory**: 16GB+ RAM recommended for 14B models
- **Storage**: SSD recommended for faster model loading  
- **CPU**: Multi-core processors provide better performance
- **Embeddings**: Local Sentence Transformers (no API calls)

---

## 🛠️ Development & Testing

### Running Tests
```bash
pytest tests/
```

### Development Mode
```bash
python run.py --start --debug
```

### Adding New FAQ Sources
1. Place documents in `data/faqs/` directory
2. Supported formats: `.xlsx`, `.csv`, `.txt`, `.pdf`, `.docx`
3. Reload FAQ database in the web interface

---

## 📖 Documentation

- **[Ollama Setup Guide](docs/OLLAMA_SETUP.md)** - Detailed local LLM setup
- **[Setup Guide](docs/SETUP.md)** - General installation instructions  
- **[Usage Guide](docs/USAGE.md)** - How to use the chatbot effectively
- **[System Documentation](docs/SYSTEM_DOCUMENTATION.md)** - Complete technical reference

---

## 🔒 Privacy & Security

### Local Operation
- All FAQ processing happens on your machine
- No data sent to external services (when using Ollama)
- Conversation history stored locally only
- Complete control over your data

### Network Security
- Ollama runs on localhost by default
- No external API calls required
- Firewall-friendly operation

---

## 💡 Use Cases

### HCP Technical Support
- Product documentation Q&A
- Troubleshooting guides
- Configuration assistance
- Feature explanations

### Knowledge Management
- Internal FAQ systems
- Technical documentation
- Training materials
- Support ticket deflection

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Include tests for new functionality
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🆘 Support

- **Issues**: Report bugs and request features via GitHub Issues
- **Documentation**: Check the `docs/` directory for detailed guides
- **Community**: Join discussions in GitHub Discussions

---

**🎉 Get started in minutes with local LLMs and no API costs!**
