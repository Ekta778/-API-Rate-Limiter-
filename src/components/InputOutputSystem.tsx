import React, { useState } from 'react';
import { Play, RotateCcw, Hash, Type, ArrowUpDown, Calculator } from 'lucide-react';
import { ProcessingEntry } from '../App';

type ProcessingMode = 'uppercase' | 'reverse' | 'count' | 'hash';

interface ProcessingModeConfig {
  id: ProcessingMode;
  name: string;
  description: string;
  icon: React.ReactNode;
}

const processingModes: ProcessingModeConfig[] = [
  {
    id: 'uppercase',
    name: 'Uppercase',
    description: 'Convert text to uppercase letters',
    icon: <Type className="h-5 w-5" />
  },
  {
    id: 'reverse',
    name: 'Reverse',
    description: 'Reverse the input string',
    icon: <ArrowUpDown className="h-5 w-5" />
  },
  {
    id: 'count',
    name: 'Count',
    description: 'Count characters and words',
    icon: <Calculator className="h-5 w-5" />
  },
  {
    id: 'hash',
    name: 'Hash',
    description: 'Generate base64 hash',
    icon: <Hash className="h-5 w-5" />
  }
];

interface Props {
  onProcess: (entry: Omit<ProcessingEntry, 'id' | 'timestamp'>) => void;
}

export default function InputOutputSystem({ onProcess }: Props) {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [processingMode, setProcessingMode] = useState<ProcessingMode>('uppercase');
  const [isProcessing, setIsProcessing] = useState(false);

  const processInput = async () => {
    if (!input.trim()) return;

    setIsProcessing(true);
    const startTime = Date.now();

    // Simulate processing delay
    await new Promise(resolve => setTimeout(resolve, 500 + Math.random() * 1000));

    let result = '';
    
    switch (processingMode) {
      case 'uppercase':
        result = input.toUpperCase();
        break;
      case 'reverse':
        result = input.split('').reverse().join('');
        break;
      case 'count':
        const chars = input.length;
        const words = input.trim().split(/\s+/).filter(word => word.length > 0).length;
        result = `Characters: ${chars}, Words: ${words}`;
        break;
      case 'hash':
        result = `Hash: ${btoa(input)}`;
        break;
    }

    const processingTime = Date.now() - startTime;
    
    setOutput(result);
    setIsProcessing(false);

    onProcess({
      input,
      output: result,
      mode: processingModes.find(m => m.id === processingMode)?.name || processingMode,
      processingTime
    });
  };

  const clearAll = () => {
    setInput('');
    setOutput('');
  };

  return (
    <div className="bg-white/90 backdrop-blur-sm rounded-2xl border border-pink-200 p-6 shadow-lg">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">Processing System</h2>
        <p className="text-gray-600">Select a processing mode and transform your data</p>
      </div>

      {/* Processing Mode Selection */}
      <div className="mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-3">
          Processing Mode
        </label>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          {processingModes.map((mode) => (
            <button
              key={mode.id}
              onClick={() => setProcessingMode(mode.id)}
              className={`p-3 rounded-lg border transition-all duration-200 ${
                processingMode === mode.id
                  ? 'bg-gradient-to-r from-pink-500 to-fuchsia-500 border-pink-400 text-white'
                  : 'bg-white border-pink-200 text-gray-700 hover:bg-pink-50 hover:border-pink-300'
              }`}
            >
              <div className="flex items-center justify-center mb-2">
                {mode.icon}
              </div>
              <div className="text-sm font-medium">{mode.name}</div>
            </button>
          ))}
        </div>
        <p className="text-sm text-gray-600 mt-2">
          {processingModes.find(m => m.id === processingMode)?.description}
        </p>
      </div>

      {/* Input Section */}
      <div className="mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Input Data
        </label>
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter your data here..."
          className="w-full h-32 px-4 py-3 bg-white border border-pink-200 rounded-lg text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-transparent resize-none"
        />
      </div>

      {/* Action Buttons */}
      <div className="flex flex-wrap gap-3 mb-6">
        <button
          onClick={processInput}
          disabled={!input.trim() || isProcessing}
          className="flex items-center space-x-2 px-6 py-3 bg-gradient-to-r from-pink-500 to-fuchsia-500 text-white rounded-lg font-medium hover:from-pink-600 hover:to-fuchsia-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200"
        >
          <Play className="h-5 w-5" />
          <span>{isProcessing ? 'Processing...' : 'Process Input'}</span>
        </button>
        
        <button
          onClick={clearAll}
          className="flex items-center space-x-2 px-6 py-3 bg-gray-100 text-gray-700 rounded-lg font-medium hover:bg-gray-200 transition-all duration-200"
        >
          <RotateCcw className="h-5 w-5" />
          <span>Clear All</span>
        </button>
      </div>

      {/* Output Section */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Processed Output
        </label>
        <div className="relative">
          <textarea
            value={output}
            readOnly
            placeholder="Processed data will appear here..."
            className="w-full h-32 px-4 py-3 bg-gray-50 border border-pink-200 rounded-lg text-gray-800 placeholder-gray-400 resize-none font-mono"
          />
          {isProcessing && (
            <div className="absolute inset-0 bg-white/80 backdrop-blur-sm rounded-lg flex items-center justify-center">
              <div className="flex items-center space-x-3 text-gray-700">
                <div className="animate-spin rounded-full h-6 w-6 border-2 border-pink-500 border-t-transparent"></div>
                <span>Processing your data...</span>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}