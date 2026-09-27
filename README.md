🤖 AI Agent Engineering
Welcome to the AI Agent Engineering learning repository! This repo is designed as a structured, day-by-day guide to help you build and understand Agentic AI from the ground up using locally hosted models.

📌 About This Repository
Day-by-Day Learning Path: Structured content progressing step-by-step from foundational concepts to advanced agent architectures.

Daily Notes: Each directory includes dedicated notes explaining the core concepts, goals, and hands-on exercises for that day.

100% Local Execution: Powered by Ollama to run light, capable LLMs directly on your machine without external API fees.

⚙️ Prerequisites & Setup
Before getting started, make sure you have python, Ollama installed on your system (Windows or macOS).

## ⚙️ Setup: Ollama & Local Model

This guide covers the setup required to run the AI Agent Engineering projects using a locally hosted LLM with Ollama.

2. Install Ollama

Ollama allows you to run LLMs locally on your machine without requiring external API services.

Download Ollama

Install Ollama for your operating system:

👉 Download Ollama

After installation, verify that Ollama is available:

ollama --version

If the installation was successful, you should see the installed Ollama version.

3. Pull & Run the Local Model

This project uses Qwen3 4B as the default local model.

Pull the Model

Open your terminal and run:

ollama pull qwen3:4b

This downloads the Qwen3 4B model to your local machine.

Run the Model

Start the model with:

ollama run qwen3:4b

You can now interact with the model directly through the terminal.

Local API

When Ollama is running, it provides an OpenAI-compatible API endpoint:

http://localhost:11434/v1

This endpoint will be used by the Python applications in this repository to communicate with the locally hosted model. 

## Environment Configuration
Create a .env file in the project root directory and add the following configuration:

Code snippet
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=qwen3:4b

🚀 Getting Started
Clone the repository:

Bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/ChandraKiran34/AI-Agent-Engineering.git)
cd AGENTIC-AI
