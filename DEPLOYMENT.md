# 🚀 Deployment Guide for Streamlit Cloud

This guide will help you deploy your Text Agent app on Streamlit Cloud for public access.

## 📋 Prerequisites

1. **GitHub Account**: You need a GitHub account
2. **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io)
3. **Groq API Key**: Get your API key from [console.groq.com](https://console.groq.com)

## 🔧 Setup Steps

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and click "New repository"
2. Name it something like `text-agent-groq`
3. Make it **Public** (required for free Streamlit Cloud)
4. Don't initialize with README (we'll push our code)

### 2. Push Your Code

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Text Agent with Groq API"

# Add remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/YOUR_USERNAME/text-agent-groq.git

# Push to GitHub
git push -u origin main
```

### 3. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/text-agent-groq`
5. Set the main file path: `agent_ui.py`
6. Click "Deploy"

### 4. Configure Environment Variables

1. In your Streamlit Cloud app dashboard
2. Go to "Settings" → "Secrets"
3. Add your Groq API key:

```toml
GROQ_API_KEY = "gsk_your_actual_api_key_here"
```

## 🔒 Security Notes

- ✅ Never commit your API key to GitHub
- ✅ Use Streamlit Cloud's secrets management
- ✅ The `.env` file is already in `.gitignore`

## 🌐 Your App URL

Once deployed, your app will be available at:
```
https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app
```

## 🐛 Troubleshooting

### Common Issues:

1. **"Module not found" errors**: Make sure `requirements.txt` is in the root directory
2. **API key errors**: Check that you've set the secret correctly in Streamlit Cloud
3. **Model errors**: The app uses `llama3-8b-8192` which should be available on Groq

### Support:

- Check Streamlit Cloud logs in your app dashboard
- Verify your Groq API key is valid
- Ensure all dependencies are listed in `requirements.txt`

## 📱 Features

Your deployed app will have:
- ✅ Text summarization
- ✅ Text rewriting
- ✅ Email composition
- ✅ Tone changing
- ✅ Real-time processing with Groq LLMs 