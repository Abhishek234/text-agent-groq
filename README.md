# Email Summarizer

A Python script that uses OpenAI's GPT API to generate concise summaries of email content.

## Features

- 📧 Interactive email input
- 🤖 AI-powered summarization using GPT-3.5-turbo
- 🔐 Secure API key handling
- ⚡ Fast and efficient processing
- 🛡️ Comprehensive error handling

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. **Clone or download the files** to your local machine

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   
   **Option 1: .env file (recommended)**
   ```bash
   # Copy the template and add your API key
   cp config.env .env
   # Edit .env and replace 'your-openai-api-key-here' with your actual API key
   ```
   
   **Option 2: Environment variable**
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   
   **Option 3: Enter when prompted**
   - The script will prompt you to enter your API key if not found in environment variables

## Usage

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Enter your email content**:
   - The script will prompt you to enter the email content
   - Type or paste your email text
   - Press `Ctrl+D` (Unix/Mac) or `Ctrl+Z` (Windows) when finished

3. **View the summary**:
   - The script will generate and display a concise summary

## Example

```
📧 Email Summarizer
==================================================
Enter your email content below (press Ctrl+D or Ctrl+Z when finished):
--------------------------------------------------
Subject: Project Update - Q4 Goals
From: john.doe@company.com
To: team@company.com

Hi Team,

I wanted to provide an update on our Q4 objectives. We've made significant 
progress on the new product launch, with development at 75% completion. 
The marketing campaign is scheduled to begin next week, and we're on track 
to meet our December 15th deadline.

Please review the attached project timeline and let me know if you have 
any questions or concerns.

Best regards,
John

🔄 Generating summary...

==================================================
📋 EMAIL SUMMARY
==================================================
John provides a Q4 project update indicating 75% completion of the new 
product launch with marketing starting next week. The team is on track 
for the December 15th deadline and should review the attached timeline.
==================================================
```

## Configuration

The script uses the following default settings:
- **Model**: GPT-3.5-turbo
- **Max tokens**: 150 (for summary length)
- **Temperature**: 0.3 (for consistent output)

You can modify these settings in the `summarize_email()` function in `main.py`.

## Error Handling

The script handles various error scenarios:
- Missing or invalid API key
- Network connectivity issues
- Rate limiting
- API errors
- Invalid input

## Security Notes

- Never commit your API key to version control
- Use environment variables for production deployments
- The script doesn't store your API key locally

## Troubleshooting

**"Authentication failed" error**:
- Verify your API key is correct
- Ensure you have sufficient credits in your OpenAI account

**"Rate limit exceeded" error**:
- Wait a moment and try again
- Consider upgrading your OpenAI plan if this happens frequently

**"No module named 'openai'" error**:
- Run `pip install -r requirements.txt` to install dependencies

## License

This project is open source and available under the MIT License. 