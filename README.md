# Playwright Residential Proxy Examples

Practical examples for configuring an HTTP proxy in Playwright with Python and Node.js.

## Features
- Python and Node.js examples
- HTTP proxy with username/password authentication
- Linux and Windows setup notes
- Exit-IP verification
- Basic troubleshooting guidance

> These examples focus on HTTP proxy configuration. Test SOCKS5 authentication separately; compatibility can depend on the client, endpoint, and authentication method.

## Requirements
- Python 3.9+ or a supported Node.js version
- Playwright and Chromium
- A working proxy endpoint and valid credentials

## Configure your proxy
Copy `.env.example` to `.env`, then replace the placeholders with your own endpoint and credentials. Never commit real credentials.

```dotenv
PROXY_SERVER=http://your-proxy-host:your-port
PROXY_USERNAME=your-username
PROXY_PASSWORD=your-password
```

Python does not automatically load `.env` in this example. Export the variables in your shell before running the script.

## Python setup
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r python/requirements.txt
python -m playwright install chromium
```

On Windows PowerShell, activate with `.venv\\Scripts\\Activate.ps1`. On Linux, if system libraries are missing, run:

```bash
python -m playwright install --with-deps chromium
```

Run the check:

```bash
python python/check_proxy.py
```

## Node.js setup
```bash
npm install
npx playwright install chromium
node --env-file=.env nodejs/check-proxy.js
```

The `--env-file` option requires a compatible Node.js version. Alternatively, export the three environment variables in your shell and run `node nodejs/check-proxy.js`.

## Interpret the result
A successful IP-check response should contain an IP address. Compare it with a direct connection to see whether the visible exit IP changed.

Keep these checks separate:
- **Proxy connectivity:** the IP-check page loads.
- **Exit IP/location:** the returned address and reported location match your expectations closely enough.
- **Target website:** the destination returns the content your workflow expects.

A working proxy connection does not guarantee every target website will return its expected content. Geolocation databases can disagree.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Proxy authentication error or HTTP 407 | Verify username, password, and authentication method. |
| Navigation timeout | Check endpoint, port, protocol, and network connectivity. |
| Unexpected exit location | Verify location settings and compare geolocation results. |
| IP check works but target page fails | Inspect the destination response separately. |

## Documentation
- [Playwright network and proxy settings](https://playwright.dev/python/docs/network)
- [Playwright Python getting started](https://playwright.dev/python/docs/intro)
- [KindProxy residential proxy plans](https://www.kindproxy.com/pricing/residential-proxies/traffic/?spread=github)

## License
Released under the MIT License. See [LICENSE](LICENSE).
