import React from 'react';
import { History, Trash2, Clock } from 'lucide-react';
import { ProcessingEntry } from '../App';

interface Props {
  history: ProcessingEntry[];
  onClear: () => void;
}

export default function ProcessingHistory({ history, onClear }: Props) {
  const formatTime = (date: Date) => {
    return date.toLocaleTimeString('en-US', {
      hour12: false,
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    });
  };

  const truncateText = (text: string, maxLength: number = 30) => {
    return text.length > maxLength ? `${text.substring(0, maxLength)}...` : text;
  };

  return (
    <div className="bg-white/90 backdrop-blur-sm rounded-2xl border border-pink-200 p-6 shadow-lg">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-2">
          <History className="h-5 w-5 text-pink-600" />
          <h3 className="text-lg font-semibold text-gray-800">Processing History</h3>
        </div>
        {history.length > 0 && (
          <button
            onClick={onClear}
            className="flex items-center space-x-1 px-3 py-1 text-sm text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-all duration-200"
          >
            <Trash2 className="h-4 w-4" />
            <span>Clear</span>
          </button>
        )}
      </div>

      <div className="space-y-3 max-h-96 overflow-y-auto">
        {history.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            <History className="h-12 w-12 mx-auto mb-3 opacity-50" />
            <p>No processing history yet</p>
            <p className="text-sm">Start processing data to see history</p>
          </div>
        ) : (
          history.map((entry) => (
            <div
              key={entry.id}
              className="bg-pink-50 rounded-lg p-4 border border-pink-100 hover:bg-pink-100 transition-all duration-200"
            >
              <div className="flex items-center justify-between mb-2">
                <span className="text-sm font-medium text-pink-700 bg-pink-200 px-2 py-1 rounded">
                  {entry.mode}
                </span>
                <div className="flex items-center space-x-2 text-xs text-gray-600">
                  <Clock className="h-3 w-3" />
                  <span>{formatTime(entry.timestamp)}</span>
                  <span>({entry.processingTime}ms)</span>
                </div>
              </div>
              
              <div className="space-y-2">
                <div>
                  <span className="text-xs text-gray-600 uppercase tracking-wide">Input:</span>
                  <p className="text-sm text-gray-800 font-mono bg-white rounded px-2 py-1 mt-1 border border-pink-100">
                    {truncateText(entry.input)}
                  </p>
                </div>
                
                <div>
                  <span className="text-xs text-gray-600 uppercase tracking-wide">Output:</span>
                  <p className="text-sm text-gray-800 font-mono bg-white rounded px-2 py-1 mt-1 border border-pink-100">
                    {truncateText(entry.output)}
                  </p>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}