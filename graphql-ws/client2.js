const { createClient } = require("graphql-ws");
const WebSocket = require("ws");

class MyWebSocket extends WebSocket {
  constructor(address, protocols) {
    super(address, protocols, {
      headers: {
        authToken:
          "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InVzZXJpZCI6IjY0N2VlOTM3ZjNkZTM5MjVmYjFiOWFiYiIsImRldmljZWlkIjoiNjQ4MmFlNGIwYmEyZTkyMzNkNWE3NjdmIn0sImlhdCI6MTY4NjI4NTg5OSwiZXhwIjoxNjg2ODkwNjk5fQ.1hV217oFlZUJGPODQb9BHBVeIX6eHqG_eqdAqWaBHSE",
        origin: "http://localhost:3000",
      },
    });
  }
}

const wsClient = createClient({
  url: "wss://dev-core.datxasia.com/graphql",
  webSocketImpl: MyWebSocket,
});

async function wsExecute(payload) {
  return new Promise((resolve, reject) => {
    let result;
    wsClient.subscribe(payload, {
      next: (data) => resolve(data),
      error: reject,
      complete: () => resolve(result),
    });
  });
}

async function test() {
  try {
    const result = await wsExecute({
      query: /* GraphQL */ `
        subscription sectorsRating {
          sectorsRating {
            timestamp
            data {
              sector
              rank
            }
          }
        }
      `,
    });
    console.dir(result, { depth: null });
  } catch (error) {
    console.log(error);
  }
}

test();

// wsClient.dispose();
// subscription {
//   recommendationBotLatest(recommendationType: SHORT_RECOMMENDATION) {
//     id
//     openDate
//     openPrice
//     closedDate
//     closedPrice
//     ticker
//   }
// }

// subscription sectorsRating {
//   sectorsRating {
//     timestamp
//     data {
//       sector
//       rank
//     }
//   }
// }

// const a = {
//   data: {
//     recommendationBotLatest: {
//       timestamp: 1686291051,
//       data: {
//         id: "id",
//         openDate: "openDate",
//         openPrice: "openPrice",
//         closedDate: "closedDate",
//         closedPrice: "closedPrice",
//         ticker: "ticker",
//       },
//     },
//   },
// };
