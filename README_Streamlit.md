# API Rate Limiter - Streamlit Version

A beautiful, production-ready API rate limiting system built with Streamlit. Features a stunning pink gradient theme with glassmorphism effects and real-time traffic control capabilities.

![API Rate Limiter](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=1200&h=400&fit=crop)

## ✨ Features

### 🎨 Beautiful Design
- **Pink Gradient Theme**: Stunning gradient background with glassmorphism effects
- **Interactive Dashboard**: Real-time metrics and analytics
- **Responsive Layout**: Optimized for all screen sizes
- **Modern UI Components**: Custom styled Streamlit components

### 🛡️ Processing Modes
- **Uppercase**: Convert text to uppercase letters
- **Reverse**: Reverse the input string character by character
- **Count**: Count characters and words in the input
- **Base64 Hash**: Generate base64 encoded representation
- **MD5 Hash**: Generate MD5 hash of the input
- **Word Frequency**: Find the most frequent word in text

### 📊 Real-time Analytics
- **Processing History**: Complete log of all operations with timestamps
- **System Statistics**: Live metrics including total operations and processing times
- **Performance Charts**: Visual analytics with Plotly charts
- **Mode Distribution**: Pie charts showing processing mode usage

### 🚀 Advanced Features
- **Configurable Rate Limiting**: Adjustable request limits and time windows
- **Simulated Processing**: Realistic processing delays for demonstration
- **Performance Monitoring**: Detailed timing and performance metrics
- **Data Export**: Processing history with full analytics

## 🛠️ Tech Stack

- **Framework**: Streamlit
- **Data Processing**: Pandas
- **Visualizations**: Plotly
- **Styling**: Custom CSS with glassmorphism effects
- **Icons**: Unicode emojis and symbols

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd api-rate-limiter-streamlit
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   The app will automatically open at `http://localhost:8501`

## 🎯 Usage

### Basic Operation
1. **Select Processing Mode**: Choose from 6 different processing modes
2. **Configure Settings**: Adjust rate limiting and processing settings in sidebar
3. **Enter Input**: Type or paste your data in the input textarea
4. **Process**: Click the "Process Input" button to transform your data
5. **View Results**: See processed output and analytics

### Processing Modes Explained

#### Uppercase Mode 🔤
Converts all text to uppercase letters.
```
Input: "Hello World"
Output: "HELLO WORLD"
```

#### Reverse Mode 🔄
Reverses the character order of the input string.
```
Input: "Hello World"
Output: "dlroW olleH"
```

#### Count Mode 📊
Provides character and word count statistics.
```
Input: "Hello World"
Output: "Characters: 11, Words: 2"
```

#### Base64 Hash Mode 🔐
Generates a base64 encoded representation.
```
Input: "Hello World"
Output: "Base64: SGVsbG8gV29ybGQ=..."
```

#### MD5 Hash Mode 🔑
Generates MD5 hash of the input.
```
Input: "Hello World"
Output: "MD5: b10a8db164e0754105b7a99be72e3fe5"
```

#### Word Frequency Mode 📈
Finds the most frequent word in text.
```
Input: "hello world hello"
Output: "Most frequent word: 'hello' (2 times)"
```

### Configuration Options

#### Rate Limiting Settings
- **Max Requests per Minute**: 1-100 requests
- **Time Window**: 10-300 seconds
- **Processing Delay**: Configurable simulation delay

#### System Actions
- **Clear History**: Reset all processing history and statistics
- **Export Data**: Download processing history as CSV

### Analytics Dashboard

#### Real-time Metrics
- **Total Operations**: Count of all processing operations
- **Average Processing Time**: Mean processing duration
- **Recent Activity**: Operations in the last minute
- **System Status**: Real-time health indicator

#### Visual Analytics
- **Processing Time Charts**: Line charts showing performance over time
- **Mode Distribution**: Pie charts showing usage patterns
- **Performance Statistics**: Min, max, and standard deviation metrics

## 🏗️ Project Structure

```
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README_Streamlit.md      # This documentation
└── .streamlit/
    └── config.toml          # Streamlit configuration (optional)
```

## 🎨 Design System

### Color Palette
- **Primary Pink**: Various shades from light to dark pink
- **Glassmorphism**: Semi-transparent backgrounds with blur effects
- **Gradients**: Smooth color transitions throughout the UI
- **Accent Colors**: Green for success, red for errors

### Components
- **Metric Cards**: Glassmorphism effect with backdrop blur
- **Processing Cards**: Enhanced cards for main functionality
- **Interactive Charts**: Plotly visualizations with custom styling
- **Responsive Layout**: Streamlit columns and containers

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py --server.port 8501
```

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy with one click

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Heroku Deployment
1. Create `setup.sh` and `Procfile`
2. Configure buildpacks
3. Deploy via Git or GitHub integration

## 🔧 Configuration

### Streamlit Configuration
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#ec4899"
backgroundColor = "#fce7f3"
secondaryBackgroundColor = "#fdf2f8"
textColor = "#831843"

[server]
maxUploadSize = 200
```

### Custom Styling
The app uses extensive custom CSS for:
- Glassmorphism effects
- Pink gradient themes
- Responsive design
- Interactive animations

## 📊 Performance

### Optimization Features
- **Session State Management**: Efficient state handling
- **History Limiting**: Maximum 50 entries for performance
- **Lazy Loading**: Charts load only when needed
- **Caching**: Streamlit caching for better performance

### Monitoring
- Real-time processing time tracking
- Performance analytics and charts
- System health indicators
- Usage pattern analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit Team** for the amazing framework
- **Plotly** for beautiful interactive charts
- **Pandas** for data processing capabilities
- **Python Community** for excellent libraries

---

<div align="center">
  <p>🛡️ Built with ❤️ and Streamlit</p>
  <p>Ready for production deployment</p>
</div>
```