import React, { useState } from "react";
import axios from "axios";

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [text, setText] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>("");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFile(e.target.files?.[0] || null);
    setText("");
    setError("");
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setError("");
      setText("");

      const response = await axios.post("http://127.0.0.1:8000/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      console.log("Backend response:", response.data);

      if (response.data.error) {
        setError(response.data.error);
      } else {
        setText(response.data.text || "No text extracted.");
      }
    } catch (err: any) {
      console.error("Upload error:", err);
      const backendMessage =
        err.response?.data?.detail || err.message || "Unexpected error occurred.";
      setError("Failed to upload or extract text: " + backendMessage);
    } finally {
      setLoading(false);
    }
  };


  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>TransformoDocs</h1>
      <input type="file" accept=".pdf,.docx,.txt" onChange={handleFileChange} />
      <button onClick={handleUpload} style={{ marginLeft: "1rem" }}>
        Upload & Extract
      </button>

      {loading && <p>Processing file...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {text && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Extracted Text:</h3>
          <pre style={{ whiteSpace: "pre-wrap", background: "#f4f4f4", padding: "1rem" }}>
            {text}
          </pre>
        </div>
      )}
    </div>
  );
};

export default App;
