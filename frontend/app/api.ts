const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}api/endpoint`, {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
  },
});

const data = await res.json();

export { };
