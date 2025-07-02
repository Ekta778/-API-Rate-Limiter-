import React, { useState } from 'react';
import { Shield, Activity, Clock, BarChart3 } from 'lucide-react';
import InputOutputSystem from './components/InputOutputSystem';
import ProcessingHistory from './components/ProcessingHistory';
import SystemStats from './components/SystemStats';

export interface ProcessingEntry {
  id: string;
  input: string;
  output: string;
  mode: string;
  timestamp: Date;
  processingTime: number;
}

function App() {
  const [history, setHistory] = useState<ProcessingEntry[]>([]);

  const addToHistory = (entry: Omit<ProcessingEntry, 'id' | 'timestamp'>) => {
    const newEntry: ProcessingEntry = {
      ...entry,
      id: Date.now().toString(),
      timestamp: new Date(),
    };
    
    setHistory(prev => [newEntry, ...prev.slice(0, 49)]); // Keep last 50 entries
  };

  const clearHistory = () => {
    setHistory([]);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-100 via-pink-50 to-rose-100">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-pink-200 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-gradient-to-r from-pink-500 to-fuchsia-500 rounded-lg">
                <Shield className="h-8 w-8 text-white" />
              </div>
              <div>
                <h1 className="text-3xl font-bold text-gray-800">API Rate Limiter</h1>
                <p className="text-gray-600">Beautiful traffic control system</p>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-6">
              <div className="flex items-center space-x-2 text-gray-600">
                <Activity className="h-5 w-5" />
                <span>Real-time Processing</span>
              </div>
              <div className="flex items-center space-x-2 text-gray-600">
                <Clock className="h-5 w-5" />
                <span>Live Analytics</span>
              </div>
              <div className="flex items-center space-x-2 text-gray-600">
                <BarChart3 className="h-5 w-5" />
                <span>Performance Metrics</span>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Input/Output System */}
          <div className="lg:col-span-2">
            <InputOutputSystem onProcess={addToHistory} />
          </div>

          {/* System Stats */}
          <div className="space-y-8">
            <SystemStats history={history} />
            <ProcessingHistory history={history} onClear={clearHistory} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;