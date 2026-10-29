const { chromium } = require("playwright");

function requiredEnv(name) {
  const value = process.env[name];
  if (!value) throw new Error(`Missing environment variable ${name}. Set it before running.`);
  return value;
}

(async () => {
  const browser = await chromium.launch({
    proxy: {
      server: requiredEnv("PROXY_SERVER"),
      username: requiredEnv("PROXY_USERNAME"),
      password: requiredEnv("PROXY_PASSWORD"),
    },
  });

  try {
    const page = await browser.newPage();
    const response = await page.goto("https://api.ipify.org?format=json", {
      waitUntil: "domcontentloaded",
      timeout: 30_000,
    });
    console.log("HTTP status:", response ? response.status() : "No response");
    console.log("IP-check response:", await page.locator("body").innerText());
  } finally {
    await browser.close();
  }
})().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
