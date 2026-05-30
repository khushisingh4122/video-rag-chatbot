"use client";

import { useState } from "react";

export default function Home() {
  const [videoA, setVideoA] = useState("");
  const [videoB, setVideoB] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const analyzeVideos = async () => {
    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            youtube_url: videoA,
            instagram_url: videoB,
          }),
        }
      );

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error(error);

      setResult({
        success: false,
        error: "Could not connect to backend",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-950 text-white p-8">
      <h1 className="text-5xl font-bold text-center mb-3">
        🎥 Video Intelligence Dashboard
      </h1>

      <p className="text-center text-gray-400 mb-10">
        Compare YouTube videos using views, likes,
        engagement, scores and AI analysis
      </p>

      <div className="grid md:grid-cols-2 gap-6">
        <div className="bg-slate-900 p-6 rounded-xl shadow-lg">
          <h2 className="text-xl font-bold mb-4">
            Video A
          </h2>

          <input
            value={videoA}
            onChange={(e) => setVideoA(e.target.value)}
            placeholder="Paste YouTube URL"
            className="w-full p-3 rounded bg-slate-800"
          />
        </div>

        <div className="bg-slate-900 p-6 rounded-xl shadow-lg">
          <h2 className="text-xl font-bold mb-4">
            Video B
          </h2>

          <input
            value={videoB}
            onChange={(e) => setVideoB(e.target.value)}
            placeholder="Paste YouTube URL"
            className="w-full p-3 rounded bg-slate-800"
          />
        </div>
      </div>

      <div className="text-center mt-8">
        <button
          onClick={analyzeVideos}
          className="bg-purple-600 hover:bg-purple-700 px-8 py-3 rounded-lg font-bold"
        >
          Analyze Videos
        </button>
      </div>

      {loading && (
        <div className="mt-8 bg-slate-900 p-6 rounded-xl text-center">
          ⏳ Analyzing videos...
        </div>
      )}

      {result?.success && (
        <div className="mt-8">
          <h2 className="text-3xl font-bold mb-6">
            Analysis Result
          </h2>

          <div className="grid md:grid-cols-2 gap-6">

            <div className="bg-slate-900 p-6 rounded-xl">
              <h3 className="text-2xl font-bold mb-4">
                🎬 Video A
              </h3>

              {result.video_a?.thumbnail && (
                <img
                  src={result.video_a.thumbnail}
                  alt="Video A"
                  className="w-full rounded-lg mb-4"
                />
              )}

              <p><strong>Title:</strong> {result.video_a?.title}</p>
              <p><strong>Channel:</strong> {result.video_a?.channel}</p>
              <p><strong>Views:</strong> {result.video_a?.views?.toLocaleString()}</p>
              <p><strong>Likes:</strong> {result.video_a?.likes?.toLocaleString()}</p>
              <p><strong>Duration:</strong> {result.video_a?.duration}</p>
              <p><strong>Engagement:</strong> {result.video_a?.engagement}%</p>
              <p><strong>Score:</strong> {result.video_a?.score?.toLocaleString()}</p>

              <div className="mt-2 bg-slate-700 rounded-full h-4">
                <div
                  className="bg-green-500 h-4 rounded-full"
                  style={{
                    width: `${Math.min(
                      (result.video_a?.engagement || 0) * 10,
                      100
                    )}%`,
                  }}
                />
              </div>
            </div>

            <div className="bg-slate-900 p-6 rounded-xl">
              <h3 className="text-2xl font-bold mb-4">
                🎬 Video B
              </h3>

              {result.video_b?.thumbnail && (
                <img
                  src={result.video_b.thumbnail}
                  alt="Video B"
                  className="w-full rounded-lg mb-4"
                />
              )}

              <p><strong>Title:</strong> {result.video_b?.title}</p>
              <p><strong>Channel:</strong> {result.video_b?.channel}</p>
              <p><strong>Views:</strong> {result.video_b?.views?.toLocaleString()}</p>
              <p><strong>Likes:</strong> {result.video_b?.likes?.toLocaleString()}</p>
              <p><strong>Duration:</strong> {result.video_b?.duration}</p>
              <p><strong>Engagement:</strong> {result.video_b?.engagement}%</p>
              <p><strong>Score:</strong> {result.video_b?.score?.toLocaleString()}</p>

              <div className="mt-2 bg-slate-700 rounded-full h-4">
                <div
                  className="bg-green-500 h-4 rounded-full"
                  style={{
                    width: `${Math.min(
                      (result.video_b?.engagement || 0) * 10,
                      100
                    )}%`,
                  }}
                />
              </div>
            </div>

          </div>

          <div className="mt-6 bg-green-700 p-6 rounded-xl text-center">
            <h2 className="text-3xl font-bold">
              🏆 Winner: {result.winner}
            </h2>
          </div>

          <div className="mt-4 bg-yellow-600 p-4 rounded-xl text-center">
            <h3 className="text-2xl font-bold">
              ⭐ Best Engagement: {result.engagement_winner}
            </h3>
          </div>
          <div className="grid md:grid-cols-3 gap-4 mt-6">

            <div className="bg-slate-900 p-5 rounded-xl text-center shadow-lg">
              <h3 className="text-lg font-bold mb-2">
                👀 Views Difference
              </h3>

              <p className="text-2xl font-bold text-green-400">
                {result.views_difference?.toLocaleString()}
              </p>
            </div>

            <div className="bg-slate-900 p-5 rounded-xl text-center shadow-lg">
              <h3 className="text-lg font-bold mb-2">
                👍 Likes Difference
              </h3>

              <p className="text-2xl font-bold text-blue-400">
                {result.likes_difference?.toLocaleString()}
              </p>
            </div>

            <div className="bg-slate-900 p-5 rounded-xl text-center shadow-lg">
              <h3 className="text-lg font-bold mb-2">
                🔥 Engagement Difference
              </h3>

              <p className="text-2xl font-bold text-yellow-400">
                {result.engagement_difference}%
              </p>
            </div>

          </div>
          <div className="mt-6 bg-blue-900 p-6 rounded-xl">
            <h2 className="text-2xl font-bold mb-4">
              🤖 AI Summary
            </h2>

            <pre className="whitespace-pre-wrap">
              {result.summary}
            </pre>
          </div>

          <div className="mt-6 text-center">
            <button
              onClick={() => {
                const blob = new Blob(
                  [result.summary],
                  { type: "text/plain" }
                );

                const url =
                  window.URL.createObjectURL(blob);

                const a =
                  document.createElement("a");

                a.href = url;
                a.download =
                  "video-analysis-report.txt";

                a.click();
              }}
              className="bg-purple-600 hover:bg-purple-700 px-6 py-3 rounded-lg font-bold"
            >
              📥 Download Report
            </button>
          </div>

        </div>
      )}

      {result?.error && (
        <div className="mt-8 bg-red-700 p-6 rounded-xl">
          {result.error}
        </div>
      )}
    </main>
  );
}