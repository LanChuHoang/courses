import asyncio
import pathlib
import re
import sys
import time
import urllib
from pathlib import Path

import aiofiles
from aiohttp import ClientSession

HREF_RE = re.compile(r'href="(.*?)"')

async def fetch(url: str, session: ClientSession):
  response = await session.request(method="GET", url=url)
  html = await response.text()
  return html

async def parse(url: str, html: str):
  found = set()
  for link in HREF_RE.findall(html):
      try:
          abslink = urllib.parse.urljoin(url, link)
      except (urllib.error.URLError, ValueError):
          print("Error parsing URL: %s", link)
          pass
      else:
          found.add(abslink)
  return found

async def save(file_path: Path, url: str, data: set):
  async with aiofiles.open(file_path, "a") as f:
      for found_url in data:
          await f.write(f"{url}\t{found_url}\n")

async def process_one(file_path: Path, url: str, session: ClientSession):
  try:
    html = await fetch(url, session)
    found_urls = await parse(url, html)
    await save(file_path, url, found_urls)
    print(f"Done processing {url}, got {len(found_urls)} urls")
  except Exception as e:
    print(f"Failed to process {url}, exception {e}")

async def bulk_craw_and_save(file_path: Path, urls: set):
  async with ClientSession() as session:
    tasks = []
    for url in urls:
      task = process_one(file_path, url, session)
      tasks.append(task)
    await asyncio.gather(*tasks)
    
    # for url in urls:
    #   await process_one(file_path, url, session)

if __name__ == "__main__":
  assert sys.version_info >= (3,7), "Require Python 3.7+"
  here = pathlib.Path(__file__).parent
  input_file_path = here.joinpath("urls.txt")
  output_file_path = here.joinpath("found_urls.txt")
  with open(input_file_path) as input_file:
    urls = set(map(str.strip, input_file))
  with open(output_file_path, "w") as output_file:
    output_file.write("source_url\tparsed_url\n")
  
  start = time.perf_counter()
  asyncio.run(bulk_craw_and_save(output_file_path, urls))
  elapsed = time.perf_counter() - start
  print(f"Program completed in {elapsed:0.5f} seconds.")