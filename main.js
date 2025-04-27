function runTest() {
  const url = document.getElementById('urlInput').value;

  if (!url.startsWith("http")) {
    alert("Please enter a valid URL starting with http:// or https://");
    return;
  }

  fetch('http://localhost:5000/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url: url })
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      alert("Error: " + data.error);
      console.error("Error details:", data.details || data.raw);
      return;
    }

    document.querySelector('#lcp span').innerText = `LCP: ${data.LCP.toFixed(2)} ms`;
    document.querySelector('#fid span').innerText = `FID: ${data.FID.toFixed(2)} ms`;
    document.querySelector('#cls span').innerText = `CLS: ${data.CLS}`;
  })
  .catch(err => {
    console.error("Request failed", err);
    alert("Something went wrong. See console.");
  });
}
