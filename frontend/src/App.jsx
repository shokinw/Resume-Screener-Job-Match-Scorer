import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [jd, setJd] = useState("");
  const [resumeId, setResumeId] = useState(null);
  const [result, setResult] = useState(null);

  // Upload Resume
  const uploadResume = async () => {

    const formData = new FormData();

    formData.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:8000/upload",formData
    );

    console.log(res.data);

    setResumeId(res.data.resume_id);

    alert(
      "Uploaded Resume ID: " +
      res.data.resume_id
  );
};

  // Match Resume
  const matchResume = async () => {
    const res = await axios.post("http://127.0.0.1:8000/match",
  {
    resume_id: resumeId,
    jd_text: jd
  }
);

    setResult(res.data);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>Resume Screener AI</h1>

      {/* Upload */}
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadResume}>Upload Resume</button>

      <hr />

      {/* JD Input */}
      <textarea
        rows="6"
        cols="50"
        placeholder="Paste Job Description"
        onChange={(e) => setJd(e.target.value)}
      />

      <br />

      <button onClick={matchResume}>Match Resume</button>

      {/* Result */}
      {result && (
        <div>
          <h2>Match Score: {result.match_score}</h2>
        </div>
      )}
    </div>
  );
}

export default App;