import "./styles.css";
import { BrowserRouter, Link } from "react-router-dom";
import { Router } from "./router/Router";

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
      <Router />
    </BrowserRouter>
  );
};
