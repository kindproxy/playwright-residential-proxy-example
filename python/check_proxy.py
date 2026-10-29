import asyncio
import os
from playwright.async_api import async_playwright


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable {name}. Set it before running.")
    return value


async def main() -> None:
    proxy = {
        "server": required_env("PROXY_SERVER"),
        "username": required_env("PROXY_USERNAME"),
        "password": required_env("PROXY_PASSWORD"),
    }

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(proxy=proxy)
        try:
            page = await browser.new_page()
            response = await page.goto(
                "https://api.ipify.org?format=json",
                wait_until="domcontentloaded",
                timeout=30_000,
            )
            print("HTTP status:", response.status if response else "No response")
            print("IP-check response:", await page.locator("body").inner_text())
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
