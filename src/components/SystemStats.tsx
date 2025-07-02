import React from 'react';
import { BarChart3, Clock, Activity, Zap } from 'lucide-react';
import { ProcessingEntry } from '../App';

interface Props {
  history: ProcessingEntry[];
}

export default function SystemStats({ history }: Props) {
  const totalOperations = history.length;
  const averageProcessingTime = history.length > 0 
    ? Math.round(history.reduce((sum, entry) => sum + entry.processingTime, 0) / history.length)
    : 0;
  
  const recentOperations = history.filter(
    entry => Date.now() - entry.timestamp.getTime() < 60000
  ).length;

  const stats = [
    {
      label: 'Total Operations',
      value: totalOperations.toLocaleString(),
      icon: <BarChart3 className="h-5 w-5" />,
      color: 'from-pink-500 to-rose-500'
    },
    {
      label: 'Avg Processing Time',
      value: `${averageProcessingTime}ms`,
      icon: <Clock className="h-5 w-5" />,
      color: 'from-fuchsia-500 to-pink-500'
    },
    {
      label: 'Recent Activity',
      value: `${recentOperations}/min`,
      icon: <Activity className="h-5 w-5" />,
      color: 'from-rose-500 to-pink-600'
    }
  ];

  return (
    <div className="bg-white/90 backdrop-blur-sm rounded-2xl border border-pink-200 p-6 shadow-lg">
      <div className="flex items-center space-x-2 mb-6">
        <Zap className="h-5 w-5 text-pink-600" />
        <h3 className="text-lg font-semibold text-gray-800">System Statistics</h3>
      </div>

      <div className="space-y-4">
        {stats.map((stat, index) => (
          <div key={index} className="bg-pink-50 rounded-lg p-4 border border-pink-100">
            <div className="flex items-center justify-between mb-2">
              <div className={`p-2 rounded-lg bg-gradient-to-r ${stat.color} text-white`}>
                {stat.icon}
              </div>
              <div className="text-right">
                <div className="text-2xl font-bold text-gray-800">{stat.value}</div>
                <div className="text-sm text-gray-600">{stat.label}</div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* System Status */}
      <div className="mt-6 p-4 bg-gradient-to-r from-green-100 to-emerald-100 rounded-lg border border-green-200">
        <div className="flex items-center space-x-2">
          <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
          <span className="text-green-700 font-medium">System Online</span>
        </div>
        <p className="text-green-600 text-sm mt-1">All systems operational</p>
      </div>
    </div>
  );
}