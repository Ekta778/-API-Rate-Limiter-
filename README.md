# API Rate Limiter

A beautiful, production-ready API rate limiting system built with React, TypeScript, and Tailwind CSS. Features a stunning pink gradient theme with glassmorphism effects and real-time traffic control capabilities.

![API Rate Limiter](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=1200&h=400&fit=crop)

## ✨ Features

### 🎨 Beautiful Design
- **Pink Gradient Theme**: Stunning gradient background from deep pink to rose tones
- **Glassmorphism Effects**: Modern frosted glass UI components with backdrop blur
- **Responsive Design**: Optimized for all screen sizes from mobile to desktop
- **Smooth Animations**: Elegant transitions and hover effects throughout

### 🛡️ Rate Limiting Modes
- **Uppercase**: Convert text to uppercase letters
- **Reverse**: Reverse the input string character by character
- **Count**: Count characters and words in the input
- **Hash**: Generate base64 hash representation

### 📊 Real-time Analytics
- **Processing History**: Complete log of all operations with timestamps
- **System Statistics**: Live metrics including total operations and processing times
- **Performance Monitoring**: Average processing time tracking
- **Activity Tracking**: Recent operations per minute counter

### 🚀 Advanced Features
- **Simulated Processing**: Realistic processing delays for demonstration
- **Input Validation**: Smart input handling and validation
- **History Management**: Maintains last 50 operations for performance
- **Clear Functionality**: Easy reset for input, output, and history

## 🛠️ Tech Stack

- **Frontend**: React 18 with TypeScript
- **Styling**: Tailwind CSS with custom pink theme
- **Icons**: Lucide React icon library
- **Build Tool**: Vite for fast development and building
- **Code Quality**: ESLint with TypeScript support

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd api-rate-limiter
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open in browser**
   Navigate to `http://localhost:5173`

## 🎯 Usage

### Basic Operation
1. **Select Processing Mode**: Choose from Uppercase, Reverse, Count, or Hash
2. **Enter Input**: Type or paste your data in the input textarea
3. **Process**: Click the "Process Input" button to transform your data
4. **View Results**: See the processed output in the output section

### Processing Modes Explained

#### Uppercase Mode
Converts all text to uppercase letters.
```
Input: "Hello World"
Output: "HELLO WORLD"
```

#### Reverse Mode
Reverses the character order of the input string.
```
Input: "Hello World"
Output: "dlroW olleH"
```

#### Count Mode
Provides character and word count statistics.
```
Input: "Hello World"
Output: "Characters: 11, Words: 2"
```

#### Hash Mode
Generates a base64 hash representation.
```
Input: "Hello World"
Output: "Hash: SGVsbG8gV29ybGQ=..."
```

### Advanced Features

#### Processing History
- View complete history of all processing operations
- Each entry shows input, output, timestamp, and processing time
- Automatically truncates long text for better readability
- Maintains last 50 operations for optimal performance

#### System Statistics
- **Total Operations**: Count of all processing operations
- **Average Processing Time**: Mean processing duration in milliseconds
- **Recent Activity**: Operations performed in the last minute
- **System Status**: Real-time system health indicator

## 🏗️ Project Structure

```
src/
├── components/
│   ├── InputOutputSystem.tsx    # Main rate limiting interface
│   ├── ProcessingHistory.tsx    # History display component
│   └── SystemStats.tsx          # Statistics dashboard
├── App.tsx                      # Root application component
├── main.tsx                     # Application entry point
├── index.css                    # Global styles and Tailwind imports
└── vite-env.d.ts               # Vite type definitions
```

## 🎨 Design System

### Color Palette
- **Primary Pink**: `pink-600` to `pink-900`
- **Rose Accents**: `rose-300` to `rose-800`
- **Fuchsia Highlights**: `fuchsia-300` to `fuchsia-500`
- **Background**: Gradient from `pink-900` via `pink-800` to `rose-900`

### Typography
- **Headings**: Bold, white text with proper hierarchy
- **Body Text**: Pink-200 for primary content
- **Monospace**: Used for input/output display and technical data
- **Responsive**: Scales appropriately across all devices

### Components
- **Cards**: Glassmorphism effect with `backdrop-blur-sm`
- **Buttons**: Pink gradient with hover states
- **Inputs**: Pink-themed with focus states
- **Borders**: Subtle pink borders with transparency

## 🚀 Build & Deploy

### Development
```bash
npm run dev          # Start development server
npm run lint         # Run ESLint checks
```

### Production
```bash
npm run build        # Build for production
npm run preview      # Preview production build
```

### Deployment
The application can be deployed to any static hosting service:
- **Netlify**: Drag and drop the `dist` folder
- **Vercel**: Connect your Git repository
- **GitHub Pages**: Use GitHub Actions for automated deployment

## 🔧 Configuration

### Tailwind CSS
The project uses a custom Tailwind configuration optimized for the pink theme. Modify `tailwind.config.js` to customize colors, spacing, or add new utilities.

### Processing Modes
Add new processing modes by:
1. Extending the `processingMode` type in `InputOutputSystem.tsx`
2. Adding the new mode to the `processingModes` array
3. Implementing the processing logic in the `processInput` function

### Performance Tuning
- History is limited to 50 items for optimal performance
- Processing delays are simulated (500ms + random 0-1000ms)
- Components use React hooks for efficient state management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **React Team** for the amazing framework
- **Tailwind CSS** for the utility-first CSS framework
- **Lucide** for the beautiful icon library
- **Vite** for the lightning-fast build tool

---

<div align="center">
  <p>Built with ❤️ and lots of ☕</p>
  <p>Made for production-ready applications</p>
</div>