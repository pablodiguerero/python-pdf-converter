from typing import List

from pyppeteer import launch

from application.config import ChromeTask, ChromeResults
from application.fastapi import logger


async def get_files(tasks: List[ChromeTask]) -> List[ChromeResults]:
    results: List[ChromeResults] = []
    browser = await launch(options={"args": ["--no-sandbox"]})
    page = await browser.newPage()

    for task in tasks:
        logger.info(f"Get page {task.url}")

        try:
            await page.goto(task.url)
        except Exception as e:
            logger.exception(f"Got exception on page {task.url}")
            continue

        await page.setViewport({"width": 800, "height": 1200})
        results.append(ChromeResults(url=task.url, content=await page.pdf()))

    await browser.close()

    return results
