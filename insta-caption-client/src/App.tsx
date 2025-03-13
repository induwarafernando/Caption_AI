import React, { useState } from "react";
import axios from "axios";

const App: React.FC = () => {
    const [prompt, setPrompt] = useState("");
    const [caption, setCaption] = useState("");

    const handleGenerate = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:8000/generate-caption", { prompt });
            setCaption(response.data.caption);
        } catch (error) {
            console.error("Error generating caption:", error);
            setCaption("⚠️ Failed to generate caption. Please try again.");
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
            <h1 className="text-3xl font-bold mb-4">📸 Instagram Caption Generator</h1>
            <input
                className="border p-2 w-80 text-black"
                placeholder="Describe your photo..."
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
            />
            <button className="mt-4 bg-blue-500 p-2 rounded-lg" onClick={handleGenerate}>
                Generate Caption
            </button>
            {caption && <p className="mt-4 text-lg">{caption}</p>}
        </div>
    );
};

export default App;
