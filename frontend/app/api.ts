const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

const api = async (endpoint: string, options: RequestInit = {}) => {
  const res = await fetch(`${BASE_URL}/api/${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });

  if (!res.ok) {
    const errorText = await res.text().catch(() => "");
    throw new Error(`HTTP Error: ${res.status} ${errorText}`);
  }

  const contentType = res.headers.get("content-type");

  if (contentType && contentType.includes("application/json")) {
    return res.json();
  }

  return null; 
};

export default api;