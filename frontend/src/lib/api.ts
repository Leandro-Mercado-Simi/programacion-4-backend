const BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const apiFetch = async <T>(
  endpoint: string,
  options?: {
    method?: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
    body?: unknown;
  },
): Promise<T> => {
  const response = await fetch(`${BASE_URL}${endpoint}`, {
    method: options?.method ?? "GET",
    headers: { "Content-Type": "application/json" },
    body: options?.body ? JSON.stringify(options.body) : undefined,
  });

  if (!response.ok) throw new Error(`HTTP error: ${response.status}`);

  if (response.status === 204) return undefined as T;

  return response.json();
};
