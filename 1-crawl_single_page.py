import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url = "https://www.linkedin.com/in/asad-panhwar-03aa92236/"
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())
    
