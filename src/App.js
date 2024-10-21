import './App.css';
import React, { useState } from 'react';
import Checkviz from './components/Checkviz';
import ReliabilityMap from './components/ReliabilityMap';

function App() {
  const [labelon, setLabelon] = useState(false);
  const [dummy, setDummy] = useState(0);

  const handleToggle = () => {
    setLabelon(!labelon);
    console.log("Label state:", !labelon); // Log the new state
    setDummy(dummy => dummy + 1); // This forces a re-render
  };

  return (
    <div className="App app-container">
      <div className="label-container">
      <label>
        <input type="checkbox" checked={labelon} onChange={handleToggle} />
        Show Labels
      </label>
      </div>
      {/* <div className="square-content"> */}
        <header/>
        {/* <Checkviz
          method="tsne"
          dataset="mnist_sampled_50"
          isLabel={true}
          radius={5}
        /> */}
        <ReliabilityMap
          identifier="info_sample_5000_tsne_perplexity_5"
          isLabel= {labelon}
          showMissing={true}
          showFalse={true}
          radius={0.8}  // 1.8 for noncategory, 3 for category data
          stroke={3.0}
          drawEdge={true}
        />
        <footer/>
      </div>
    // </div>
  );
}

export default App;
