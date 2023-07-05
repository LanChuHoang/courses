import asyncio

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://core.datxasia.com/graphql")

with open('./graphql/client/gql-python/schema.graphql') as f:
    schema_str = f.read()
    
def exception_handler(func):
  async def wrapper(*args, **kwargs):
    try:
      result = await func(*args, **kwargs)
      print(result)
      return result 
    except TransportQueryError as e:
      print("eee ", e.errors)
      # raise Exception( "lololo")
      return e.errors
  return wrapper

@exception_handler
async def get():
  async with Client(transport=transport, schema=schema_str) as session:
    query = gql(
        """
          query DRF {
            derivativesRecommendation(input: {
              startDate: "2023-07-03f",
              endDate: "2023-07-04",
              tickers: ["VN30F2307"]
            }) {
              id,
              date,
              ticker,
              type,
              role,
              price,
              quantity,
              holdingPercentage,
              normedPnlPoint
            }
          }
        """
    )
    result = await session.execute(query)
  return result

async def main():
  await get()
  
asyncio.run(main())
asyncio.run(main())