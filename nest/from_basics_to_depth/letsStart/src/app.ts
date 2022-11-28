import * as express from "express";
const app: express.Express = express();
const port: number = 8000;
class Server {
  public app: express.Application;

  constructor(){
    const app: express.Application = express{}
    this.app = app
  }
}

app.get("/", (req: express.Request, res: express.Response) => {
  res.send("Hellow World");
});

app.listen(port, () => {
  console.log("E");
});
