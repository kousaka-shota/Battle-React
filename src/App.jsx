import "./styles.css";
import { Home } from "./Home";
import { Page1 } from "./Page1";
import { Page2 } from "./Page2";
import { BrowserRouter, Link, Switch, Route } from "react-router-dom";
import { Page1DetailA } from "./Page1DetailA";
import { Page1DetailB } from "./Page1DetailB";

export const App = () => {
  return (
    <BrowserRouter>
      <div className="App">
        <Link to="/">Home</Link>
        <br />
        <Link to="/page1">page1</Link>
        <br />
        <Link to="/page2">page2</Link>
      </div>

      <Switch>
        <Route exact path="/">
          <Home />
        </Route>

        <Route
          path="/page1"
          render={() => (
            <Switch>
              <Route exact path="/page1">
                <Page1 />
              </Route>
              <Route path="/page1/detailA">
                <Page1DetailA />
              </Route>
              <Route path="/page1/detailB">
                <Page1DetailB />
              </Route>
            </Switch>
          )}
        />

        <Route path="/page2">
          <Page2 />
        </Route>
      </Switch>
    </BrowserRouter>
  );
};
